# Engineering Instructions

These instructions apply across this repository. More specific instructions in a nested `AGENTS.md` may refine them for that directory.

The goal is to build work that feels considered, reliable, and genuinely useful. Keep the code straightforward and the product polished. Use these notes as practical guidance, not as a script: apply what fits the project, and use good judgement when a check does not.

## Before changing code

1. Inspect the existing implementation, project structure, relevant documentation, and tests.
2. Identify the actual cause or requirement before editing.
3. Check whether an existing helper, dependency, or pattern already solves the problem.
4. Keep the proposed change proportional to the task.

## Implementation standards

- Prefer simple, explicit, maintainable code over clever abstractions.
- Make the smallest complete change. Do not refactor unrelated areas.
- Preserve existing public interfaces and data formats unless the task requires a change.
- Avoid adding dependencies when the standard library or existing tooling is sufficient.
- Validate inputs at boundaries and handle failure paths deliberately.
- Keep secrets, credentials, personal data, and production data out of source control and logs.
- Do not add placeholder implementations, fake data, silent fallbacks, or success messages for unfinished behavior.
- Follow the language, formatting, naming, and architecture conventions already used by the project.

## Product and interface quality

Treat the interface as part of the product, not a coat of paint added at the end.

- Remove filler badges, redundant labels, random italics, and decorative details that do not help someone understand or use the product.
- Use monospace text only when it communicates something that benefits from it, such as code or technical values.
- Establish a small, consistent design system for colour, type, spacing, radii, borders, shadows, and motion. Reuse it rather than inventing one-off values throughout the interface.
- Show the real product and its useful states. Give the main feature enough room and visual weight to be understood.
- Group related content with spacing. Write specific headlines, make the main action easy to recognise, and use an accent colour with restraint.
- Keep icon families, stroke weights, sizing, and alignment consistent. Remove embellishments that compete with the content.
- Keep nested corner radii visually coherent. As a useful rule, the inner radius is the outer radius minus the surrounding padding.
- Make text readable against its background, and check headline wrapping at narrow and wide viewport sizes.
- Align things by how they look together, not only by whether their coordinates match.
- Use tabular numerals for values that need to line up, such as counters, prices, dates, and statistics.
- Design loading, empty, disabled, success, and error states rather than showing a blank area while work is happening.
- Animate feedback when it helps explain an action or confirm a change. Keep motion purposeful, quick, and respectful of reduced-motion preferences.

## Website launch, metadata, and discoverability

For websites and browser-based products, use this as a launch review. Do not add web-only files to projects that do not need them.

- Use the intended production domain when one exists. Do not leave a temporary `vercel.app` address as the public identity of a finished site.
- Check the page source and rendered HTML. Important content should not depend unnecessarily on an empty client-only shell; use server rendering or pre-rendering where it benefits access, performance, and discoverability.
- Build a useful 404 page with a clear way back into the product.
- Verify the actual browser experience and production build, including the project's framework setup (for example, Vite and React when that is the stack). Check more than one modern browser when practical.
- Give each important page its own accurate title and useful meta description.
- Add a suitable Open Graph image so shared links look intentional.
- Add structured data only when it accurately describes the page and follows the relevant schema.
- Use a clear heading hierarchy. Normally, each page should have one main `h1`; do not omit the main heading or add multiple page-level headings without a real reason.
- Set canonical URLs where duplicate or alternate URLs make that useful.
- Consider an `llms.txt` when it would genuinely help people or tools understand a substantial public site or documentation set; do not add it as empty decoration.
- Review `robots.txt intentionally. Do not block AI crawlers by accident; make crawler access a deliberate site policy.
- Include a favicon and appropriate app icons.
- Provide a `sitemap.xml` for sites with indexable pages where it is useful.
- Set the document language correctly with the `lang` attribute.
- Give informative images meaningful alt text. Use empty alt text for purely decorative images so screen readers can skip them.

## Performance and production checks

- Treat source maps deliberately. Keep private maps available for error diagnosis where practical, but do not expose source or sensitive implementation details in production unintentionally.
- Check the browser console and resolve errors, warnings that indicate real problems, and failed network requests before release.
- Inspect production bundle sizes. Split routes or load heavy features on demand, remove unused code, and optimise assets when JavaScript bundles become unnecessarily large.
- Prefer measured improvements over arbitrary size targets or premature optimisation.

## Verification

- Run the narrowest relevant tests first, then broader checks when practical.
- Run the project's formatter, linter, type checker, and tests when they exist.
- Add or update tests when behavior changes.
- Review the final diff for unintended files, generated artifacts, secrets, and unrelated edits.
- State exactly which checks were run and which were not. Never report an unexecuted check as passing.

## Documentation

Update documentation when setup, configuration, public behavior, architecture, or operational procedures change. Record significant architectural decisions in `docs/DECISIONS/`.

## Git hygiene

- Keep commits focused and messages descriptive.
- Do not rewrite shared history or force-push unless explicitly requested.
- Do not commit generated output, local IDE state, or environment-specific files without a project-specific reason.
- Respect the user's requested repository, branch, and pull request. Do not create a new pull request unless asked.

## Using these guidelines

These checks are a way to catch avoidable problems, not a reason to overbuild. Make sensible trade-offs for the project's audience, stack, and scope. Keep the result clear, accessible, fast, secure, and pleasant to use. When a check does not apply, leave it out rather than forcing it in.
