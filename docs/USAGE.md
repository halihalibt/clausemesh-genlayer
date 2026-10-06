# Deploy, call and reuse ClauseMesh

Canonical Development / Validation / Submission Network: Stable GenLayer Studionet. Chain ID: 61999. Contract: `0x0Dcb5F452412aB73b32149ad1e082533D929Ed73`. Final authoritative evidence is the accepted Phase 5 Studionet evidence.

## Set up and test independently

Python 3.12.14, `python -m venv .venv`, activate using your platform's command, `python -m pip install -r requirements.lock.txt`, then `python -m pytest`. GenVM bundle/runner hashes are pinned in toolchain.lock.json; first load may download the official cached bundle. The authoritative `specifications/PROJECT_BLUEPRINT_V1.md` is repo-local because the consensus tests verify the frozen canonical prompt against it. `python verification/phase6_load.py` checks source/prompt/linter/schema/storage. Local direct-mode consensus is mocked; see separate real receipts.

## Pinned client call shapes

These are illustrative SDK calls, not an auto-executing transaction script. Obtain account_a/account_b only through an authorized signing workflow; do not paste a private key into code, shell, chat, logs or a package. Use faucet/test assets. Explicitly approve new network source submission/deployment before using it.

```python
from pathlib import Path
from genlayer_py import create_client
from genlayer_py.chains import studionet
from genlayer_py.types import CalldataAddress, TransactionHashVariant

read_client = create_client(chain=studionet)
contract = "0x0Dcb5F452412aB73b32149ad1e082533D929Ed73"
# Only if deploying a separate authorized instance:
# deploy_client = create_client(chain=studionet, account=authorized_account)
# deploy_id = deploy_client.deploy_contract(
#     code=Path("contracts/clause_mesh.py").read_bytes(),
#     args=[], leader_only=False,
# )
```

Write exactly once, retain each original returned ID immediately and wait/query the same ID to finalized success before dependent writes. Creation receipt returns the exact Workspace ID; never guess an ID from an unfinished transaction or resend a create after a wait failure.

```python
# ca/cb are clients for independently authorized Party A/B signers.
create_id = ca.write_contract(contract, "create_workspace", args=[
    CalldataAddress(party_b_address), "Compact example",
    ["Reports must be exported as CSV.", "Invoices must be paid monthly."],
], leader_only=False)
# Query/finalize original create_id; decode its exact returned workspace_id.
respond_id = cb.write_contract(contract, "respond_and_seal", args=[
    workspace_id,
    ["Reports must never be exported as CSV.", "Invoices must be paid monthly."],
], leader_only=False)
# Query/finalize original respond_id and verify READY.
reconcile_id = ca.write_contract(contract, "reconcile",
    args=[workspace_id], leader_only=False)
# Any signer may reconcile once READY; do not repeat for nicer labels.
```

No implicit retries surround write submission. After an ID exists, bounded official lifecycle queries may resume it; one active waiter, one sequential query retry at most after a transient failure, respect Retry-After. No infinite/recursive retry or automatic write resubmission.

```python
w = read_client.read_contract(contract, "get_workspace", args=[workspace_id],
    transaction_hash_variant=TransactionHashVariant.LATEST_FINAL)
history = read_client.read_contract(contract, "get_workspace_summaries",
    args=[CalldataAddress(party_b_address)],
    transaction_hash_variant=TransactionHashVariant.LATEST_FINAL)
relation = read_client.read_contract(contract, "get_relation",
    args=[workspace_id, 0, 0],
    transaction_hash_variant=TransactionHashVariant.LATEST_FINAL)
```

`get_workspace` returns id, label, A/B addresses, clauses_a/clauses_b, flags, exact row-major relation_matrix and derived_status. Histories are numeric ID ascending, B only after responding. Display newest-first by reversing a local copy. `get_relation` takes zero-based A/B indexes and requires a reconciled Workspace; exact codes 0/1/2/3 mean Unrelated/Equivalent/Compatible/Conflict. Agreement/Conflict derivation is deterministic from those codes, no AI summary.

## Stable Contract errors

`INVALID_COUNTERPARTY`, `INVALID_LABEL`, `INVALID_CLAUSE_COUNT`, `INVALID_CLAUSE`, `UNAUTHORIZED`, `ALREADY_SEALED`, `NOT_READY`, `ALREADY_RECONCILED`, `WORKSPACE_NOT_FOUND`, `NOT_RECONCILED`, `INVALID_RELATION_INDEX`, `INVALID_CONSENSUS_OUTPUT`.

Treat error text as a stable semantic identifier; never display raw traces/server configuration. Failed consensus leaves the sealed READY Workspace unchanged. A second successful reconcile is rejected. Repeated create is intentionally legal; tx-ID safety belongs at caller submission boundaries.

Canonical Development / Validation / Submission Network: Stable GenLayer Studionet. Chain ID: 61999. Contract: `0x0Dcb5F452412aB73b32149ad1e082533D929Ed73`. Final authoritative evidence is the accepted Phase 5 Studionet evidence.