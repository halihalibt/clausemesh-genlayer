"""Pinned SDK storage tests; direct-mode consensus rollback is explicit simulation."""
import json
import sys
from pathlib import Path
from types import SimpleNamespace
import pytest
from gltest.direct.loader import deploy_contract
from gltest.direct.vm import VMContext
ROOT=Path(__file__).resolve().parents[1]
RESULTS=[]

@pytest.fixture
def env(monkeypatch):
    vm=VMContext()
    with vm.activate():
        c=deploy_contract(ROOT/'contracts/clause_mesh.py',vm,sdk_version='v0.2.16')
        from genlayer import Address
        a,b,t=[Address('0x'+ch*40) for ch in '123']
        module=sys.modules[type(c._instance).__module__]
        vm.sender=a
        e=SimpleNamespace(vm=vm,c=c,a=a,b=b,t=t,m=module,prompts=[])
        e.outputs=[]
        def responder(prompt):
            e.prompts.append(prompt)
            if not e.outputs: raise RuntimeError('No mock response configured')
            response=e.outputs.pop(0)
            if isinstance(response,Exception): raise response
            return json.dumps(response)
        monkeypatch.setattr(vm,'_match_llm_mock',responder)
        yield e

def raw(matrix):return json.dumps({'matrix':matrix},separators=(',',':'))

def ready(e,a=None,b=None,label='test'):
    e.vm.sender=e.a
    wid=e.c.create_workspace(e.b,label,a or ['Mobile access is required.'])
    e.vm.sender=e.b
    e.c.respond_and_seal(wid,b or ['Mobile access is required.'])
    e.vm.sender=e.t
    return wid

def consensus(e,wid,leader,validators,decision=None):
    """Execute actual callbacks, then simulate GenLayer commit/discard using SDK snapshots.

    Direct mode does not implement chain consensus: it speculatively writes.
    This adapter never edits the contract or substitutes the equivalence rule.
    Chain finalization is independently verified in the remote test.
    """
    snap=e.vm.snapshot()
    e.outputs=[leader]
    try:
        e.c.reconcile(wid)
        votes=[]
        for output in validators:
            e.outputs=[output]
            votes.append(e.vm.run_validator())
        accepted=all(votes) and decision not in ('FAILED','REJECTED','UNDETERMINED')
        if not accepted:e.vm.revert(snap)
        return votes,accepted
    except Exception:
        e.vm.revert(snap)
        raise

def invariant(e):
    c=e.c
    assert int(c.workspace_count)==len(c.workspaces)
    assert c.protocol_version=='CLAUSEMESH-V1'
    for wid in range(1,int(c.workspace_count)+1):
        w=c.get_workspace(wid)
        assert w['id']==wid and w['party_a']!=w['party_b']
        assert 1<=len(w['clauses_a'])<=4
        assert all(3<=len(x)<=240 and x==x.strip() for x in w['clauses_a']+w['clauses_b'])
        assert len(w['label'])<=80
        assert (1<=len(w['clauses_b'])<=4) if w['party_b_submitted'] else w['clauses_b']==[]
        if w['reconciled']:
            assert w['party_b_submitted'] and len(w['relation_matrix'])==len(w['clauses_a'])*len(w['clauses_b'])
            assert all(type(x) is int and 0<=x<=3 for x in w['relation_matrix'])
            assert w['derived_status']=='RECONCILED'
        else:
            assert w['relation_matrix']==[]
            assert w['derived_status']==('READY' if w['party_b_submitted'] else 'WAITING_FOR_B')
        assert wid in [s['id'] for s in c.get_workspace_summaries(w['party_a'])]
        assert (wid in [s['id'] for s in c.get_workspace_summaries(w['party_b'])])==w['party_b_submitted']

def error(e,code,fn):
    before=e.vm._storage.snapshot()
    with pytest.raises(e.m.gl.vm.UserError,match=code):fn()
    assert e.vm._storage.snapshot()==before
    invariant(e)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome=yield
    report=outcome.get_result()
    if report.when=='call' or (report.when=='setup' and report.failed):
        RESULTS.append({'test':item.nodeid,'outcome':report.outcome,'duration_seconds':round(report.duration,5),'failure':str(report.longrepr) if report.failed else None})

def pytest_sessionfinish(session,exitstatus):
    target=ROOT/'evidence/phase2-local.json'
    target.write_text(json.dumps({'scope':'Phase 2 local SDK storage and mocked consensus; chain rollback model explicitly simulated','exit_status':exitstatus,'passed':sum(r['outcome']=='passed' for r in RESULTS),'failed':sum(r['outcome']=='failed' for r in RESULTS),'skipped':sum(r['outcome']=='skipped' for r in RESULTS),'tests':RESULTS},indent=2)+'\n')
