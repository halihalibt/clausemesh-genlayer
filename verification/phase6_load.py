"""Phase 6 frozen-source load/schema/happy-path smoke; not the Phase 2 acceptance suite.

Run with Python 3.12.14 in a venv containing requirements.lock.txt.
Uses the real pinned SDK, SDK-backed storage, and mocked LLM text.
No user source or transaction is sent to any remote RPC.
"""

import ast
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile

from gltest.direct.loader import deploy_contract
from gltest.direct.sdk_loader import setup_sdk_paths
from gltest.direct.vm import VMContext


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts/clause_mesh.py"
EVIDENCE = ROOT / "evidence/phase6-load"
SDK_VERSION = "v0.2.16"


def main():
    EVIDENCE.mkdir(exist_ok=True)
    source = CONTRACT.read_text(encoding="utf-8")
    compile(source, str(CONTRACT), "exec")
    tree = ast.parse(source)
    prompt = next(ast.literal_eval(node.value) for node in tree.body
                  if isinstance(node, ast.Assign)
                  and any(isinstance(target, ast.Name)
                          and target.id == "CANONICAL_CLASSIFICATION_PROMPT"
                          for target in node.targets))
    frozen_prompt = (ROOT / "verification/canonical_prompt.txt").read_text(encoding="utf-8")
    assert prompt == frozen_prompt, "Frozen prompt changed"
    blueprint = ROOT / "specifications/PROJECT_BLUEPRINT_V1.md"
    if blueprint.exists():
        text = blueprint.read_text(encoding="utf-8")
        section = text.split("# 15.1 CANONICAL CLASSIFICATION PROMPT TEMPLATE\n", 1)[1]
        original = section.split("Canonical template:\n\n```text\n", 1)[1].split("\n```", 1)[0]
        assert prompt == original, "Prompt differs from authoritative Blueprint"

    # Avoid the tooling's unpinned 'latest' fallback. Reuse exactly the runner
    # selected by the content hash in the source header and this release.
    sdk_paths = setup_sdk_paths(CONTRACT, SDK_VERSION)
    std_path = next(path for path in sdk_paths if (path / "genlayer").is_dir())
    with tempfile.TemporaryDirectory(prefix="clausemesh-sdk-") as temporary:
        sdk_root = Path(temporary)
        shutil.copytree(std_path, sdk_root / "runners/genlayer-py-std/src")
        environment = dict(os.environ, GENVMROOT=str(sdk_root))
        for command, output_name in [
            (["genvm-lint", "check", str(CONTRACT), "--json"], "sdk-check.json"),
            (["genvm-lint", "schema", str(CONTRACT), "--json"], "sdk-schema.json"),
        ]:
            result = subprocess.run(command, env=environment, capture_output=True, text=True)
            (EVIDENCE / output_name).write_text(result.stdout, encoding="utf-8")
            assert result.returncode == 0, result.stderr + result.stdout
    schema = json.loads((EVIDENCE / "sdk-schema.json").read_text())
    methods = schema["schema"]["methods"]
    expected_write = {"create_workspace", "respond_and_seal", "reconcile"}
    expected_view = {"get_workspace", "get_workspace_summaries", "get_relation"}
    assert set(methods) == expected_write | expected_view
    assert {name for name, meta in methods.items() if meta["readonly"]} == expected_view

    vm = VMContext()
    with vm.activate():
        contract = deploy_contract(CONTRACT, vm, sdk_version=SDK_VERSION)
        from genlayer import Address
        alice = Address("0x1111111111111111111111111111111111111111")
        bob = Address("0x2222222222222222222222222222222222222222")
        trigger = Address("0x3333333333333333333333333333333333333333")
        vm.sender = alice
        workspace_id = contract.create_workspace(bob, " Smoke ", [" Mobile access is required. "])
        waiting = contract.get_workspace(workspace_id)
        assert workspace_id == 1 and waiting["derived_status"] == "WAITING_FOR_B"
        assert waiting["label"] == "Smoke" and waiting["clauses_a"] == ["Mobile access is required."]
        assert len(contract.get_workspace_summaries(alice)) == 1
        assert contract.get_workspace_summaries(bob) == []
        assert waiting["relation_matrix"] == []
        vm.sender = bob
        contract.respond_and_seal(workspace_id, ["Mobile access is required."])
        ready = contract.get_workspace(workspace_id)
        assert ready["derived_status"] == "READY" and ready["relation_matrix"] == []
        assert len(contract.get_workspace_summaries(bob)) == 1
        vm.sender = trigger
        # gltest 0.29.2 auto-decodes JSON in every mock even in text mode.
        # Quote the raw JSON text once so its mock decoder returns a string,
        # matching the production exec_prompt(text) result. Contract unchanged.
        raw = '{"matrix":[["EQUIVALENT"]]}'
        vm.mock_llm("(?s).*", json.dumps(raw))
        contract.reconcile(workspace_id)
        stored = contract.get_workspace(workspace_id)
        assert stored["derived_status"] == "RECONCILED" and stored["relation_matrix"] == [1]
        assert contract.get_relation(workspace_id, 0, 0) == 1
        assert len(vm._captured_validators) == 1
        # Native direct mode executes a speculative leader, then invokes the
        # validator separately. This does not prove network consensus/finality.
        assert vm.run_validator() is True
        _, leader_fn, validator_fn = vm._captured_validators[0]
        import cloudpickle
        # Direct mode bypasses serialization; verify the actual closures too.
        serialised = [len(cloudpickle.dumps(fn)) for fn in (leader_fn, validator_fn)]
        for fn in (leader_fn, validator_fn):
            assert "self" not in fn.__code__.co_freevars
        storage_types = {
            "workspaces": type(contract.workspaces).__name__,
            "clauses_a": type(contract.workspaces[0].clauses_a).__name__,
            "clauses_b": type(contract.workspaces[0].clauses_b).__name__,
            "relation_matrix": type(contract.workspaces[0].relation_matrix).__name__,
            "history_map": type(contract.workspace_ids_by_party).__name__,
            "history_array": type(contract.workspace_ids_by_party[alice]).__name__,
        }
        assert storage_types == {
            "workspaces": "DynArray", "clauses_a": "DynArray", "clauses_b": "DynArray",
            "relation_matrix": "DynArray", "history_map": "TreeMap", "history_array": "DynArray",
        }
    report = {
        "scope": "Phase 6 local SDK smoke with mocked LLM; no new remote transactions",
        "python": platform.python_version(), "genvm_bundle": SDK_VERSION,
        "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        "canonical_prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
        "canonical_prompt_verbatim": True, "python_compile": "PASS",
        "sdk_load_and_schema": "PASS", "public_writes": sorted(expected_write),
        "public_views": sorted(expected_view), "happy_path": "PASS",
        "independent_validator_callback": "PASS (mocked)",
        "callback_pickle_sizes": serialised, "storage_types": storage_types,
        "stored_matrix": stored["relation_matrix"],
        "remote_deployment": "NOT RUN BY THIS LOCAL VERIFIER: see separate deployment-status.json",
        "real_multi_validator_reconciliation": "Not run by this local smoke; see retained Phase 5 real network evidence",
    }
    (EVIDENCE / "phase1-smoke.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
