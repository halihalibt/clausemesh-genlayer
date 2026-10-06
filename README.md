# ClauseMesh — Bilateral Semantic Set Reconciliation

**Reusable Intelligent Contract primitive · CLAUSEMESH-V1 · GenLayer**

ClauseMesh turns two independently sealed natural-language requirement sets into persistent, queryable semantic relations. It provides immutable bilateral inputs, one contract-defined nondeterministic boundary, independently executing Validators and a deterministic Material Family Equivalence Principle. Applications can read exact accepted relations without running another AI call.

Canonical Development / Validation / Submission Network: Stable GenLayer Studionet. Chain ID: 61999. Contract: `0x0Dcb5F452412aB73b32149ad1e082533D929Ed73`. Final authoritative evidence is the accepted Phase 5 Studionet evidence.

## Why this primitive exists

Two parties may describe the same requirement differently, impose incompatible constraints or discuss unrelated dimensions. A conventional AI report is advice controlled by one provider/server. ClauseMesh instead freezes each party's own input, independently checks a complete relation matrix under shared rules and makes only an accepted Leader result reusable persistent state. It does not judge fairness, legality, factual truth or which party should win; it creates no merged agreement.

Replacing GenLayer with one OpenAI API call and a database removes independent validation under the contract-defined equivalence rule, consensus-controlled commit/discard and the shared durable state that neither application's operator nor one model alone controls. GenLayer is the trust primitive rather than an incidental API used to generate text.

## Persistent state and lifecycle

Root fields: `protocol_version: str`, `workspace_count: u64`, `workspaces: DynArray[Workspace]`, `workspace_ids_by_party: TreeMap[Address, DynArray[u64]]`.

Each Workspace stores a 1-based ID, label, A/B addresses, typed persistent A/B clause arrays, `party_b_submitted`, `reconciled` and flattened `DynArray[u8]` relation matrix. Status and derived sets are computed, not additional persistent fields. A seals at creation; only named B may submit once. After successful reconciliation neither inputs nor results can be replaced.

`WAITING_FOR_B → READY → RECONCILED`. Reconciliation is permissionless once READY. Rejected/failed/undetermined consensus does not commit speculative Workspace writes. Contract history returns summaries by numeric ID ascending even if B responds in another order. B enters its history only after responding; physical append indexing is unchanged.

Bounds: 1–4 clauses per party, 3–240 characters after edge trimming, label 0–80 characters. Zero/self counterparty is invalid. Exact/semantic duplicate clauses are allowed; a repeated valid create intentionally makes a new Workspace, so callers must never automatically resubmit after a transaction ID exists.

## One meaningful nondeterministic boundary

Only `reconcile` invokes `gl.vm.run_nondet_unsafe(leader_fn, validator_fn)`.

1. Snapshot sealed clauses in original A/B order and build the frozen Canonical Classification Prompt once.
2. Leader independently runs one full A×B matrix classification and strictly parses its JSON.
3. Each Validator independently runs the identical prompt and clause input/order as one full-matrix task. It is not a format-only checker or a vote on an explanation.
4. Deterministic code maps every Leader/Validator cell to its Material Family and compares cell by cell.
5. GenLayer owns consensus acceptance/finalization. Accepted raw Leader output is parsed again and its exact relation codes are persisted; no reasoning, confidence or summary is stored.

The frozen prompt's definitions, ambiguity rule and untrusted-clause rule instruct each role to treat submitted clauses as data. Local injection tests verify prompt boundaries and validation, not universal remote-model injection resistance. Its verbatim template is [verification/canonical_prompt.txt](verification/canonical_prompt.txt); the frozen prompt and parser behavior are covered by the test suite. Only dimensions and actual ordered clauses are filled. Maximum matrix: 4×4, one full-matrix LLM request per role, no Web facts or second AI stage.

| Relation | Stored code | Material Family |
|---|---:|---|
| UNRELATED | 0 | NONE |
| EQUIVALENT | 1 | AGREEMENT |
| COMPATIBLE | 2 | AGREEMENT |
| CONFLICT | 3 | CONFLICT |

EQUIVALENT↔COMPATIBLE is intentionally tolerated because both have the same agreement effect. AGREEMENT↔CONFLICT, NONE↔AGREEMENT and CONFLICT↔NONE must disagree. This is not exact label/string equality: `strict_eq` would reject permitted agreement-family variance. `prompt_comparative` / `prompt_non_comparative` would delegate or substitute the frozen deterministic cell-family rule. None of those convenience wrappers is used. Malformed role output never approves a candidate.

The accepted **Leader's exact code**, including Equivalent versus Compatible, is stored; the result is not collapsed to family codes, averaged or regenerated. Agreement Core selects codes 1/2; Conflict Set selects code 3; Unrelated pairs select code 0. All are deterministic row-major reductions of persisted state.

## Public interface and reuse

Exactly three writes and three views, no auxiliary public methods:

| Method | Arguments | Return / rule |
|---|---|---|
| `create_workspace` | counterparty Address, label str, clauses_a list[str] | int ID; sender is A and seals A |
| `respond_and_seal` | workspace_id int, clauses_b list[str] | None; only B, once |
| `reconcile` | workspace_id int | None; any sender, only READY, once successfully |
| `get_workspace` | workspace_id int | dict snapshot including derived status and exact matrix |
| `get_workspace_summaries` | address Address | summaries ascending by numeric ID, one aggregate read |
| `get_relation` | workspace_id int, a_index int, b_index int | exact integer code; zero-based indexes, requires reconciled |

Other builders can query `get_relation(id,a,b)` as a reusable clause-pair decision, or fetch a finalized whole Workspace and derive their own deterministic view. Example uses include delivery-requirement reconciliation, supplier/buyer specification comparisons and policy compatibility maps. These are reuse examples, not new implemented features or payment/legal adjudication.

See [docs/USAGE.md](docs/USAGE.md) for all six calls and stable errors, [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for storage/invariants and [docs/CONSENSUS.md](docs/CONSENSUS.md) for the custom validation rule.

## Deployment and reproducible tests

Use Python **3.12.14**, the exact [requirements.lock.txt](requirements.lock.txt) and content-addressed SDK pins in [toolchain.lock.json](toolchain.lock.json). Tested: GenVM **v0.2.16**, genlayer-test **0.29.2**, genlayer-py **0.16.3**, pytest **9.1.1**, genvm-linter **0.11.0**, cloudpickle **3.1.2**. Compatible client pin is retained because genlayer-test requires genlayer-py `<0.17`; no dependency override was introduced.

```bash
python -m venv .venv
# Activate this environment using your platform's standard command.
python -m pip install -r requirements.lock.txt
python verification/phase6_load.py
python -m pytest
```

The local suite has **139 PASS / 0 FAIL / 0 skipped**. It exercises real pinned SDK storage but uses explicitly mocked LLM outputs and an SDK snapshot/revert consensus rollback model. It does not misrepresent direct-mode callbacks as chain consensus. Fresh Phase 6 results are under `evidence/phase6-*`.

Canonical Development / Validation / Submission Network: Stable GenLayer Studionet. Chain ID: 61999. Contract: `0x0Dcb5F452412aB73b32149ad1e082533D929Ed73`. Final authoritative evidence is the accepted Phase 5 Studionet evidence.

## Canonical source and real proof

Canonical source: this repository's `contracts/clause_mesh.py`.

SHA-256: `5489c4c66471af9c5bfc5607d8f4640e22ebac0cfca36ce63ee762c038444830`. Source bytes are frozen at the Phase 5 verified version. Its only prior approved repair was deterministic ascending summaries in the view; no Phase 6 Contract edit occurred. Repository B carries a byte-equivalent copy of this canonical source.

Canonical Development / Validation / Submission Network: Stable GenLayer Studionet. Chain ID: 61999. Contract: `0x0Dcb5F452412aB73b32149ad1e082533D929Ed73`. Final authoritative evidence is the accepted Phase 5 Studionet evidence.

Studionet deployment tx `0xbb4e6c59c6b997eb81e8123178c4e437f6316c9c134241a796b1a838ebb16eeb`. One real final-source multi-Validator reconciliation tx `0x73468ab79503a1151eddd3ec0c31af5c4836b5eb4b902325dbdbb71d97a53d0c` reached **FINALIZED / MAJORITY_AGREE / SUCCESS**, five initial validators with **3 agree / 2 idle**, persisted matrix `[3,0,0,1]`. Accepted Leader output and independent Validator execution statistics are in [evidence/phase5-network/](evidence/phase5-network/). Exact-match evidence checks pass; no repeated consensus was used to obtain a preferred matrix.

The reverse-response real ordering case confirms Contract A/B history `[1,2]` after B seals #2 then #1. Only the canonical Studionet deployment and accepted final-source evidence are included in this public submission repository. See [docs/EVIDENCE-INDEX.md](docs/EVIDENCE-INDEX.md), [examples/sample_cases.md](examples/sample_cases.md) and [docs/SUBMISSION-INTELLIGENT-CONTRACTS.md](docs/SUBMISSION-INTELLIGENT-CONTRACTS.md).

License: MIT. All submitted clauses become public onchain data. Do not submit private, confidential or sensitive information.


Phase 6 COMPLETE. READY FOR INTELLIGENT CONTRACTS SUBMISSION. Public repository: https://github.com/halihalibt/clausemesh-genlayer. GenLayer form submission remains pending.
