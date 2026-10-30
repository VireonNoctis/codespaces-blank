# Architecture

## Product boundary

SwarmForge is a portable Agent Skill. It provides instructions, task contracts, coordination policies, and operational guidance. It is not an agent runtime and does not create model sessions without host-provided tools or a separately deployed adapter.

The portable Skill is intentionally independent of one model vendor. Host adapters translate its generic workflow into the operations supported by a particular runtime.

## Logical architecture

~~~mermaid
flowchart TD
    U[User objective] --> S[SwarmForge Skill]
    S --> C[Capability discovery]
    C --> P[Task planner and dependency graph]
    P --> O[Orchestration strategy]
    O --> H{Confirmed host capability}
    H -->|Native| N[Native subagents or teams]
    H -->|MCP| M[Connected orchestration tools]
    H -->|API| A[Provider API or SDK]
    H -->|Local| L[CLI and process workers]
    H -->|Remote| R[Queue and worker pool]
    H -->|Unavailable| F[Single-agent plan and task briefs]
    N --> I[Result collection]
    M --> I
    A --> I
    L --> I
    R --> I
    F --> I
    I --> V[Integration and verification]
    V --> D[Auditable delivery]
~~~

This is a logical design, not a claim that all adapters are implemented in this repository.

## Layers

| Layer | Responsibility | Must not assume |
|---|---|---|
| Skill | Plan, delegate policy, contracts, verify | A particular tool or runtime |
| Host adapter | Map generic tasks to host operations | Other hosts have equivalent APIs |
| Orchestrator | Queue, dependencies, lifecycle, quotas, retries | Unlimited provider capacity |
| Workspace provider | Filesystem, worktree, container, patch exchange | Shared writes are safe |
| Model provider | Inference, tool calls, model limits | All vendors behave identically |
| Integration gate | Conflict resolution, tests, final report | Worker summaries prove correctness |

## Worker lifecycle

1. Discover capabilities and limits.
2. Plan tasks and dependency edges.
3. Admit tasks under global and provider budgets.
4. Execute with the selected runtime.
5. Observe status, logs, cancellation, and usage.
6. Collect results and integrate them.
7. Verify, close sessions, release workspaces, and report.

## Task state model

- `pending`: planned but not dispatched.
- `ready`: dependencies satisfied and capacity available.
- `running`: worker session confirmed active.
- `blocked`: waiting on a dependency, permission, or resource.
- `completed`: deliverable returned and accepted.
- `failed`: execution ended unsuccessfully.
- `cancelled`: intentionally stopped.

A job is not an agent. Reports must distinguish queued tasks, active sessions, terminal sessions, and retries.

## Collaboration topologies

SwarmForge supports fan-out/fan-in, hierarchical supervisors, DAG pipelines, map/reduce, independent reviewer panels, competing hypotheses, peer teams, and hybrid execution. See [Orchestration patterns](ORCHESTRATION_PATTERNS.md).

## Workspace isolation

Preferred approaches for concurrent code writers:

1. Separate worktree or branch per writer.
2. Patch-based contributions with one integrator.
3. Non-overlapping file ownership in a shared filesystem.
4. Serialized writes where overlap cannot be avoided.

Read-only research can use a shared snapshot. Code changes should be integrated in a controlled workspace.

## Failure and observability

Represent provider errors, missing permissions, rate limits, timeouts, malformed results, and conflicts as visible task states. Retry only transient failures.

A production adapter should expose task/session ID, provider/model, role, status, timestamps, retry count, workspace or patch reference, usage/cost when available, and error reason. Avoid logging prompts, source files, and secrets by default.

## Related decisions

- [ADR 0001: Skill is the product](DECISIONS/0001-skill-is-the-product.md)
