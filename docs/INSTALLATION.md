# Installation

The repository root is the Skill package. Install the whole directory so the host can read `SKILL.md` and its referenced documentation.

## Claude Code

Personal Skill:

~~~text
~/.claude/skills/swarmforge/
~~~

Project Skill:

~~~text
.claude/skills/swarmforge/
~~~

Place `SKILL.md` directly inside the `swarmforge` directory. Claude Code discovers personal and project Skills from its documented locations.

## Claude.ai

1. Download this repository as a ZIP.
2. Ensure `SKILL.md` is at the root of the Skill folder inside the ZIP.
3. Upload it through Claude's Skills settings.
4. Enable code execution where required.
5. Test using a small task and inspect the tools that are actually available.

Custom Skills on Claude.ai require a supported plan and code execution. The interface and availability can change; follow the official instructions in [Sources](SOURCES.md).

## Claude API

Use the documented Skills API and attach the Skill with the required code-execution tool. Claude API Skills run in a constrained sandbox with no network access and no runtime package installation. Use an external orchestrator for networked provider calls or worker fleets.

## Codex CLI and IDE extension

Repository Skill:

~~~text
.agents/skills/swarmforge/
~~~

Personal Skill:

~~~text
~/.agents/skills/swarmforge/
~~~

Codex can also use managed and plugin-distributed Skills. Refresh/restart the host if a newly added Skill is not detected.

## ChatGPT desktop, web, mobile, and Work

Standalone Skills are supported in the documented ChatGPT desktop and Codex surfaces. To distribute SwarmForge to ChatGPT web, mobile, and Work, package it as a plugin. A plugin can bundle the Skill with an MCP server connection that exposes real orchestration tools.

The repository includes optional `agents/openai.yaml` presentation metadata. It does not bundle a server or declare a server dependency.

## VS Code and Copilot

VS Code documents project Skill locations including `.github/skills/`, `.claude/skills/`, and `.agents/skills/`, with corresponding personal locations for supported harnesses. A skill being discoverable does not guarantee agent spawning. Use the selected harness's actual tools.

## Cursor and other clients

Check the client's current documentation for Agent Skills compatibility and its install path. Do not assume compatibility or feature parity. If no live delegation operations are exposed, use the manual fallback or configure an adapter.

## No native delegation?

SwarmForge still provides a task graph, role briefs, file ownership plan, and execution order. For live workers, configure one of the options in [Execution modes](EXECUTION_MODES.md) and implement the operations in [Adapter contract](ADAPTER_CONTRACT.md).

## Verify installation

Invoke SwarmForge on a task with two independent read-only workstreams. Confirm that the host reports actual worker sessions and that the coordinator collects their results. Do not begin with simultaneous writes to the same file.
