import pytest
from conftest import ready,raw,consensus,invariant,error
BAD=[
    'not JSON','```json\n{"matrix":[["EQUIVALENT"]]}\n```',
    '{"matrix":[]}','{"matrix":[[],[]]}','{"matrix":[["EQUIVALENT","UNRELATED"]]}',
    '{"matrix":[["EQUIVALENT"],["EQUIVALENT"]]}','{"matrix":[["AGREEMENT"]]}',
    '{"matrix":[["equivalent"]]}','{"matrix":[[1]]}','{"matrix":[[null]]}',
    '{"matrix":[[true]]}','{"matrix":[[{}]]}','{"matrix":["EQUIVALENT"]}',
    '{"matrix":null}','{"matrix":[["EQUIVALENT"]],"reason":"ok"}',
    '{"matrix":[["EQUIVALENT"]],"matrix":[["CONFLICT"]]}','[]','null',
    '{"matrix":[[NaN]]}','{"matrix":[["EQUIVALENT"]]} trailing prose',
]

@pytest.mark.parametrize('output',BAD)
def test_C06_malformed_leader_no_state_mutation(env,output):
    e=env;wid=ready(e);before=e.c.get_workspace(wid);storage=e.vm._storage.snapshot();e.outputs=[output]
    with pytest.raises(e.m.gl.vm.UserError,match='INVALID_CONSENSUS_OUTPUT'):e.c.reconcile(wid)
    # Actual contract rejection before any speculative matrix write; no manual revert.
    assert e.c.get_workspace(wid)==before and e.vm._storage.snapshot()==storage;invariant(e)

@pytest.mark.parametrize('output',BAD)
def test_C07_malformed_validator_never_approves(env,output):
    e=env;wid=ready(e);before=e.c.get_workspace(wid)
    votes,accepted=consensus(e,wid,raw([['EQUIVALENT']]),[output])
    assert votes==[False] and not accepted and e.c.get_workspace(wid)==before;invariant(e)

@pytest.mark.parametrize('kind',['leader_failure','leader_timeout','validator_failure','validator_timeout','FAILED','REJECTED','UNDETERMINED'])
def test_failure_lifecycle_returns_READY(env,kind):
    e=env;wid=ready(e);before=e.c.get_workspace(wid);storage=e.vm._storage.snapshot();good=raw([['EQUIVALENT']])
    if kind.startswith('leader'):
        e.outputs=[TimeoutError('model timeout') if kind.endswith('timeout') else RuntimeError('model failed')]
        with pytest.raises(Exception):e.c.reconcile(wid)
    else:
        validator=TimeoutError('model timeout') if kind=='validator_timeout' else RuntimeError('model failed') if kind=='validator_failure' else good
        votes,accepted=consensus(e,wid,good,[validator],decision=kind)
        assert not accepted
        if kind.startswith('validator'):assert votes==[False]
    assert e.c.get_workspace(wid)==before and e.vm._storage.snapshot()==storage
    assert before['derived_status']=='READY' and before['relation_matrix']==[] and before['reconciled'] is False
    invariant(e)

def test_invalid_wrapped_leader_never_runs_validator_AI(env):
    e=env;wid=ready(e);good=raw([['EQUIVALENT']]);e.outputs=[good];e.c.reconcile(wid)
    count=len(e.prompts)
    assert not e.vm.run_validator(leader_error=RuntimeError('Leader failed'))
    assert not e.vm.run_validator(leader_result=BAD[0])
    assert len(e.prompts)==count

@pytest.mark.parametrize('value',[None,{},[],1,True])
def test_parser_rejects_non_text(env,value):
    with pytest.raises(env.m.gl.vm.UserError,match='INVALID_CONSENSUS_OUTPUT'):env.m._parse_matrix(value,1,1)

def test_manual_reconcile_after_definite_mock_disagreement(env):
    e=env;wid=ready(e);good=raw([['EQUIVALENT']])
    assert not consensus(e,wid,good,[raw([['UNRELATED']])])[1]
    assert e.c.get_workspace(wid)['derived_status']=='READY'
    assert consensus(e,wid,good,[good])[1]
    assert e.c.get_workspace(wid)['relation_matrix']==[1];invariant(e)

def test_final_accepted_boundary_output_reparsed(env,monkeypatch):
    e=env;wid=ready(e)
    monkeypatch.setattr(e.m.gl.vm,'run_nondet_unsafe',lambda leader,validator:BAD[0])
    error(e,'INVALID_CONSENSUS_OUTPUT',lambda:e.c.reconcile(wid))

@pytest.mark.parametrize('semantic',['ALREADY_RECONCILED','INVALID_CONSENSUS_OUTPUT',None])
def test_server_error_evidence_never_retains_sensitive_configuration(semantic):
    import base64,importlib.util,json
    from pathlib import Path
    path=Path(__file__).resolve().parents[1]/'verification/rpc_evidence.py'
    spec=importlib.util.spec_from_file_location('rpc_evidence_test',path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    marker='SENSITIVE_MARKER_DO_NOT_RETAIN'
    payload={'code':-32000,'message':marker,'data':{'receipt':{'execution_result':'ERROR','result':base64.b64encode(b'\x01'+(semantic or marker).encode()).decode(),'node_config':{'private_key':marker,'api_key':marker,'password':marker}},'secret':marker}}
    ex=module.SafeRPCError('gen_call',payload)
    assert marker not in str(ex)+json.dumps(ex.evidence)
    assert 'node_config' not in json.dumps(ex.evidence)
    assert ex.evidence.get('decoded_user_error')==semantic
