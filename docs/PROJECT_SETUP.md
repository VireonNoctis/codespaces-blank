# SwarmForge Setup and Validation

This is a portable Agent Skill package. It is not a runtime service.

## Install the Skill

Install the whole repository directory in the host's documented Skill location. The root must contain `SKILL.md`. Use [INSTALLATION.md](INSTALLATION.md) for host-specific paths and [PLATFORM_COMPATIBILITY.md](PLATFORM_COMPATIBILITY.md) for supported surfaces.

## Choose an execution backend

1. Prefer native subagents or agent teams exposed by the host.
2. Use an already configured MCP orchestration bridge when multiple clients need the same worker service.
3. Use a provider API/SDK orchestrator when custom routing, quotas, and lifecycle control are required.
4. Use local CLI workers for developer-machine execution.
5. Use a durable remote queue and isolated worker fleet for workloads that justify operating infrastructure.
6. Fall back to a single-agent task plan when no real delegation mechanism is available.

Compare the choices in [EXECUTION_MODES.md](EXECUTION_MODES.md).

## Package checks

Run from the repository root:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The GitHub Actions workflow runs these checks on pushes and pull requests.

## Adding a provider adapter

Read [ADAPTER_CONTRACT.md](ADAPTER_CONTRACT.md). Implement real capability discovery, worker creation, status, waiting, cancellation, result collection, and workspace controls. Do not add guessed provider APIs or expose credentials in Skill files.

## Before claiming 500-agent support

Review [SCALING_TO_500.md](SCALING_TO_500.md). A 500-session claim requires a real orchestrator, provider capacity, isolated workspaces, cost controls, and repeatable concurrency/load-test evidence. The Skill alone does not supply these.
