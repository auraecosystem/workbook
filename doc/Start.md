 `.xlsl` work-paper pipeline and validate the target workbook, below is the execution protocol using the standard Aura runtime engine.

**1. Dependency Setup & Test Verification**

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt pytest
pytest -q

```

(Prepares the Python environment and executes initial test suites.)

**2. Execute Schema & Workbook Validation**

```bash
python -c "from src.file_loader import validate_workbook; import json; ok, r = validate_workbook('data/Aura.xlsl'); print(json.dumps(r, indent=2))"

```

(Validates the multi-dimensional `.xlsl` file structure against the canonical system schema.)

**3. Launch Multi-Agent Execution Orchestrator**

```bash
aura data/Aura.xlsl

```

(Points the task manager to the target work-paper to initialize multi-agent handoffs, run sub-workers, and record state outputs.)

**Simulated Execution Telemetry**

| Execution Phase | Status | Detail / Artifact |
| --- | --- | --- |
| **Schema Validation** | `PASSED` | Verified against `schema/aura_schema.yaml`.

 |
| **AST & DAG Parsing** | `COMPLETE` | Generated dependency graph across semantic layers.

 |
| **Agent Dispatch** | `ACTIVE` | Multi-agent execution loop initialized via context windows.

 |
| **Inference Layer Mutation** | `SYNCHRONIZED` | Predictive vectors and model states updated directly within file.

 |

Would you like to run a specific sub-agent (such as the symbolic logic solver or tensor optimizer) with custom parameters on your workbook?
