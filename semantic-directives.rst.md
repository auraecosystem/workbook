

# Explicit Directive Response Schemas

The SCRIPT.GOD directive layer defines explicit response schemas for
semantic analysis and execution.

These schemas provide a stable interface between neural interpretation,
symbolic reasoning, execution engines, model providers, and verification
systems.

The canonical response envelope is:

::

```
DirectiveResponse {
    protocol
    version
    directive
    request_id
    status
    subject
    semantic_state
    execution
    verification
    evidence
    errors
    warnings
    timestamps
}
```

## Fields

`protocol`
Protocol identifier. MUST be `SCRIPT.GOD`.

`version`
Semantic protocol version.

`directive`
Directive that produced the response.

`request_id`
Unique identifier for correlating the request and all derived events.

`status`
Current operation state.

Allowed values:

::

```
ACCEPTED
PROCESSING
COMPLETE
PARTIAL
BLOCKED
FAILED
CANCELLED
```

`subject`
Original subject or normalized task description.

`semantic_state`
Semantic intermediate representation.

`execution`
Execution plan and execution state, when applicable.

`verification`
Verification requirements and observed verification state.

`evidence`
Machine- or human-observable evidence supporting the response.

`errors`
Structured errors.

`warnings`
Non-fatal conditions that may affect interpretation or execution.

`timestamps`
Lifecycle timestamps.

## Canonical JSON Envelope

::

```
{
  "protocol": "SCRIPT.GOD",
  "version": "1.0",
  "directive": "^↑D",
  "request_id": "req_01J...",
  "status": "COMPLETE",
  "subject": "...",
  "semantic_state": {},
  "execution": null,
  "verification": {},
  "evidence": [],
  "errors": [],
  "warnings": [],
  "timestamps": {
    "created_at": "...",
    "completed_at": "..."
  }
}
```

# ^↑D Response Schema

The `^↑D` response MUST represent the semantic analysis produced by the
directive.

Conceptual schema:

::

```
DeepSemanticResponse {
    protocol: "SCRIPT.GOD"
    version: string
    directive: "^↑D"
    request_id: string
    status: Status
    subject: string

    semantic_state: {
        intent: Intent
        concepts: Concept[]
        entities: Entity[]
        relationships: Relationship[]
        requirements: Requirement[]
        constraints: Constraint[]
        dependencies: Dependency[]
        assumptions: Assumption[]
        inferences: Inference[]
        alternatives: Alternative[]
        risks: Risk[]
        unknowns: Unknown[]
        invariants: Invariant[]
        execution_requirements: ExecutionRequirement[]
        verification_requirements: VerificationRequirement[]
    }

    execution: null | ExecutionPlan

    verification: VerificationState

    evidence: Evidence[]

    errors: Error[]
    warnings: Warning[]

    timestamps: Timestamps
}
```

## Intent

::

```
Intent {
    primary: string
    goals: string[]
    scope: string
    non_goals: string[]
    priority: string
}
```

## Concept

::

```
Concept {
    id: string
    name: string
    description: string
    type: string
    confidence: number
}
```

`confidence` MUST be between `0` and `1`.

## Entity

::

```
Entity {
    id: string
    name: string
    type: string
    description: string
    source: string | null
}
```

## Relationship

::

```
Relationship {
    source: string
    relation: string
    target: string
    description: string
    confidence: number
}
```

Examples of `relation` include:

::

```
depends_on
implements
extends
calls
produces
consumes
constrains
verifies
routes
delegates
contains
conflicts_with
```

## Requirement

::

```
Requirement {
    id: string
    statement: string
    priority: "MUST" | "SHOULD" | "MAY"
    source: string
    acceptance_criteria: string[]
}
```

## Constraint

::

```
Constraint {
    id: string
    category: string
    statement: string
    severity: "REQUIRED" | "IMPORTANT" | "ADVISORY"
    source: string
}
```

## Dependency

::

```
Dependency {
    id: string
    subject: string
    type: string
    required: boolean
    version: string | null
    reason: string
}
```

## Assumption

::

```
Assumption {
    id: string
    statement: string
    confidence: number
    validation_required: boolean
}
```

## Inference

::

```
Inference {
    id: string
    statement: string
    derived_from: string[]
    confidence: number
}
```

## Alternatives

::

```
Alternative {
    id: string
    description: string
    advantages: string[]
    disadvantages: string[]
    rejected: boolean
    rejection_reason: string | null
}
```

## Risk

::

```
Risk {
    id: string
    description: string
    category: string
    likelihood: "LOW" | "MEDIUM" | "HIGH"
    impact: "LOW" | "MEDIUM" | "HIGH"
    mitigation: string | null
}
```

## Unknown

::

```
Unknown {
    id: string
    question: string
    impact: "LOW" | "MEDIUM" | "HIGH"
    blocking: boolean
}
```

## Invariant

::

```
Invariant {
    id: string
    statement: string
    verification_method: string
}
```

## ExecutionRequirement

::

```
ExecutionRequirement {
    id: string
    action: string
    required_capabilities: string[]
    authorization_required: boolean
    environment: string | null
}
```

## VerificationRequirement

::

```
VerificationRequirement {
    id: string
    assertion: string
    method: string
    required: boolean
}
```

## Example `^↑D` Response

::

```
{
  "protocol": "SCRIPT.GOD",
  "version": "1.0",
  "directive": "^↑D",
  "request_id": "req_001",
  "status": "COMPLETE",
  "subject": "neural-symbolic compilation",

  "semantic_state": {
    "intent": {
      "primary": "Understand neural-symbolic compilation",
      "goals": [
        "define the concept",
        "explain the architecture",
        "identify the compilation boundary"
      ],
      "scope": "research",
      "non_goals": [],
      "priority": "HIGH"
    },

    "concepts": [
      {
        "id": "c1",
        "name": "neural reasoning",
        "description": "Flexible statistical inference over representations",
        "type": "computational_paradigm",
        "confidence": 0.96
      },
      {
        "id": "c2",
        "name": "symbolic representation",
        "description": "Explicit structured representation of rules and relationships",
        "type": "computational_paradigm",
        "confidence": 0.98
      }
    ],

    "entities": [],
    "relationships": [],
    "requirements": [],
    "constraints": [],
    "dependencies": [],
    "assumptions": [],
    "inferences": [],
    "alternatives": [],
    "risks": [],
    "unknowns": [],
    "invariants": [],

    "execution_requirements": [],
    "verification_requirements": [
      {
        "id": "v1",
        "assertion": "The semantic model distinguishes neural inference from symbolic execution",
        "method": "semantic_review",
        "required": true
      }
    ]
  },

  "execution": null,

  "verification": {
    "required": true,
    "status": "COMPLETE",
    "checks": [
      {
        "id": "v1",
        "status": "PASS"
      }
    ]
  },

  "evidence": [
    {
      "type": "analysis",
      "source": "model",
      "reference": null,
      "content": "..."
    }
  ],

  "errors": [],
  "warnings": [],

  "timestamps": {
    "created_at": "...",
    "completed_at": "..."
  }
}
```

# ^D Response Schema

The `^D` response represents executable intent and its observed result.

Conceptual schema:

::

```
DeepExecutionResponse {
    protocol: "SCRIPT.GOD"
    version: string
    directive: "^D"
    request_id: string
    status: Status
    subject: string

    semantic_state: SemanticState

    execution: {
        plan: ExecutionPlan
        operations: Operation[]
        state: ExecutionState
        outputs: Output[]
        mutations: Mutation[]
    }

    verification: VerificationState

    evidence: Evidence[]

    errors: Error[]
    warnings: Warning[]

    timestamps: Timestamps
}
```

## ExecutionPlan

::

```
ExecutionPlan {
    id: string
    objective: string
    prerequisites: string[]
    steps: ExecutionStep[]
    rollback_strategy: string | null
}
```

## ExecutionStep

::

```
ExecutionStep {
    id: string
    action: "CREATE"
         | "MODIFY"
         | "REMOVE"
         | "REFACTOR"
         | "CONFIGURE"
         | "TEST"
         | "VERIFY"

    description: string
    dependencies: string[]
    required_capabilities: string[]
    authorization_required: boolean
    expected_outputs: string[]
}
```

## Operation

::

```
Operation {
    id: string
    step_id: string
    command: string | null
    tool: string | null
    target: string | null
    status: ExecutionState
    started_at: string | null
    completed_at: string | null
}
```

Allowed execution states:

::

```
PENDING
READY
RUNNING
SUCCEEDED
FAILED
BLOCKED
CANCELLED
ROLLED_BACK
```

## Mutation

A mutation records a change made to an external system.

::

```
Mutation {
    id: string
    target: string
    operation: string
    before: string | null
    after: string | null
    reversible: boolean
    rollback_operation: string | null
}
```

## Output

::

```
Output {
    id: string
    type: string
    content: string | null
    location: string | null
    content_hash: string | null
}
```

## Example `^D` Response

::

```
{
  "protocol": "SCRIPT.GOD",
  "version": "1.0",
  "directive": "^D",
  "request_id": "req_002",
  "status": "COMPLETE",
  "subject": "implement the semantic directive parser",

  "semantic_state": {
    "intent": {
      "primary": "Implement a parser for ^↑D and ^D",
      "goals": [
        "recognize directives",
        "parse arguments",
        "produce structured output"
      ],
      "scope": "repository",
      "non_goals": [],
      "priority": "HIGH"
    }
  },

  "execution": {
    "plan": {
      "id": "plan_001",
      "objective": "Implement semantic directive parsing",
      "prerequisites": [],
      "steps": [
        {
          "id": "step_001",
          "action": "CREATE",
          "description": "Create directive parser",
          "dependencies": [],
          "required_capabilities": ["code"],
          "authorization_required": false,
          "expected_outputs": ["parser"]
        },
        {
          "id": "step_002",
          "action": "TEST",
          "description": "Test directive recognition",
          "dependencies": ["step_001"],
          "required_capabilities": ["code"],
          "authorization_required": false,
          "expected_outputs": ["test-results"]
        }
      ],
      "rollback_strategy": null
    },

    "operations": [],
    "state": "SUCCEEDED",
    "outputs": [],
    "mutations": []
  },

  "verification": {
    "required": true,
    "status": "PASS",
    "checks": [
      {
        "id": "check_001",
        "assertion": "Parser recognizes ^↑D",
        "status": "PASS"
      },
      {
        "id": "check_002",
        "assertion": "Parser recognizes ^D",
        "status": "PASS"
      }
    ]
  },

  "evidence": [],
  "errors": [],
  "warnings": [],

  "timestamps": {
    "created_at": "...",
    "completed_at": "..."
  }
}
```

# Error Schema

Errors MUST be structured.

::

```
Error {
    code: string
    message: string
    phase: string
    severity: "ERROR" | "FATAL"
    retryable: boolean
    details: object | null
}
```

Canonical error codes include:

::

```
INVALID_DIRECTIVE
INVALID_SCHEMA
MISSING_CONTEXT
SEMANTIC_AMBIGUITY
POLICY_DENIED
AUTHORIZATION_REQUIRED
CAPABILITY_UNAVAILABLE
DEPENDENCY_FAILURE
EXECUTION_FAILURE
VERIFICATION_FAILURE
RESOURCE_EXHAUSTED
TIMEOUT
PROVIDER_FAILURE
INTERNAL_ERROR
```

# Evidence Schema

Evidence is distinct from claims.

::

```
Evidence {
    type: string
    source: string
    reference: string | null
    content: string | null
    content_hash: string | null
    timestamp: string
}
```

Examples:

::

```
{
  "type": "test_result",
  "source": "npm",
  "reference": "test-run-123",
  "content": "42 tests passed",
  "content_hash": null,
  "timestamp": "..."
}
```

Evidence MUST NOT be fabricated.

# Verification Schema

::

```
VerificationState {
    required: boolean
    status: "PENDING"
           | "RUNNING"
           | "PASS"
           | "FAIL"
           | "PARTIAL"
           | "NOT_APPLICABLE"

    checks: VerificationCheck[]
}
```

::

```
VerificationCheck {
    id: string
    assertion: string
    method: string
    status: "PENDING" | "PASS" | "FAIL" | "SKIPPED"
    evidence_ids: string[]
    failure_reason: string | null
}
```

# Response Invariants

The following invariants are normative.

1. Every directive response MUST identify the directive.

2. Every response MUST contain a unique `request_id`.

3. `^↑D` MUST NOT claim execution unless execution was explicitly
   requested and actually performed.

4. `^D` MUST preserve the semantic requirements supplied to it.

5. A response with `status = COMPLETE` MUST satisfy all required
   verification checks.

6. A response with failed required verification MUST NOT have
   `status = COMPLETE`.

7. `BLOCKED` MUST contain an actionable reason.

8. `FAILED` MUST contain at least one structured error.

9. Evidence MUST correspond to an observable operation or source.

10. Claims without evidence MUST NOT be represented as verified facts.

11. Security and authorization policy MUST be evaluated independently of
    semantic intent.

12. Provider-specific response formats MUST be normalized into the
    SCRIPT.GOD response schema before being exposed to higher layers.

# Directive Composition Contract

When directives are chained:

::

```
^↑D
  |
  v
DeepSemanticResponse
  |
  v
^D
  |
  v
DeepExecutionResponse
  |
  v
VERIFY
  |
  v
RESULT
```

The `request_id` SHOULD remain correlated across the complete operation
chain.

A derived execution request SHOULD reference the semantic response that
produced it.

::

```
execution.semantic_source = "req_001"
```

This creates a traceable chain:

::

```
INTENT
  |
  v
req_001
^↑D
  |
  v
SEMANTIC MODEL
  |
  v
req_002
^D
  |
  v
EXECUTION
  |
  v
EVIDENCE
  |
  v
VERIFICATION
  |
  v
RESULT
```

# Neural-Symbolic Boundary

The response schema deliberately separates:

::

```
semantic_state
execution
verification
evidence
```

This establishes the neural-symbolic boundary.

The model may infer semantic structure.

The execution layer operates on explicit structure.

The verification layer determines whether the resulting system satisfies
the required assertions.

Therefore:

::

```
MODEL OUTPUT
    ≠
VERIFIED FACT
```

and:

::

```
INTENT
    ≠
AUTHORIZATION
```

and:

::

```
PLAN
    ≠
EXECUTION
```

and:

::

```
EXECUTION
    ≠
VERIFIED SUCCESS
```

These distinctions are fundamental protocol invariants.

# Schema Evolution

Protocol versions MUST be explicit.

Backward-compatible fields MAY be added without changing the major
protocol version.

Breaking changes MUST increment the major version.

::

```
1.x
  |
  +-- compatible additions

2.0
  |
  +-- breaking schema changes
```

Consumers SHOULD reject unsupported major versions rather than silently
interpreting incompatible responses.

# Canonical Transformation

The complete directive transformation is:

::

```
^↑D
  |
  v
DeepSemanticResponse
  |
  v
Semantic IR
  |
  v
ExecutionPlan
  |
  v
^D
  |
  v
DeepExecutionResponse
  |
  v
VerificationState
  |
  v
Evidence
  |
  v
RESULT
```

This response contract makes SCRIPT.GOD suitable for implementation as a
typed protocol rather than merely a natural-language convention.

One important correction to the earlier design: I would not make `^D` directly consume arbitrary prose emitted by `^↑D`. The semantic response should become an explicit intermediate representation (IR). That gives you the neural-symbolic compiler boundary you were aiming for and makes the protocol implementable in TypeScript, Python, Rust, or Go with JSON Schema/OpenAPI validation.
