# Execution Modes

SwarmForge selects only mechanisms confirmed to exist in the current host and installation.

## A. Native subagents

The host exposes real tools to create agents, pass tasks, collect results, and possibly message or cancel workers. Best for focused parallel work with low setup. Host limits, context, model selection, and permissions remain authoritative.

## B. Native agent teams

The host exposes multiple sessions with direct teammate communication and shared coordination state. Best for work requiring discussion, task claiming, and domain ownership. Shared task state does not make concurrent file edits safe.

## C. MCP orchestration bridge

A configured Model Context Protocol server exposes worker lifecycle tools to compatible hosts. This is a strong cross-client option: one orchestration service can serve different AI products through their MCP connections.

MCP is a tool protocol, not a scheduler. The server must implement or proxy worker creation, status, messaging, waiting, cancellation, workspace isolation, quotas, and result collection. A connected MCP server does not imply capacity for 500 workers.

## D. Provider API / SDK orchestrator

A dedicated service calls model-provider APIs and manages session creation, tools, scheduling, workspace, retries, budgets, and results. Possible designs include one provider pool, multiple providers behind a router, role-based model selection, provider fallback, or supervisor agents delegating to specialized agents.

This offers the most control over scheduling and large-scale execution, but requires provider-specific adapters, credentials, quota handling, cost controls, and operations. Provider APIs are not interchangeable.

## E. Local CLI / process workers

A process manager launches installed coding-agent CLIs with scoped task briefs and workspaces. Best for local development. Use separate Git worktrees, clones, containers, or patch output. Local CPU, memory, disk, process count, authentication, and provider limits become constraints.

## F. Remote queue and worker pool

A durable queue dispatches tasks to container/VM workers. Typical supporting components include a task database, queue, worker images, workspace service, object storage, logs, metrics, and cancellation channel. Best for durable large fan-out, but requires real infrastructure, security isolation, monitoring, and cost operations. Not included in this Skill repository.

## G. CI matrix / build farm

Independent jobs run in CI and publish artifacts for integration. Best for tests, static scans, deterministic builds, and bounded non-interactive tasks. CI jobs are not inherently AI agents; a workflow must invoke a real agent runner.

## H. Manual / single-agent fallback

When no delegation exists, SwarmForge creates a dependency graph, role briefs, file ownership plan, and execution order for the user or another runtime. This fallback must never simulate workers or invent results.

## Workspace strategies

| Strategy | Isolation | Trade-off |
|---|---|---|
| Shared mutable workspace | Low | Fast but conflict-prone; serialize writers |
| Git worktrees | High between working trees | Shared Git object database; coordinate commits |
| Separate clones | Strong separation | More disk and network usage |
| Containers/VMs | Process and filesystem boundaries | Resource and setup overhead |
| Patch-only workers | No shared writes | Integrator applies and tests patches |
| Read-only snapshot | Strong against accidental edits | No direct implementation |

## Recommended progression

Start with native delegation. Add an MCP bridge when multiple hosts need the same interface. Add a provider SDK service when stronger routing and scheduling are needed. Build a remote worker pool only when workload evidence justifies operating it.
