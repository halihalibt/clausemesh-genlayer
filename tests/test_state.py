import pytest
from conftest import ready,raw,consensus,invariant,error

def test_T01_creation_and_T04_response(env):
    e=env; assert int(e.c.workspace_count)==0
    assert e.c.get_workspace_summaries(e.a)==[]
    wid=e.c.create_workspace(e.b,'  标签  ',['  AbC  内部\n空格。  ','same','same'])
    w=e.c.get_workspace(wid)
    assert wid==1 and w['label']=='标签'
    assert w['party_a']==e.a and w['party_b']==e.b
    assert w['clauses_a']==['AbC  内部\n空格。','same','same']
    assert not w['party_b_submitted'] and w['derived_status']=='WAITING_FOR_B'
    assert e.c.get_workspace_summaries(e.b)==[]
    invariant(e)
    e.vm.sender=e.b;e.c.respond_and_seal(wid,['  回复要求  ','回复要求'])
    w=e.c.get_workspace(wid)
    assert w['clauses_b']==['回复要求','回复要求'] and w['derived_status']=='READY'
    assert e.c.get_workspace_summaries(e.b)[0]['status']=='READY'
    invariant(e)

@pytest.mark.parametrize('label',['',' '*3,'字'*80])
@pytest.mark.parametrize('clause',['abc','字'*240])
def test_T03_inclusive_bounds(env,label,clause):
    e=env;wid=ready(e,[clause]*4,[clause]*4,label);assert e.c.get_workspace(wid)['label']==label.strip();invariant(e)

@pytest.mark.parametrize('side',['a','b'])
@pytest.mark.parametrize('clauses,code',[([],'INVALID_CLAUSE_COUNT'),(['abc']*5,'INVALID_CLAUSE_COUNT'),(['ab'],'INVALID_CLAUSE'),(['x'*241],'INVALID_CLAUSE'),([' \n\t '],'INVALID_CLAUSE'),(['abc','ab'],'INVALID_CLAUSE'),(['abc',None],'INVALID_CLAUSE')])
def test_T03_invalid_clauses_no_partial_write(env,side,clauses,code):
    e=env
    if side=='a':fn=lambda:e.c.create_workspace(e.b,'',clauses)
    else:
        wid=e.c.create_workspace(e.b,'',['abc']);e.vm.sender=e.b
        fn=lambda:e.c.respond_and_seal(wid,clauses)
    error(e,code,fn)

@pytest.mark.parametrize('label',['x'*81,None])
def test_T03_invalid_label(env,label):error(env,'INVALID_LABEL',lambda:env.c.create_workspace(env.b,label,['abc']))

def test_duplicate_creation_and_history_order(env):
    e=env
    for wid in range(1,4):assert e.c.create_workspace(e.b,'same',['same','same'])==wid
    assert [w['id'] for w in e.c.get_workspace_summaries(e.a)]==[1,2,3]
    assert e.c.get_workspace_summaries(e.b)==[]
    e.vm.sender=e.b;e.c.respond_and_seal(2,['same']);e.c.respond_and_seal(1,['same'])
    # Persistent history remains append order; the view returns ascending IDs.
    assert [int(wid) for wid in e.c.workspace_ids_by_party[e.b]]==[2,1]
    assert [w['id'] for w in e.c.get_workspace_summaries(e.b)]==[1,2]
    invariant(e)

@pytest.mark.parametrize('wid',[0,-1,2,True])
@pytest.mark.parametrize('method',['get_workspace','respond_and_seal','reconcile','get_relation'])
def test_T09_workspace_ids(env,wid,method):
    e=env;e.c.create_workspace(e.b,'',['abc'])
    args={'get_workspace':[wid],'respond_and_seal':[wid,['abc']],'reconcile':[wid],'get_relation':[wid,0,0]}[method]
    error(e,'WORKSPACE_NOT_FOUND',lambda:getattr(e.c,method)(*args))

def test_T10_relation_row_major_and_derived_sets(env):
    e=env;wid=ready(e,['A first','A second'],['B first','B second','B third'])
    error(e,'NOT_RECONCILED',lambda:e.c.get_relation(wid,0,0))
    matrix=[['EQUIVALENT','CONFLICT','UNRELATED'],['COMPATIBLE','UNRELATED','CONFLICT']]
    assert consensus(e,wid,raw(matrix),[raw(matrix)]*3)==([True]*3,True)
    w=e.c.get_workspace(wid);assert w['relation_matrix']==[1,3,0,2,0,3]
    for i in range(2):
        for j in range(3):assert e.c.get_relation(wid,i,j)==[1,3,0,2,0,3][i*3+j]
    assert e.m._reduce_matrix(w['relation_matrix'],2,3)=={'agreement_core':[[0,0],[1,0]],'conflict_set':[[0,1],[1,2]],'unrelated':[[0,2],[1,1]]}
    for i,j in [(-1,0),(0,-1),(2,0),(0,3),(True,0),(0,False)]:error(e,'INVALID_RELATION_INDEX',lambda:e.c.get_relation(wid,i,j))
    before=e.vm._storage.snapshot()
    e.c.get_workspace(wid);e.c.get_workspace_summaries(e.a);e.c.get_relation(wid,0,0)
    assert e.vm._storage.snapshot()==before
    invariant(e)

def test_C09_maximum_4x4(env):
    e=env;wid=ready(e,[f'A clause {i}' for i in range(4)],[f'B clause {i}' for i in range(4)])
    labels=['UNRELATED','EQUIVALENT','COMPATIBLE','CONFLICT'];matrix=[labels[i:]+labels[:i] for i in range(4)]
    assert consensus(e,wid,raw(matrix),[raw(matrix)]*4)[1]
    assert len(e.prompts)==5 and len(set(e.prompts))==1
    stored=e.c.get_workspace(wid)['relation_matrix'];assert stored==[0,1,2,3,1,2,3,0,2,3,0,1,3,0,1,2]
    assert [e.c.get_relation(wid,i,j) for i in range(4) for j in range(4)]==stored
    reduced=e.m._reduce_matrix(stored,4,4);assert [len(reduced[k]) for k in ['agreement_core','conflict_set','unrelated']]==[8,4,4]
    invariant(e)

def test_history_view_ascending_after_reverse_party_b_sealing_without_state_mutation(env):
    e = env
    assert e.c.create_workspace(e.b, 'First', ['CSV export is required.']) == 1
    assert e.c.create_workspace(e.b, 'Second', ['CSV export is required.']) == 2
    assert e.c.get_workspace_summaries(e.b) == []
    e.vm.sender = e.b
    e.c.respond_and_seal(2, ['CSV export is required.'])
    assert [w['id'] for w in e.c.get_workspace_summaries(e.b)] == [2]
    e.c.respond_and_seal(1, ['CSV export is required.'])
    # The frozen persistent index and B's post-response-only indexing are unchanged.
    assert [int(wid) for wid in e.c.workspace_ids_by_party[e.b]] == [2, 1]
    before = e.vm._storage.snapshot()
    assert [w['id'] for w in e.c.get_workspace_summaries(e.a)] == [1, 2]
    assert [w['id'] for w in e.c.get_workspace_summaries(e.b)] == [1, 2]
    assert e.vm._storage.snapshot() == before
    invariant(e)
