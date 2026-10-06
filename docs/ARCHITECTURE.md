# ClauseMesh storage and deterministic boundaries

ClauseMesh is one Intelligent Contract, not an application server. Protocol CLAUSEMESH-V1 and source `contracts/clause_mesh.py` are canonical in this repository. Source SHA-256: `5489c4c66471af9c5bfc5607d8f4640e22ebac0cfca36ce63ee762c038444830`.

## Schema

| Root field | Storage type | Purpose |
|---|---|---|
| protocol_version | str | CLAUSEMESH-V1 |
| workspace_count | u64 | 1-based creation counter |
| workspaces | DynArray[Workspace] | storage-backed records |
| workspace_ids_by_party | TreeMap[Address,DynArray[u64]] | append indexes for participant history |

Workspace fields: `id:u64`, `label:str`, `party_a:Address`, `party_b:Address`, `clauses_a:DynArray[str]`, `clauses_b:DynArray[str]`, `party_b_submitted:bool`, `reconciled:bool`, `relation_matrix:DynArray[u8]`. SDK storage allocation uses annotated containers and an allow-storage dataclass; no ordinary persistent dict/list replaces them.

## Invariants

- `workspace_count == len(workspaces)`; ID n maps to record n−1.
- A clauses are sealed at creation. Only designated B can append its validated response, once; A/B addresses differ.
- Before B response: B clauses `[]`, `party_b_submitted=false`, `reconciled=false`, matrix `[]`, WAITING_FOR_B.
- After B seal: B has 1–4 clauses, READY, unreconciled empty matrix.
- Final accepted reconciliation: matrix length A_count×B_count, valid codes 0–3, flags true, RECONCILED.
- Rejected/failed consensus discards speculative changes; original READY snapshot stays unchanged.
- Successful reconciliation cannot run again, so exact accepted codes persist without revision.
- A is indexed on create, B only on response. Index writes retain append order; the summaries view deterministically sorts by numeric ID without mutating storage.

Labels and clauses are edge-trimmed only; case, punctuation, internal whitespace, Unicode and duplicate content are preserved. Label ≤80 characters; each set 1–4 clauses; each trimmed clause 3–240 characters. Invalid input raises a stable UserError before mutation.

## Determinism and consensus

Create, response, input validation, status derivation, parser, history return sorting, relation lookups and pair reduction are deterministic. Only reconcile calls the custom nondeterministic boundary described in CONSENSUS.md. Role callbacks capture plain prompt/dimensions, never storage or self. The prompt excludes labels/addresses from classification and preserves exact clause order.

Relation index = a_index×B_count+b_index. A rows/B columns, zero-based programmatic indexes, human labels A1/B1. `get_relation` refuses unreconciled state and out-of-range indexes. Pair sets are derived in memory, not new fields or public methods.

## Trust and evidence

One model/server cannot commit arbitrary shared semantic state: independent participants seal inputs and multiple GenLayer roles execute the frozen task, with acceptance governed by the contract's deterministic equivalence rule. The application/UI only reads and displays finalized codes; it does not rewrite them.

Canonical Development / Validation / Submission Network: Stable GenLayer Studionet. Chain ID: 61999. Contract: `0x0Dcb5F452412aB73b32149ad1e082533D929Ed73`. Final authoritative evidence is the accepted Phase 5 Studionet evidence.