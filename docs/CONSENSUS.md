# Custom Leader/Validator consensus

## Frozen task

One `reconcile(workspace_id)` snapshots both immutable clause arrays and builds the Canonical Classification Prompt in `verification/canonical_prompt.txt`. Same frozen definitions, ambiguity and untrusted-input rules; identical dimensions, clause content and input order for Leader and Validator. The label is not classification context. The task classifies every A×B pair as UNRELATED, EQUIVALENT, COMPATIBLE or CONFLICT; it does not fact-check, browse, decide legality or generate an agreement.

## Actual stable mechanism

`gl.vm.run_nondet_unsafe(leader_fn, validator_fn)` is the sole nondeterministic boundary. Leader calls `gl.nondet.exec_prompt(prompt)` once for the entire matrix and strictly parses it. Each Validator parses the wrapped Leader return, independently reruns that same complete classification through `leader_fn()`, parses its own output and returns the deterministic cell-family comparison.

The Validator is not format-only and does not ask a model whether it likes the Leader answer. Invalid Leader wrapping, malformed JSON, invalid enum/dimensions or independent model/parsing failure returns disagreement rather than approval. Chain consensus owns accept/finalize or speculative storage discard.

## Equivalence Principle

| Stored relation | Code | Family |
|---|---:|---|
| UNRELATED | 0 | NONE |
| EQUIVALENT | 1 | AGREEMENT |
| COMPATIBLE | 2 | AGREEMENT |
| CONFLICT | 3 | CONFLICT |

For every cell, family(Leader[i]) must equal family(Validator[i]); any material mismatch is disagreement. EQUIVALENT versus COMPATIBLE may differ because both are AGREEMENT. AGREEMENT versus CONFLICT, NONE versus AGREEMENT and CONFLICT versus NONE cannot be tolerated. Comparison is deterministic code, not a second probabilistic judgment.

`strict_eq` would incorrectly require exact labels and reject permitted agreement-family variance. `prompt_comparative` or `prompt_non_comparative` would replace the frozen independent full-task plus deterministic family comparison with convenience semantics. None is used; no wrapper, majority simplification or consensus-family collapse substitutes the rule.

## Parsing and persistence

Output is text containing exactly one JSON object with sole key `matrix`, a list of the exact dimensions, canonical relation strings only. Code fences, extra fields, malformed/duplicate JSON keys or invalid shape are not repaired into valid output. A maximum 4×4 matrix yields at most 16 row-major codes.

After the boundary accepts, the original accepted Leader raw output is parsed again and exact codes appended once to `relation_matrix`; `reconciled=true`. Compatible remains code 2 even if a Validator chose Equivalent (1). No Validator replacement, regenerated result, reasoning or confidence is persisted.

Agreement Core = all row-major indexes whose code is 1 or 2; Conflict Set = code 3; Unrelated = code 0. These reductions do not invoke AI.

## Verification

Current tests exercise all 16 relation-family pairs, material mismatch per cell, malformed Leader/Validator output, prompt injection, identical frozen input/order, 4×4, wrapped returns, one custom boundary and absence of convenience wrappers. Direct-mode tests use real SDK storage with mocked outputs and explicit snapshot/revert; that is not real network consensus.

Real Studionet source proof: reconcile `0x73468ab79503a1151eddd3ec0c31af5c4836b5eb4b902325dbdbb71d97a53d0c`, FINALIZED / MAJORITY_AGREE / SUCCESS, five initial validators, 3 agree / 2 idle, independent successful Validator LLM statistics. Accepted Leader matrix `[[CONFLICT,UNRELATED],[UNRELATED,EQUIVALENT]]` is persisted as `[3,0,0,1]`. `evidence/phase5-network/real-browser-evidence.json` and `evidence-check-results.json` distinguish actual observations from offline consistency assertions.

Canonical Development / Validation / Submission Network: Stable GenLayer Studionet. Chain ID: 61999. Contract: `0x0Dcb5F452412aB73b32149ad1e082533D929Ed73`. Final authoritative evidence is the accepted Phase 5 Studionet evidence.