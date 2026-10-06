# Fresh Phase 6 complete test inventory

Contract: 139 PASS / 0 FAIL / 0 skipped. Local pinned SDK and mocked consensus; real consensus is separate evidence.

| Result | Test |
|---|---|
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[UNRELATED-UNRELATED]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[UNRELATED-EQUIVALENT]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[UNRELATED-COMPATIBLE]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[UNRELATED-CONFLICT]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[EQUIVALENT-UNRELATED]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[EQUIVALENT-EQUIVALENT]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[EQUIVALENT-COMPATIBLE]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[EQUIVALENT-CONFLICT]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[COMPATIBLE-UNRELATED]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[COMPATIBLE-EQUIVALENT]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[COMPATIBLE-COMPATIBLE]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[COMPATIBLE-CONFLICT]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[CONFLICT-UNRELATED]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[CONFLICT-EQUIVALENT]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[CONFLICT-COMPATIBLE]` |
| PASSED | `tests/test_consensus.py::test_C01_C05_all_material_family_pairs[CONFLICT-CONFLICT]` |
| PASSED | `tests/test_consensus.py::test_each_cell_material_disagreement[0]` |
| PASSED | `tests/test_consensus.py::test_each_cell_material_disagreement[1]` |
| PASSED | `tests/test_consensus.py::test_each_cell_material_disagreement[2]` |
| PASSED | `tests/test_consensus.py::test_each_cell_material_disagreement[3]` |
| PASSED | `tests/test_consensus.py::test_C11_custom_boundary_schema_and_frozen_prompt` |
| PASSED | `tests/test_consensus.py::test_C08_C12_identical_full_prompt_order_and_input_injection` |
| PASSED | `tests/test_consensus.py::test_family_helper_rejects_noncanonical_codes[leader0-validator0]` |
| PASSED | `tests/test_consensus.py::test_family_helper_rejects_noncanonical_codes[leader1-validator1]` |
| PASSED | `tests/test_consensus.py::test_family_helper_rejects_noncanonical_codes[leader2-validator2]` |
| PASSED | `tests/test_consensus.py::test_family_helper_rejects_noncanonical_codes[leader3-validator3]` |
| PASSED | `tests/test_consensus.py::test_family_helper_rejects_noncanonical_codes[leader4-validator4]` |
| PASSED | `tests/test_consensus.py::test_family_helper_rejects_noncanonical_codes[leader5-validator5]` |
| PASSED | `tests/test_consensus.py::test_pinned_RPC_Address_wire_encoding_matches_contract_SDK` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[not JSON]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[```json\n{"matrix":[["EQUIVALENT"]]}\n```]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[[],[]]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[["EQUIVALENT","UNRELATED"]]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[["EQUIVALENT"],["EQUIVALENT"]]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[["AGREEMENT"]]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[["equivalent"]]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[[1]]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[[null]]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[[true]]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[[{}]]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":["EQUIVALENT"]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":null}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[["EQUIVALENT"]],"reason":"ok"}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[["EQUIVALENT"]],"matrix":[["CONFLICT"]]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[[]]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[null]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[[NaN]]}]` |
| PASSED | `tests/test_failures.py::test_C06_malformed_leader_no_state_mutation[{"matrix":[["EQUIVALENT"]]} trailing prose]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[not JSON]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[```json\n{"matrix":[["EQUIVALENT"]]}\n```]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[[],[]]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[["EQUIVALENT","UNRELATED"]]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[["EQUIVALENT"],["EQUIVALENT"]]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[["AGREEMENT"]]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[["equivalent"]]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[[1]]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[[null]]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[[true]]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[[{}]]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":["EQUIVALENT"]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":null}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[["EQUIVALENT"]],"reason":"ok"}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[["EQUIVALENT"]],"matrix":[["CONFLICT"]]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[[]]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[null]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[[NaN]]}]` |
| PASSED | `tests/test_failures.py::test_C07_malformed_validator_never_approves[{"matrix":[["EQUIVALENT"]]} trailing prose]` |
| PASSED | `tests/test_failures.py::test_failure_lifecycle_returns_READY[leader_failure]` |
| PASSED | `tests/test_failures.py::test_failure_lifecycle_returns_READY[leader_timeout]` |
| PASSED | `tests/test_failures.py::test_failure_lifecycle_returns_READY[validator_failure]` |
| PASSED | `tests/test_failures.py::test_failure_lifecycle_returns_READY[validator_timeout]` |
| PASSED | `tests/test_failures.py::test_failure_lifecycle_returns_READY[FAILED]` |
| PASSED | `tests/test_failures.py::test_failure_lifecycle_returns_READY[REJECTED]` |
| PASSED | `tests/test_failures.py::test_failure_lifecycle_returns_READY[UNDETERMINED]` |
| PASSED | `tests/test_failures.py::test_invalid_wrapped_leader_never_runs_validator_AI` |
| PASSED | `tests/test_failures.py::test_parser_rejects_non_text[None]` |
| PASSED | `tests/test_failures.py::test_parser_rejects_non_text[value1]` |
| PASSED | `tests/test_failures.py::test_parser_rejects_non_text[value2]` |
| PASSED | `tests/test_failures.py::test_parser_rejects_non_text[1]` |
| PASSED | `tests/test_failures.py::test_parser_rejects_non_text[True]` |
| PASSED | `tests/test_failures.py::test_manual_reconcile_after_definite_mock_disagreement` |
| PASSED | `tests/test_failures.py::test_final_accepted_boundary_output_reparsed` |
| PASSED | `tests/test_failures.py::test_server_error_evidence_never_retains_sensitive_configuration[ALREADY_RECONCILED]` |
| PASSED | `tests/test_failures.py::test_server_error_evidence_never_retains_sensitive_configuration[INVALID_CONSENSUS_OUTPUT]` |
| PASSED | `tests/test_failures.py::test_server_error_evidence_never_retains_sensitive_configuration[None]` |
| PASSED | `tests/test_permissions.py::test_T02_counterparty[zero]` |
| PASSED | `tests/test_permissions.py::test_T02_counterparty[self]` |
| PASSED | `tests/test_permissions.py::test_T05_only_B_can_respond[a]` |
| PASSED | `tests/test_permissions.py::test_T05_only_B_can_respond[t]` |
| PASSED | `tests/test_permissions.py::test_T06_double_seal` |
| PASSED | `tests/test_permissions.py::test_T07_not_ready_no_AI` |
| PASSED | `tests/test_permissions.py::test_permissionless_and_T08_success_immutable[a]` |
| PASSED | `tests/test_permissions.py::test_permissionless_and_T08_success_immutable[b]` |
| PASSED | `tests/test_permissions.py::test_permissionless_and_T08_success_immutable[t]` |
| PASSED | `tests/test_state.py::test_T01_creation_and_T04_response` |
| PASSED | `tests/test_state.py::test_T03_inclusive_bounds[abc-]` |
| PASSED | `tests/test_state.py::test_T03_inclusive_bounds[abc-   ]` |
| PASSED | `tests/test_state.py::test_T03_inclusive_bounds[abc-\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57]` |
| PASSED | `tests/test_state.py::test_T03_inclusive_bounds[\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57-]` |
| PASSED | `tests/test_state.py::test_T03_inclusive_bounds[\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57-   ]` |
| PASSED | `tests/test_state.py::test_T03_inclusive_bounds[\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57-\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57\u5b57]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses0-INVALID_CLAUSE_COUNT-a]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses0-INVALID_CLAUSE_COUNT-b]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses1-INVALID_CLAUSE_COUNT-a]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses1-INVALID_CLAUSE_COUNT-b]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses2-INVALID_CLAUSE-a]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses2-INVALID_CLAUSE-b]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses3-INVALID_CLAUSE-a]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses3-INVALID_CLAUSE-b]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses4-INVALID_CLAUSE-a]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses4-INVALID_CLAUSE-b]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses5-INVALID_CLAUSE-a]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses5-INVALID_CLAUSE-b]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses6-INVALID_CLAUSE-a]` |
| PASSED | `tests/test_state.py::test_T03_invalid_clauses_no_partial_write[clauses6-INVALID_CLAUSE-b]` |
| PASSED | `tests/test_state.py::test_T03_invalid_label[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]` |
| PASSED | `tests/test_state.py::test_T03_invalid_label[None]` |
| PASSED | `tests/test_state.py::test_duplicate_creation_and_history_order` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[get_workspace-0]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[get_workspace--1]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[get_workspace-2]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[get_workspace-True]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[respond_and_seal-0]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[respond_and_seal--1]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[respond_and_seal-2]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[respond_and_seal-True]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[reconcile-0]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[reconcile--1]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[reconcile-2]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[reconcile-True]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[get_relation-0]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[get_relation--1]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[get_relation-2]` |
| PASSED | `tests/test_state.py::test_T09_workspace_ids[get_relation-True]` |
| PASSED | `tests/test_state.py::test_T10_relation_row_major_and_derived_sets` |
| PASSED | `tests/test_state.py::test_C09_maximum_4x4` |
| PASSED | `tests/test_state.py::test_history_view_ascending_after_reverse_party_b_sealing_without_state_mutation` |

Frontend: 113 PASS / 0 FAIL / 0 skipped / 0 todo. Local test-only fakes.

| Result | Test |
|---|---|
| PASSED | `offline real SDK adapter: no network requests SDK aggregate finalized read decodes byte addresses, bigint IDs and exact codes` |
| PASSED | `offline real SDK adapter: no network requests SDK aggregate history encodes address type and performs one read` |
| PASSED | `offline real SDK adapter: no network requests wallet-backed SDK write preserves actual provider tx ID, no lifecycle wait/resend inside write` |
| PASSED | `offline real SDK adapter: no network requests wallet chain/account checked before any write; no auto switch prompt` |
| PASSED | `offline real SDK adapter: no network requests official SDK waiter handles stored FINALIZED receipt and exact execution return ID` |
| PASSED | `offline real SDK adapter: no network requests SDK 429 wrapper retains Retry-After through Viem, stops after one automatic read retry` |
| PASSED | `serialization and sanitized receipts Python JSON-safe addr# representation normalizes only at adapter boundary` |
| PASSED | `serialization and sanitized receipts u64 ID is exact and malformed snapshot fails read` |
| PASSED | `serialization and sanitized receipts execution rollback maps stable Contract error rather than raw stack` |
| PASSED | `serialization and sanitized receipts Retry-After accepts seconds and HTTP date` |
| PASSED | `serialization and sanitized receipts transaction projection discards server secrets/configuration` |
| PASSED | `serialization and sanitized receipts RPC user error strips raw node_config before SDK diagnostics` |
| PASSED | `serialization and sanitized receipts nested Viem causes retain sanitized code and Retry-After` |
| PASSED | `finalized create ID fallback and recovery only after finalized receipt, one summaries operation, exact A/B/trimmed label, highest matching u64 ID` |
| PASSED | `finalized create ID fallback and recovery fallback criteria survive reload; original create is not called again` |
| PASSED | `bounded real transport timeout per-request abort stops a stalled RPC; no background polling or write retry` |
| PASSED | `F03 validation mirrors frozen bounds rejects counterparty ` |
| PASSED | `F03 validation mirrors frozen bounds rejects counterparty 0x0` |
| PASSED | `F03 validation mirrors frozen bounds rejects counterparty 0x0000000000000000000000000000000000000000` |
| PASSED | `F03 validation mirrors frozen bounds rejects counterparty 0x1111111111111111111111111111111111111111` |
| PASSED | `F03 validation mirrors frozen bounds rejects counterparty 0X1111111111111111111111111111111111111111` |
| PASSED | `F03 validation mirrors frozen bounds trims edges but preserves Unicode, duplicates, internal whitespace, case and punctuation` |
| PASSED | `F03 validation mirrors frozen bounds rejects clause count []` |
| PASSED | `F03 validation mirrors frozen bounds rejects clause count [ 'abc', 'abc', 'abc', 'abc', 'abc' ]` |
| PASSED | `F03 validation mirrors frozen bounds rejects invalid clause` |
| PASSED | `F03 validation mirrors frozen bounds rejects invalid clause` |
| PASSED | `F03 validation mirrors frozen bounds rejects invalid clause` |
| PASSED | `F03 validation mirrors frozen bounds accepts empty/80-character labels and rejects 81 after trim` |
| PASSED | `F07 exact deterministic result reduction uses exact codes, row-major zero-based indexes and preserves Compatible distinct from Equivalent` |
| PASSED | `F07 exact deterministic result reduction covers maximum 4×4 without changing taxonomy` |
| PASSED | `F07 exact deterministic result reduction status derives from flags and failed consensus remains READY` |
| PASSED | `F07 exact deterministic result reduction invalid persisted matrix is read failure` |
| PASSED | `F10 friendly errors, never raw exceptions WALLET_REJECTED maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions WRONG_NETWORK maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions INVALID_COUNTERPARTY maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions INVALID_LABEL maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions INVALID_CLAUSE_COUNT maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions INVALID_CLAUSE maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions UNAUTHORIZED maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions ALREADY_SEALED maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions NOT_READY maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions ALREADY_RECONCILED maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions EXECUTION_FAILED maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions CONSENSUS_UNDETERMINED maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions STATUS_UNAVAILABLE maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions RPC_RATE_LIMITED maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions RPC_UNAVAILABLE maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions READ_FAILED maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions WORKSPACE_NOT_FOUND maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions NOT_RECONCILED maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions INVALID_RELATION_INDEX maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions INVALID_CONSENSUS_OUTPUT maps to a friendly message` |
| PASSED | `F10 friendly errors, never raw exceptions wallet 4001, HTTP 429 and unknown errors are sanitized` |
| PASSED | `F11 one bounded sequential retry per read/status operation respects Retry-After delay, at most two calls, no parallel retry` |
| PASSED | `F11 one bounded sequential retry per read/status operation one transient RPC retry may succeed` |
| PASSED | `F11 one bounded sequential retry per read/status operation nontransient read errors are not automatically retried` |
| PASSED | `frozen storage compatibility regressions frontend trimming matches Python strip, preserves BOM and strips NEL` |
| PASSED | `pinned SDK and six-method boundary stable genlayer-js Studionet metadata matches frozen chain and RPC without connecting` |
| PASSED | `pinned SDK and six-method boundary Phase 3 fake exposes exactly the frozen six methods` |
| PASSED | `F12/F13 original transaction boundary and page recovery create_workspace: timeout → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery create_workspace: RPC_UNAVAILABLE → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery create_workspace: 429 → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery create_workspace: finalization timeout → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery create_workspace: finalized read failure → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery respond_and_seal: timeout → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery respond_and_seal: RPC_UNAVAILABLE → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery respond_and_seal: 429 → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery respond_and_seal: finalization timeout → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery respond_and_seal: finalized read failure → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery reconcile: timeout → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery reconcile: RPC_UNAVAILABLE → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery reconcile: 429 → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery reconcile: finalization timeout → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery reconcile: finalized read failure → same tx after recovery, write once` |
| PASSED | `F12/F13 original transaction boundary and page recovery F13 double submit while signing cannot create duplicates` |
| PASSED | `F12/F13 original transaction boundary and page recovery F13 create with unavailable exact result never guesses latest history or resends` |
| PASSED | `F14 one active lifecycle waiter coalesces parallel Resume, including subscription reentry` |
| PASSED | `F06 lifecycle and finalized snapshot emits all submission/decision/consensus/finalization/read/success stages with tx visible` |
| PASSED | `F06 lifecycle and finalized snapshot known FAILED does not resend, mutate workspace, or read a successful result` |
| PASSED | `F06 lifecycle and finalized snapshot known REJECTED does not resend, mutate workspace, or read a successful result` |
| PASSED | `F06 lifecycle and finalized snapshot known UNDETERMINED does not resend, mutate workspace, or read a successful result` |
| PASSED | `F06 lifecycle and finalized snapshot write rejection is never retried by read retry policy` |
| PASSED | `F06 lifecycle and finalized snapshot submitted tx remains in memory if metadata storage is unavailable` |
| PASSED | `F01/F02 injected wallet and explicit network handling Connect displays correct address; disconnect clears local UI without prompting` |
| PASSED | `F01/F02 injected wallet and explicit network handling wrong network shows expected 61999, blocks writes, switches only on explicit click` |
| PASSED | `F01/F02 injected wallet and explicit network handling rejected Switch shows manual instructions without repeated prompts` |
| PASSED | `F01/F02 injected wallet and explicit network handling account and chain events update permission/network state and detach on unmount` |
| PASSED | `F03/F04/F05 Create and frozen permissions validates form then creates/seals once and navigates to receipt ID` |
| PASSED | `F03/F04/F05 Create and frozen permissions Add/Remove allow only 1–4 editable clauses` |
| PASSED | `F03/F04/F05 Create and frozen permissions wallet 0x1111111111111111111111111111111111111111 cannot edit Party B` |
| PASSED | `F03/F04/F05 Create and frozen permissions wallet 0x3333333333333333333333333333333333333333 cannot edit Party B` |
| PASSED | `F03/F04/F05 Create and frozen permissions only Party B seals, then response becomes read-only` |
| PASSED | `F06/F07 workspace consensus and exact results permissionless third wallet reconciles; active button disabled and original ID visible` |
| PASSED | `F06/F07 workspace consensus and exact results matrix cells, deterministic lists and pair counts match exact persisted row-major data` |
| PASSED | `F06/F07 workspace consensus and exact results maximum 4×4 renders all 16 exact cells` |
| PASSED | `F06/F07 workspace consensus and exact results required result empty states render` |
| PASSED | `F06/F07 workspace consensus and exact results Prompt Injection text remains inert literal text` |
| PASSED | `F08/F09 recovery and aggregate history reload recovers entire workspace from one aggregate read, no wallet or relation requests` |
| PASSED | `F08/F09 recovery and aggregate history history uses one aggregate read, reverses newest-first locally, no per-item reads` |
| PASSED | `F08/F09 recovery and aggregate history popstate restores query-mode workspace without React Router` |
| PASSED | `F08/F09 recovery and aggregate history share link includes existing static hosting path and workspace query` |
| PASSED | `F10/F11 errors and manual bounded recovery ordinary workspace read 429 retries once then manual Retry without write` |
| PASSED | `F10/F11 errors and manual bounded recovery workspace not found and unknown RPC error never expose raw stack/secret` |
| PASSED | `F10/F11 errors and manual bounded recovery malformed matrix produces friendly read failure instead of render crash` |
| PASSED | `F10/F11 errors and manual bounded recovery no-wallet and empty-history notices are exact` |
| PASSED | `F12/F13 UI recovery never resends create_workspace create tx obtained → timeout → manual Resume → same tx and one write` |
| PASSED | `F12/F13 UI recovery never resends create_workspace create tx obtained → RPC_UNAVAILABLE → manual Resume → same tx and one write` |
| PASSED | `F12/F13 UI recovery never resends create_workspace create tx obtained → 429 → manual Resume → same tx and one write` |
| PASSED | `F12/F13 UI recovery never resends create_workspace reload restores original tx metadata, Resume does not access original payload or write` |
| PASSED | `implementation defect regressions write rejected before tx submission remains visible as friendly wallet error` |
| PASSED | `implementation defect regressions revisiting workspace after successful create reads latest state instead of stale transaction snapshot` |
| PASSED | `frozen u64 workspace identifier compatibility full u64 ID in query remains exact without JS precision loss` |
| PASSED | `Phase 5 history root-cause regression Party B consumes Contract ascending IDs after reverse seal order and only locally reverses newest-first` |
