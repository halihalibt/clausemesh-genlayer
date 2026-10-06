# Intelligent Contracts submission material

**READY FOR INTELLIGENT CONTRACTS SUBMISSION.** Not submitted. Owner supplies real repository/demo URLs after separately authorized publication.

Canonical Development / Validation / Submission Network: Stable GenLayer Studionet. Chain ID: 61999. Contract: `0x0Dcb5F452412aB73b32149ad1e082533D929Ed73`. Final authoritative evidence is the accepted Phase 5 Studionet evidence.

## Title
ClauseMesh — Bilateral Semantic Set Reconciliation

## One-line summary
A persistent Intelligent Contract primitive that freezes two clause sets and reconciles their pairwise semantics through independent GenLayer Validators and deterministic Material Family agreement.

## Detailed description / problem
Two parties often describe overlapping requirements using different language. A normal database can freeze their text, but cannot establish shared semantic results without trusting one operator's model and storage. ClauseMesh makes immutable bilateral input and independently validated classification part of shared Contract state. It returns an exact row-major relation matrix that other builders can query instead of generating a rewritten agreement.

## Primitive
Party A creates and seals 1–4 clauses for a named Party B. Only B may respond and seal 1–4 clauses. Any signer may reconcile a READY Workspace once. Three views expose state, aggregate history and an indexed relation. No payment, editing, negotiation, score or generated agreement is added. This is reusable bilateral semantic set reconciliation rather than a single application-owned LLM response.

## Why GenLayer
The nondeterministic full-matrix task is executed and independently checked inside GenLayer's consensus lifecycle. Finalized state and the accepted outcome are persisted by the Contract. Replacing this with one external AI API plus a database would replace independent validation and replicated Contract permissions/commitment with trust in a centralized provider/operator. GenLayer is the trust boundary for the semantic state transition, not an optional text generation service.

## Consensus mechanism / Validator responsibility
reconcile is the sole nondeterministic boundary. The Leader classifies the entire A×B matrix once. Each Validator independently executes the identical frozen Canonical Classification Prompt, identical sealed clause arrays and identical order. Both outputs must parse into exact canonical labels and dimensions. Each cell is compared deterministically by Material Family; malformed outputs or any material disagreement reject the candidate. The custom run_nondet_unsafe callbacks are retained, not replaced with convenience equivalence wrappers.

## Equivalence Principle
Equivalent and Compatible map to AGREEMENT; Conflict maps to CONFLICT; Unrelated maps to NONE. Equivalent↔Compatible variation is tolerated, while Agreement↔Conflict, None↔Agreement and Conflict↔None disagree. Raw strict equality would reject allowed agreement-family variation; prompt_comparative / prompt_non_comparative would replace the frozen deterministic principle with another nondeterministic task. After acceptance, the exact Leader relation codes—not the Validator's or a synthesized compromise—are persisted.

## State design
Four persistent Contract fields contain the protocol version, monotonic count, Workspace array and party index. Each Workspace stores id/label/parties, immutable clause arrays, B submission/reconciled flags and the flat relation matrix. Status is derived. History is ascending ID; B enters only after responding. Failed consensus does not commit a matrix. A successful Workspace cannot reconcile again. Agreement Core and Conflict Set are deterministic derivations, not extra AI outputs or persistent fields.

## Reusable use cases
Integrate get_relation into requirement compatibility checks, buyer/supplier requirement comparisons, or immutable bilateral scope reviews. Builders can consume the four exact codes and deterministic sets without using Handshake Map. Example payment terms are data, never token transfers or adjudication.

Canonical Development / Validation / Submission Network: Stable GenLayer Studionet, Chain ID 61999, Contract `0x0Dcb5F452412aB73b32149ad1e082533D929Ed73`. Phase 5 finalized consensus and persistent state are authoritative. See docs/EVIDENCE-INDEX.md.



## Repository
Repository name: `clausemesh-genlayer`. Add the actual public GitHub repository URL to the GenLayer submission form after publication; do not invent a URL before it exists.



