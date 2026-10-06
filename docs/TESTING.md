# Final package testing and limits

Canonical Development / Validation / Submission Network: Stable GenLayer Studionet. Chain ID: 61999. Contract: `0x0Dcb5F452412aB73b32149ad1e082533D929Ed73`. Final authoritative evidence is the accepted Phase 5 Studionet evidence.

## Contract

`python -m pytest --junitxml=evidence/phase6-contract-junit.xml` from Repository A after installing requirements.lock.txt with Python 3.12.14. Full names/results are in TEST-INVENTORY.md and phase6-local.json. Categories: state schema/invariants and deterministic helpers; permissions; input bounds/duplicates; indexes; ascending histories despite reverse B response order; malformed Leader/Validator matrices; every family comparison including Equivalent/Compatible tolerance; unchanged full prompt and clause order; injection supplied as data; maximum 4×4; failed/undetermined/rejected consensus rollback model; custom nondeterministic callback/schema and frozen prompt.

The existing accepted real Studionet receipt shows five initial Validators, three agreeing and two idle, accepted Leader matrix persisted unchanged. This is not a claim that all five independently agreed. Injection tests verify mocked control flow, prompt boundaries and parser defenses, not universal resistance of every remote language model.

## Frontend

`npm test -- --reporter=default --reporter=json --outputFile.json=docs/phase6/frontend-results.json` and `npm run build` from Repository B using the package engine versions. Full names/results are in TEST-INVENTORY.md. F01–F14 include wallet/network, create, B permission/seal, reconciliation lifecycle/result, reload, aggregate history, friendly errors, 429 bounds, original tx resume/no resend, create duplicate prevention and one active lifecycle waiter. Timeout/RPC/429/recovery cases keep the original ID and call the original write exactly once. The ascending [1,2] history fixture displays [2,1] after local reverse.

Fresh package commands reuse already installed pinned toolchain dependencies; a new network download/clean npm installation was not performed during Phase 6. package-lock.json and exact pins are retained. Use npm ci for an owner-run clean reproducible installation; npm install is also the normal developer setup.

Responsive real-production screenshots from accepted Phase 5 cover desktop 1440 and mobile 390/320. Supplemental max-4×4/wrong-network/read-error/empty-conflict viewport fixtures are synthetic and labeled. No new real frontend E2E or new reconciliation is claimed in Phase 6. Static base ./ preserves assets and ?w links under a repository prefix; Pages config is prepared only, not published.
