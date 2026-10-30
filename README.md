# SwarmForge

> A portable multi-agent orchestration Skill for coding agents. Coordinate specialist agents across supported hosts, with a design target of up to 500 concurrent sessions when the runtime, provider quotas, and infrastructure allow it.

SwarmForge is a **Skill**, not an IDE and not a hosted agent service. Its job is to make an AI coding assistant behave like a disciplined engineering lead: inspect the project, decompose work, delegate independent tasks, coordinate specialists, integrate their changes, and verify the result.

It follows the Agent Skills format: a directory with a required `SKILL.md` and optional references, scripts, and metadata. This repository is itself the Skill package.

**Important:** A Skill can instruct a host to use tools that already exist. It cannot create model sessions, raise provider limits, or guarantee 500 concurrent agents by itself. Live parallel execution requires native subagent/team tools or a configured orchestration bridge. When those are absent, SwarmForge falls back to a truthful single-agent plan.

## What SwarmForge is designed to do

- Break complex engineering work into dependency-aware tasks.
- Use native subagents or agent teams where the host provides them.
- Support external orchestration through configured MCP tools, provider APIs/SDKs, local CLI workers, or remote worker queues.
- Coordinate architecture, research, implementation, testing, security, review, and integration roles.
- Use fan-out/fan-in, hierarchical teams, DAG pipelines, map/reduce, independent reviewers, and hybrid provider workflows.
- Control concurrency with global and per-provider limits, backpressure, budgets, retries, and cancellation.
- Prevent edit collisions through isolated worktrees, patch-based contributions, or explicit file ownership.
- Verify integrated changes and report evidence instead of trusting worker summaries.

## The 500-agent target

500 is a **configurable global ceiling**, not the default number of agents to launch and not a promise that every AI product can reach it. Effective capacity is constrained by the lowest applicable host, provider, model, account, workspace, and budget limit.

SwarmForge must distinguish real active sessions from queued tasks, planned roles, and retries. It must never claim a 500-agent run unless 500 distinct worker sessions were actually admitted and observed. See [Scaling to 500](docs/SCALING_TO_500.md).

## Get started

1. Read [`SKILL.md`](SKILL.md), the portable agent playbook.
2. Follow [Installation](docs/INSTALLATION.md) for Claude, ChatGPT/Codex, or another compatible host.
3. Review [Platform compatibility](docs/PLATFORM_COMPATIBILITY.md) to understand the host-specific differences.
4. Select an execution approach from [Execution modes](docs/EXECUTION_MODES.md).
5. Use native delegation first. Add an MCP/API/CLI/remote adapter only when needed.
6. Validate the package locally:

~~~bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
~~~

No provider key is required to read or install the Skill. External execution services require their own credentials and terms. Keep credentials in the relevant secret manager or environment, never in the Skill files or prompts.

## Repository structure

~~~text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── docs/
│   ├── ADAPTER_CONTRACT.md
│   ├── ARCHITECTURE.md
│   ├── EXECUTION_MODES.md
│   ├── INSTALLATION.md
│   ├── ORCHESTRATION_PATTERNS.md
│   ├── PLATFORM_COMPATIBILITY.md
│   ├── SCALING_TO_500.md
│   ├── SECURITY_MODEL.md
│   ├── SOURCES.md
│   ├── WORKFLOWS.md
│   └── DECISIONS/
├── scripts/
│   └── validate.py
└── tests/
    └── test_skill_package.py
~~~

## Core principles

**Skill first.** The portable workflow is the product. Runtime adapters are optional.

**Capability-aware.** Use only tools and limits confirmed by the current host.

**Parallelize independence.** Do not spawn agents for trivial work or tightly coupled steps.

**Bounded execution.** Concurrency, cost, retries, tool access, and runtime are controlled.

**Isolated changes.** Concurrent writers should not share mutable files without ownership or locking.

**Verified outcomes.** Integrate, test, review, and report what actually happened.

## Scope today

This repository contains the portable Skill, cross-platform installation guidance, orchestration designs, adapter contracts, security guidance, and validation tooling. It does **not** currently ship a production orchestrator, MCP server, provider API integration, remote worker fleet, or 500-agent load test. These are extension paths documented for implementation; they are not represented as existing functionality.

## Documentation

| Topic | Document |
|---|---|
| Overall system design | [Architecture](docs/ARCHITECTURE.md) |
| Native, MCP, API, CLI, queue, and CI options | [Execution modes](docs/EXECUTION_MODES.md) |
| Different ways to coordinate agents | [Orchestration patterns](docs/ORCHESTRATION_PATTERNS.md) |
| Host setup | [Installation](docs/INSTALLATION.md) |
| Claude, ChatGPT/Codex, VS Code, and other hosts | [Platform compatibility](docs/PLATFORM_COMPATIBILITY.md) |
| Capacity planning and 500 sessions | [Scaling to 500](docs/SCALING_TO_500.md) |
| Building an external bridge | [Adapter contract](docs/ADAPTER_CONTRACT.md) |
| Permissions and isolation | [Security model](docs/SECURITY_MODEL.md) |
| Repeatable engineering recipes | [Workflows](docs/WORKFLOWS.md) |
| Official documentation links | [Sources](docs/SOURCES.md) |

## Contributing

Read [AGENTS.md](AGENTS.md) before contributing. Keep the root Skill portable, put vendor-specific behavior in references, and verify current official documentation before adding compatibility claims.

## License

No license is included yet. Until a license is selected and added, do not assume permission to reuse, modify, or redistribute this repository.
