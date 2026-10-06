import pytest
from conftest import ready,raw,consensus,error,invariant

@pytest.mark.parametrize('kind',['zero','self'])
def test_T02_counterparty(env,kind):
    e=env;party=e.m.ZERO_ADDRESS if kind=='zero' else e.a
    error(e,'INVALID_COUNTERPARTY',lambda:e.c.create_workspace(party,'',['abc']))

@pytest.mark.parametrize('caller',['a','t'])
def test_T05_only_B_can_respond(env,caller):
    e=env;wid=e.c.create_workspace(e.b,'',['abc']);e.vm.sender=getattr(e,caller)
    error(e,'UNAUTHORIZED',lambda:e.c.respond_and_seal(wid,['abc']))

def test_T06_double_seal(env):
    e=env;wid=ready(e);sealed=e.c.get_workspace(wid);e.vm.sender=e.b
    error(e,'ALREADY_SEALED',lambda:e.c.respond_and_seal(wid,['changed']))
    assert e.c.get_workspace(wid)==sealed

def test_T07_not_ready_no_AI(env):
    e=env;wid=e.c.create_workspace(e.b,'',['abc'])
    error(e,'NOT_READY',lambda:e.c.reconcile(wid));assert e.prompts==[]

@pytest.mark.parametrize('caller',['a','b','t'])
def test_permissionless_and_T08_success_immutable(env,caller):
    e=env;wid=ready(e);e.vm.sender=getattr(e,caller)
    output=raw([['EQUIVALENT']]);assert consensus(e,wid,output,[output])[1]
    sealed=e.c.get_workspace(wid);calls=len(e.prompts)
    error(e,'ALREADY_RECONCILED',lambda:e.c.reconcile(wid))
    assert len(e.prompts)==calls and e.c.get_workspace(wid)==sealed
    e.vm.sender=e.b;error(e,'ALREADY_SEALED',lambda:e.c.respond_and_seal(wid,['changed']))
    assert e.c.get_workspace(wid)==sealed;invariant(e)
