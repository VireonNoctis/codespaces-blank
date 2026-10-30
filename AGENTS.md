# SwarmForge Repository Instructions

These rules apply to the Skill and its documentation.

## Before editing

1. Read the relevant sections of SKILL.md and supporting docs.
2. Inspect the current tree, tests, workflows, and existing conventions.
3. Verify Agent Skills format and provider behavior from current official documentation before adding compatibility claims.
4. Decide whether a change belongs in the portable Skill, platform-specific docs, or an optional adapter contract.
5. Preserve the distinction between instructions and implemented runtime functionality.

## Engineering standards

- Prefer the smallest complete implementation.
- Keep vendor-specific behavior out of the portable Skill unless required.
- Never invent tool names, CLI flags, endpoints, quotas, limits, or host support.
- Do not represent queued jobs or logical roles as running agents.
- Treat 500 as a target ceiling, not an unconditional guarantee.
- Preserve the existing repository hygiene, security checks, and dependency-light approach.
- Never commit credentials, secrets, personal information, or production data.

## Verification

Run:

~~~bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
~~~

Validate Markdown links and YAML/JSON where relevant. Only report checks that were actually run. Do not claim a provider integration or 500-agent load test without a real implementation and evidence.

## Documentation

Update README.md when the product boundary or setup changes. Keep PLATFORM_COMPATIBILITY.md tied to current official sources. Update SOURCES.md when adding provider claims. Record major architecture decisions in docs/DECISIONS/.

## Git hygiene

Keep changes focused. Do not rewrite shared history or force-push. Prefer one cohesive commit and a reviewable pull request for a single template/Skill revamp.
