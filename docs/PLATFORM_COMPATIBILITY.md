# Platform Compatibility

Agent Skills standardize packaging and instructions, not identical runtime behavior. Reviewed on 2026-10-30; re-check official sources before changing claims.

## Compatibility matrix

| Host / surface | Skill packaging | Live multi-agent execution |
|---|---|---|
| Claude Code | Project `.claude/skills/` or personal `~/.claude/skills/` directory | Native subagents; Agent Teams where enabled |
| Claude.ai | Upload custom Skill ZIP through Skills settings; code execution required | Depends on enabled product tools; upload alone does not guarantee a worker pool |
| Claude API | Skills API with code-execution tool | API orchestration or external service required; API Skill sandbox has no network access |
| ChatGPT desktop | Standalone Skill | Use the subagent capabilities exposed by the host |
| Codex CLI / IDE extension | Repository or user `.agents/skills/` directory | Native subagents in supported configurations |
| ChatGPT web / mobile / Work | Distribute as a plugin that includes the Skill; plugin can include MCP servers | Use bundled MCP tools or tools provided by the current host |
| VS Code / Copilot | Supported skill folders include `.github/skills/`, `.claude/skills/`, and `.agents/skills/` | Depends on selected harness and available tools |
| Cursor or another client | Confirm its current Agent Skills support and install path | Only native delegation or a configured adapter actually exposed by that client |
| Generic Agent Skills host | Load this directory and root `SKILL.md` | No delegation unless the host provides it |

## Claude

Claude Code discovers custom Skills as directories containing `SKILL.md`; personal and project locations are documented by Anthropic. Claude Code also has subagents and Agent Teams, which are distinct execution approaches with different coordination and resource behavior.

Claude.ai accepts uploaded Skills as ZIPs on supported plans with code execution enabled. Claude API supports custom Skills alongside code execution, but Skills run in a sandbox with no network access and no runtime package installation. Do not assume an API Skill can directly call arbitrary provider APIs.

## ChatGPT and Codex

OpenAI documents the Agent Skills format for ChatGPT and Codex. Codex discovers repository and user Skill directories under `.agents/skills`. ChatGPT desktop also supports standalone Skills. For ChatGPT web, mobile, and Work distribution, package the Skill in a plugin; plugins can include MCP servers that provide live external tools.

The optional `agents/openai.yaml` supplies presentation metadata for supported OpenAI Skill surfaces. It does not create an orchestration backend.

## VS Code and other hosts

VS Code documents project skill directories including `.github/skills/`, `.claude/skills/`, and `.agents/skills/`, plus personal locations for supported harnesses. Discovery does not guarantee that the model will invoke the Skill on every relevant request, nor does it imply agent spawning is supported.

For any other client:
1. Confirm it supports the Agent Skills format.
2. Install the whole Skill directory in its documented location.
3. Inspect the tools and delegation operations actually exposed.
4. Configure an adapter if live worker creation is needed and native delegation is absent.
5. Test with independent read-only tasks before allowing concurrent writes.

## Not guaranteed

SwarmForge does not promise a Skill can force a product to spawn agents, that all clients share tool names or workspace access, that a subscription includes API usage, or that a 500-session pool is available on any specific account. No third-party product endorsement is implied.
