# ADR 0001: The Skill is the product

- Status: Accepted
- Date: 2026-10-30

## Context

The objective is to coordinate specialist agents across coding assistants such as Claude and ChatGPT/Codex. The user explicitly wants a portable `/skill`, not a standalone IDE or new editor.

## Decision

Ship SwarmForge as a portable Agent Skill with root `SKILL.md`. Keep execution backends optional and capability-driven: native host delegation first, then MCP, provider API/SDK, local CLI, remote queue, and CI execution.

## Alternatives considered

- Standalone IDE: rejected as the primary deliverable because it is not a Skill.
- Prompt-only mega-prompt: rejected because it lacks progressive disclosure and reusable references.
- Mandatory proprietary backend: rejected because it would prevent hosts with native agents from using their own runtime.
- Claim 500 agents from the Skill itself: rejected because instructions cannot override host/provider capacity.

## Consequences

The package is portable across compatible hosts. Live execution depends on actual host tools or a configured adapter. 500 remains a target ceiling until a real execution layer is implemented and load-tested.
