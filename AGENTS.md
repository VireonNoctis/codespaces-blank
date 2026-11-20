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
- Review `robots.txt` intentionally. Do not block AI crawlers by accident; make crawler access a deliberate site policy.
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


---

# UI/UX Standards

Use this section as a practical design and engineering reference alongside the standards above. 


## Core product principle: design the experience, not just the screen

- **UI** is the interface people see and manipulate: layout, type, colour, hierarchy, controls, and motion.
- **UX** is the experience of accomplishing a task: predictability, clarity, effort, feedback, recovery, and trust.
- Visual quality cannot compensate for confusing actions, silent failures, unnecessary steps, missing states, or manipulative behavior.
- Design for real people who may be busy, distracted, unfamiliar with the product, using a different device, or experiencing slow networks and partial failures.
- Do not implement only the happy path. A feature is not complete until its relevant loading, empty, error, success, partial, disabled, and recovery states are considered.

## State-first design and implementation

For each meaningful route, data section, form, and interactive control, explicitly consider the states that apply:

| State | Expected experience |
|---|---|
| Initial | Stable structure and clear purpose; no unexplained blank region. |
| Loading | An indicator scoped to the work being performed. |
| Success | A visible or inherent confirmation proportionate to the action. |
| Empty | Explains why content is absent and offers a relevant next action. |
| Partial | Available content remains visible while other sections finish loading. |
| Degraded | Unaffected parts of the product continue to work after a local failure. |
| Error | Human-readable explanation and a practical recovery action. |
| Offline / unavailable | Clearly communicates limitations while preserving context when possible. |
| Disabled | Communicates unavailable interaction and, where not obvious, why. |
| Focus | Clearly identifies the keyboard-focused control. |
| Hover | Optional pointer feedback; never a mobile requirement. |
| Pressed | Confirms that activation was received. |

**Agent requirement:** do not approve a feature based only on its default state or a screenshot. Review state transitions and test the real interaction.

## Loading states — choose the correct experience

Different loading patterns communicate different things. Select one based on scope, known progress, duration, and user expectations.

- **Skeleton screens:** use when a page or substantial region is loading and its eventual layout is known. Preserve the content's rough shape; avoid making the entire app look like an empty page.
- **Progress bars:** use when progress can be measured, such as file uploads, downloads, installations, or long-running processing. Do not fabricate percentages.
- **Inline spinners:** use for small, local operations, such as refreshing one panel or submitting a single control.
- **Optimistic UI:** for safe and reversible actions, show the expected result immediately, reconcile it with the server, and visibly roll it back or explain the failure if it is rejected.
- **No loader:** for very quick actions where a loader would flash briefly and make the interface feel unstable.

### Spinner and wait psychology

The creator uses rough wait thresholds as practical teaching examples: avoid a spinner for a sub-second operation; a plain spinner may communicate a short wait; add contextual status for a growing wait; and switch to measured progress or steps for a long operation. These are **heuristics, not universal timing laws**. Determine actual behavior from measured latency, task context, and user testing.

- Never show an unexplained blank screen for a request that takes noticeable time.
- Do not show a spinner for a request expected to finish before the indicator can communicate anything useful.
- A spinner without context becomes ambiguous as a wait grows. Add truthful status such as “Saving changes” or “Connecting to your account.”
- A looping spinner is not a substitute for progress on a long-running task. Use real progress, a sequence of steps, an honest status, or a cancel action where appropriate.
- A failure should be shown as soon as it is known. Do not leave a user waiting through an arbitrary spinner duration before revealing a failure.
- Keep feedback close to the control or region that initiated the work. Avoid a page-wide blocking loader for a small local operation.

## Error design and recovery

An effective error communicates three things:

1. **What happened** — identify the affected action or resource.
2. **Why it happened** — give the known reason in language the user can understand. Do not invent a cause when it is unknown.
3. **What to do next** — provide a direct action such as retry, correct a field, reconnect, request access, or choose another payment method.

Avoid both of these extremes:
- Never expose raw database errors, stack traces, SQL, internal service names, tokens, file paths, or backend logic in the user interface. It is confusing and may disclose sensitive implementation details.
- Do not replace every issue with an unhelpful “Something went wrong.” Be specific about the consequence and next step without leaking internals.

A **silent failure** is unacceptable. When someone activates Save, Pay, Submit, Upload, or Delete, the interface must not leave them wondering whether the operation succeeded.

### Put errors in the right place

- **Inline errors:** default for a specific field or local control. Put the message close to the thing that needs correction.
- **Toast notifications:** use for low-severity, non-blocking status that may safely disappear. Do not put a critical error only in a transient toast.
- **Modal / blocking dialog:** use sparingly when the user genuinely cannot continue without addressing the issue. Explain the problem and offer a clear way forward; never block without an actionable choice.

After a form fails, preserve valid input, identify the first correction needed, and move focus or scroll the user to it. After a local save fails, put the retry action near the Save control.

Additional requirements:
- Distinguish validation, permission, network, missing-resource, conflict, rate-limit, and unexpected server failures.
- Make retries safe; prevent duplicate financial or destructive actions.
- Keep diagnostic detail in secure logs, not in user-facing messages.
- Do not claim success until there is a trustworthy confirmation.
- Preserve the context that helps a person recover.

## Form design — remove avoidable frustration

Forms should explain their requirements before the user reaches the end.

- Clearly mark required and optional fields.
- If submission is unavailable, tell the user what is missing. A disabled button with no explanation is not sufficient.
- Validate inline at an appropriate time. Do not make users complete a long form and then scroll to the top to find an error.
- Preserve entered values and direct the user to the first field that needs attention.
- Show character limits and remaining characters as the user types when a limit matters.
- Prefill information the product already knows and is permitted to use. Do not ask for the same information twice without a reason.
- Show password requirements before submission and indicate which are satisfied while typing.
- Accept reasonable input formatting when safe (for example, spaces, dashes, and parentheses in phone numbers) and normalize it consistently at the system boundary.
- Use appropriate input types, labels, autocomplete metadata, and programmatic validation.
- Explain why information is needed when its purpose is not obvious.

### Disabled form submission

A disabled submit button can prevent invalid input, but it can also make users guess what is missing and can make requirements less discoverable.

Consider an enabled submit button that validates on activation: show exactly which fields need attention, focus the first one, and preserve the rest of the form. A disabled button is reasonable when the unavailable state is obvious or while preventing duplicate requests during an active submission. When using it, explain the requirement accessibly; never rely only on grey colour.

## Empty states — the first impression may be an empty screen

An empty state should not look like a broken product. It should answer:

- Why is this area empty?
- What is this area for?
- What can the user do next?

Examples:
- Empty dashboard → explain the value of the area and offer “Create your first project.”
- Empty collection or section → describe what belongs there and how to add it.
- No search results → show the query and suggest useful changes to the query or filters.
- A deliberately empty goal state (such as a cleared inbox) → acknowledge the achievement with restrained feedback.

Do not add decorative filler just to occupy space. Give users a meaningful next step without making the empty screen noisy.

## Partial states and graceful degradation

A page may look like one screen while its data comes from several independent services. Each region may load or fail at a different time.

- Each independently data-owning section should manage its own request, loading state, error state, and retry behavior.
- Render available content as soon as it is ready. Do not make the whole page wait for unrelated data.
- If one section fails, show a local error and retry action. Keep healthy sections usable.
- Avoid a single page-level failure boundary that erases all content when one independent panel fails.
- When appropriate, show cached or stale content while fresh data loads in the background. Indicate freshness when it matters and replace old data carefully.
- Keep transitions between cached, loading, refreshed, and failed states understandable.
- If a feature genuinely depends on multiple services, make that dependency and its status clear.

**Practical test:** if a profile loads but the activity feed fails, can the user still use the profile? If one dashboard chart fails, can the other panels remain useful?

## Success states — confirm that an action worked

Every meaningful action needs a trustworthy result.

- Confirm payments, bookings, uploads, account changes, and destructive operations clearly enough that the user knows what happened.
- For high-impact operations, show a confirmation appropriate to the consequence, including a useful reference or next step where relevant.
- For small interactions, the changed object may itself be the confirmation: a card moving into “Done,” a liked state changing, or a saved item appearing in its destination.
- Reserve confetti and large celebration screens for genuinely meaningful milestones. Do not celebrate every minor click.
- Prevent duplicate submission while a request is in progress.
- For optimistic actions, reconcile the local state with the final result and explain a rollback when necessary.

## Familiarity and decision-making

Use design laws as thinking tools, not as rigid rules or excuses to copy competitors.

### Jakob's Law — respect established expectations

People spend much of their time in other products and bring expectations to yours. Familiar controls and placements reduce unnecessary thought.

- Keep common controls, navigation, and information architecture predictable unless changing them offers a clear user benefit.
- Be consistent within the product, but do not blindly copy another product.
- Adapt patterns to the platform: a desktop shopping cart may be expected at the top-right, while a mobile cart may need to be thumb-reachable near the bottom.
- Account for localization and writing direction. A right-to-left experience may require mirrored layout and placement, not merely translated strings.
- Preserve the user's ability to find important functions without relearning the interface.

### Hick's Law — reduce decision complexity

Decision time can grow with the number and complexity of available choices.

- Group related options and establish a clear hierarchy.
- Use sensible defaults, search, filtering, and recommendations for large catalogs.
- Break complex tasks into manageable decisions when this reduces cognitive load.
- Do not remove useful choices merely to make the screen appear minimal.
- Make choices easier to compare and understand.

### Progressive disclosure — reveal complexity at the right moment

Show users what is relevant now and reveal additional controls when they become useful.

- Keep the primary action and essential information visible.
- Reveal advanced settings contextually or on demand, using familiar affordances.
- Use search or command menus when they reduce clutter without hiding core capabilities.
- Do not bury important features so deeply that users need a tutorial to find them.
- Progressive disclosure sequences capabilities; it does not remove them.

### Tesler's Law — take on complexity the system can handle

Some task complexity is inherent; the product can decide how much work falls on the user versus the system.

- Automate repetitive transformations and predictable edge cases safely.
- Use available context and sensible defaults to avoid making users repeat work.
- Do not offload engineering shortcuts, internal terminology, or avoidable configuration burden onto people.
- Do not hide complexity in ways that make behavior unpredictable or uncontrollable.
- Remember that real people are busy and distracted; design for a reasonable human, not an endlessly patient expert.

## Fitts's Law — comfortable targets and touch behavior

Targets are easier to select when their hit area is large enough and they are close to the user's current pointer or finger.

- Give controls comfortable hit areas, not merely visually large icons.
- Use padding around small icons when it does not overlap neighboring controls.
- Make an associated checkbox or radio label clickable when this improves selection.
- If an entire card is clickable, give it one clear destination and keep nested controls independently operable.
- Place frequent mobile actions within comfortable reach when appropriate to the information architecture.
- Space adjacent targets to reduce accidental activation.
- Ensure scrolling is not interpreted as tapping a card. Larger hit areas must not introduce gesture conflicts.
- Test on a physical device, not only in a desktop browser or emulator.

## Button states — implement the whole interaction

Every interactive button has a state model. The series describes six useful states:

1. **Default:** looks actionable and has clear visual hierarchy.
2. **Hover:** optional pointer feedback on hover-capable devices; do not make mobile behavior depend on hover.
3. **Focus:** visible focus indication for keyboard navigation and accessibility.
4. **Pressed:** immediate visual or tactile acknowledgment that activation was received.
5. **Loading:** communicates that work has started, preferably near or inside the activated control; prevents duplicate activation.
6. **Disabled:** indicates unavailability, with a reason when it would not otherwise be obvious.

Also:
- Use semantic buttons for actions and links for navigation.
- Support keyboard activation and logical focus order.
- Provide accessible names and announce meaningful state changes to assistive technology.
- Never communicate a state through colour alone.
- Avoid layout shifts when state changes.
- Respect reduced-motion preferences and keep motion purposeful.

### Cancellation obstruction / “Roach Motel”

A pattern where joining is easy but leaving is unusually difficult.

- Do not hide cancellation behind nested menus, obscure links, repeated screens, forced calls, or postal steps when an online cancellation path is offered at signup.
- Keep cancellation in a predictable, accessible place.
- Do not make the exit path materially harder than the entry path.

### Friction, pause screens, and loss aversion

Adding obstacles can exploit low motivation at the moment a user tries to leave.

- Do not make pause or “stay” visually dominant while making “continue to cancel” tiny or hard to discover.
- Do not automatically resume billing after a pause without clear terms, notice, and user understanding.
- Do not use playlists, activity histories, streaks, accumulated data, or other personal history to pressure users into staying.
- A user's cancellation decision must not depend on outlasting their patience.

### Retention offers, exit surveys, and confirm-shaming

- Do not turn an exit survey into a disguised sequence of retention offers.
- Do not repeatedly bargain after a user has clearly declined.
- Do not present short-term discounts in a way designed to exploit forgotten renewals or obscure future pricing.
- Never use guilt-inducing decline copy such as “No, I hate saving money.”
- Do not frame a normal choice as irresponsible or socially unacceptable.

### Social pressure and emotional manipulation


- Keep decline choices neutral, direct, and respectful.
- Do not manufacture guilt, shame, fear, or social pressure to influence an optional decision.
- Avoid misleading insurance, scarcity, risk, or consequence language.
- Respect reactance: manipulative pressure can erode trust and produce resentment.

### Variable rewards, refresh loops, and infinite scroll

Pull-to-refresh and infinite scroll can be useful patterns. They become harmful when deliberately designed to remove stopping points and exploit unpredictable rewards to maximize attention.

- Do not optimize solely for time-on-site or compulsive engagement.
- Provide meaningful stopping points and user control over autoplay, notifications, and recommendations.
- Keep refresh actions intentional and useful.
- Make it possible to pause, leave, or finish without being pulled into an endless sequence.
- Treat recommendation systems as product features that require user-benefit review, not as automatic justification for attention capture.

**Ethical requirement:** build for user outcomes, transparency, and long-term trust rather than short-term conversion at the user's expense.

## AI-assisted UI implementation

AI-generated interfaces frequently concentrate on the ideal state and omit operational behavior. When delegating design or implementation to an agent:

- Explicitly request the relevant loading, empty, error, success, partial, offline, disabled, focus, hover, and pressed states.
- Specify realistic cases: invalid input, timeouts, partial API failure, expired sessions, permission denial, duplicate clicks, stale data, and network interruption.
- Inspect behavior rather than trusting a polished screenshot.
- Verify that user-facing errors do not expose backend details.
- Verify that controls work; decorative or inert controls are not complete features.
- Keep state ownership and recovery paths local to independent components.
- Test keyboard and screen-reader behavior, touch interactions, slow connections, and real devices.
- Never fabricate progress, report success before confirmation, or hide missing behavior behind animation.

## UX completion checklist

Before marking a feature complete, check the items that apply:

- [ ] The primary task and next action are understandable without extensive instructions.
- [ ] Loading, success, empty, error, partial, and disabled states have been considered.
- [ ] A failure in one independent section does not break unrelated sections.
- [ ] Important actions receive immediate feedback and a trustworthy result.
- [ ] Errors explain the consequence and offer a useful recovery action.
- [ ] No raw backend, database, stack trace, secret, or internal identifier is exposed.
- [ ] Forms explain requirements, validate clearly, preserve input, and avoid repetition.
- [ ] Long operations show truthful status or measurable progress.
- [ ] Optimistic UI can be safely reconciled or rolled back.
- [ ] Blocking dialogs are rare and provide a way forward.
- [ ] Keyboard focus is visible; interactions work without a pointer.
- [ ] Accessible names, roles, and state announcements are present.
- [ ] Touch targets are comfortable and do not trigger accidentally while scrolling.
- [ ] Device-specific and RTL/localized conventions are considered where relevant.
- [ ] Motion is purposeful and respects reduced-motion preferences.
- [ ] No cancellation, retention, shame, or attention-capture dark pattern has been added.
- [ ] The feature has been tested with slow connections and realistic failure cases.


---

## Structural Untangling Protocol — Untangle Codebase

Use this protocol when the user explicitly asks to untangle, structurally refactor, or comprehensively redesign the codebase. Treat it as a complete goal, not a superficial cleanup. When invoked, inspect and improve the whole relevant codebase, finish the work, and preserve intended behavior except for bugs corrected by the structural redesign. This protocol does not expand ordinary feature or bug-fix requests into unsolicited whole-repository refactors.

### 1. Ask about optional additions

Besides untangling the codebase, the user may choose either or both of these additions. Present the options with these exact descriptions and ask which to include before starting an untangling run:

| Addition | Exact description |
|---|---|
| **Comments** | Remove comments that only restate the code. |
| **Tests** | Remove tests that wouldn't catch a real bug, and fix the ones that fail without one. |

Do only the additions the user chooses. If an addition is not selected, do not perform that category of cleanup as part of the untangling work. The structural redesign and the regression verification needed to protect it remain part of the core task.

### 2. List every structural problem before changing anything

Do not edit code during the initial audit. Walk the whole codebase and ask one question of every relevant relationship:

**Should these pieces change together?**

Record every place where the current design answers that question incorrectly. There are three problem classes:

#### Hidden links — pieces that must change together, but the code does not make that relationship visible

Look for:

- **Copied logic or values:** changing one copy means the others must change too, but there is no explicit shared source or relationship.
- **Hidden shared state:** a module reads a global or a file that another module sets or mutates, so changing the producer can silently break the consumer.
- **Scattered features:** one feature is split across folders by technical layer, or related code is separated across unrelated locations, so a normal feature change requires edits in multiple places.
- **Implicit call order or conventions:** callers must know an undocumented sequence, side effect, or convention for the code to work.

#### Needless links — pieces are coupled even though they change for different reasons

Look for:

- **Leaky encapsulation:** callers depend on implementation details and break when internals change.
- **Wrong dependency direction:** stable code imports more volatile code and must change whenever that volatile implementation changes.
- **Caller-specific vocabulary:** a general function has a parameter or branch that only one workflow understands, coupling the general abstraction to that caller.
- **Shallow modules:** a module's interface changes whenever its implementation changes, forcing callers to change for internal reasons.

#### Surplus — pieces with no independent reason to change

Look for:

- **Pass-through wrappers:** wrappers that only change when the thing they wrap changes.
- **Speculative generality:** extension points, configuration, or abstractions for behavior that does not and is not expected to vary.
- **Dead code:** code that has no callers or other real use and therefore has no reason to change.

#### Record every special case

A special case is code that exists for one situation rather than following naturally from the system's general rules. Treat each one as evidence of a requirement the design may not have accounted for. Inspect at least:

- An if branch for one particular value.
- A parameter that exists for one specific caller.
- A swallowed or ignored exception.
- A retry, arbitrary sleep, or timing workaround.
- A disabled test.

Do not automatically delete every special case. Determine whether the redesign makes it unnecessary or whether it represents a real requirement that the system must continue to support.

For every finding, record the file and location, the behavior or relationship involved, why the current design is wrong, and the other places that are coupled to it. Be exhaustive before implementation; do not start fixing the first issue as soon as it is found.

### 3. Redesign from first principles

Work out how the system would have been designed if it had understood today's actual requirements from the beginning.

- Search for one underlying design fix that resolves several symptoms. Prefer correcting the structural cause over adding local patches for each symptom.
- Place code that changes together together; keep independently changing code separate.
- Make dependencies point toward the parts of the system that change less.
- Give modules cohesive responsibilities and interfaces that hide volatile implementation details.
- Make important relationships explicit rather than relying on duplicated values, hidden state, caller knowledge, or call order.
- Re-evaluate every proposed fix—even one that appears cleaner—to ensure it improves the change boundaries rather than merely moving complexity elsewhere.
- Keep intended external behavior, public contracts, data compatibility, security properties, and operational requirements intact unless a deliberate behavior change is part of the request.

Maintain a decision log. Write each proposed structural fix first, followed by the complete set of problems it solves. Do not write a list of unrelated edits; make the relationship between the redesign and its evidence explicit.

Use this format:

> Proposed structural fix: [one coherent design change]
>
> - Problem it solves: [file/path and concrete issue]
> - Problem it solves: [file/path and concrete issue]
> - Problem it solves: [file/path and concrete issue]

### 4. Fix everything on the decision log

Implement the redesigned structure across all listed locations. Do not stop after fixing the easiest symptoms.

- Remove special cases that the redesign makes unnecessary.
- Preserve special cases that still express real requirements, and make their purpose and boundary clear.
- Prefer one coherent structural correction over a set of one-off conditionals, flags, wrappers, retries, or duplicate implementations.
- Keep the refactor aligned with current repository architecture, language, dependencies, runtime constraints, security requirements, and compatibility obligations.
- Do not introduce speculative frameworks, extension points, or abstractions as a side effect of making the design appear more general.
- Do not silently broaden the scope into unrelated product features or behavior changes.

If the user selected **Comments**, apply these rules:

- Remove comments that merely restate what the code does, including comments phrased as a rationale when the rationale is fully evident from the implementation.
- Keep comments documenting facts outside the code that the code itself cannot express, such as an external service limitation or platform behavior.
- Remove comments that explain workarounds when the redesign removes the underlying problem; retain them only when the workaround remains necessary and its reason is not otherwise evident.

If the user selected **Tests**, do this after the structural implementation, because tests are the regression safety net:

- Remove tests that merely repeat the implementation's own logic or interpretation rather than checking observable behavior.
- Rewrite tests coupled to private implementation details so they verify stable behavior and contracts instead.
- Remove tests that cannot fail for a meaningful regression and therefore do not verify anything.
- Fix genuinely failing tests when the failure does not represent a real product bug, while preserving tests that expose regressions.
- Keep useful regression coverage. Do not weaken the suite merely to obtain a green result.

### 5. Check and repeat until done

After the first implementation pass, independently audit the resulting codebase again for:

- Hidden links.
- Needless links.
- Surplus code and abstractions.
- Special cases that remain.
- Dependencies and import direction.
- Features still scattered across unrelated locations.
- Callers that still need to know implementation details or undocumented conventions.

Use subagents to inspect separate areas and independently search for these problems. Compare their findings, resolve disagreements against the actual code and behavior, and update the decision log. If subagents are unavailable, perform separate independent audit passes and state that limitation; do not claim parallel review that did not occur.

Generate or inspect dependency graphs where useful, and rerun them after significant changes. Use repository history and Git evidence to identify files that repeatedly change together. Test the redesigned behavior, not merely the new implementation shape.

**Do not stop while worthwhile structural problems remain.** Repeat the audit, decision-log, redesign, implementation, and verification cycle until the completion criteria below are satisfied.

The work is complete when:

- As few special cases remain as the actual requirements allow; the remaining count and reasons are understood.
- A typical change can be made in one obvious place.
- Imports and dependencies are reasonable, and stable code does not depend on more volatile implementation details.
- Related code is grouped around the behavior that changes together.
- Independent code is no longer needlessly coupled.
- Subagent reviews, or equivalent independent audits when subagents are unavailable, have no unresolved worthwhile structural findings.
- Intended behavior remains the same, apart from bugs the structural redesign corrected.
- Relevant tests and checks have been run, and limitations are explicitly reported.
- The final diff contains only intentional changes.

### Untangling techniques

- **Start from a skeleton:** where useful, temporarily reason from function signatures, module boundaries, and dependency structure before reading every implementation detail.
- **Summarize by area:** use subagents or independent passes to summarize separate parts of the codebase, then reason across the whole system.
- **Inspect dependency graphs often:** generate or review a graph of what imports what, and revisit it after structural changes.
- **Start where leverage is highest:** investigate the area whose structural correction is likely to remove the most coupling or repeated work.
- **Keep the decision log:** it preserves the connection between evidence, redesign, and implementation across long tasks and context changes.
- **Use Git as evidence:** review file co-change history and repeated patterns rather than relying only on intuition.

The governing principle is that this is a redesign of change boundaries: pieces that change together should be together, pieces that change for different reasons should not be tied together, and everything should depend on what changes less.


---

## Evidence-Led Folder Architecture and Repository Organization

Folder structure is part of the architecture: it should make ownership, dependencies, runtime boundaries, and change-together relationships obvious. Do not choose a layout because it is fashionable or copy another repository wholesale. Choose it from the project's actual requirements and verified code.

This section is mandatory before a substantial folder reorganization, a new large feature area, a new service/package, or an Untangle Codebase run. Apply the same reasoning to small changes when deciding where new files belong.

### 1. Inspect the real repository before proposing a structure

Before moving or creating folders:

1. Inspect the complete tracked file tree and identify the repository's actual top-level boundaries. Inspect enough depth to understand the ownership of important files; do not rely only on a short root listing.
2. Read the entry points, representative files, package/workspace manifests, build configuration, tests, and relevant documentation. Folder names alone do not prove what a module does.
3. Trace imports, calls, shared state, data ownership, runtime processes, build/deploy units, and test coverage. Generate or inspect a dependency graph when it can reveal hidden coupling.
4. Use Git history and co-change evidence where available to identify files that repeatedly change together.
5. Separate production code, test code, generated output, static assets, operational scripts, infrastructure, migrations, and documentation according to their actual purpose.
6. Record the current structure and its problems before changing anything. Do not start a broad move while the ownership and dependency map is still unclear.

Every proposed directory must have a clear responsibility. Every moved file must have an explicit destination and reason. Avoid moving files merely to make the tree look tidy.

### 2. Benchmark mature repositories with relevant architecture

Research real, actively maintained, substantial projects that use a comparable language, framework, deployment model, or engineering problem. Inspect their actual repository trees, manifests, and representative code. Use examples as evidence for a decision, not as templates to copy.

The following repositories are useful verified reference points:

| Project | Observed organization | Useful lesson |
|---|---|---|
| [Vercel / Next.js](https://github.com/vercel/next.js) | Separates apps/, packages/, Rust crates/, docs/, examples/, benchmarks, scripts, and tests. | Different deployable apps, reusable packages, language-specific workspace crates, and supporting material have explicit boundaries. |
| [Supabase](https://github.com/supabase/supabase) | Uses apps/, packages/, e2e/, examples/, and supabase/ for database functions and migrations. | Product applications, shared libraries, end-to-end coverage, examples, and database platform assets should not be mixed into one source folder. |
| [Visual Studio Code](https://github.com/microsoft/vscode) | Separates core src/, independently organized extensions/, cli/, remote/, build/, and tests. | Large products benefit from strong product/runtime/extension boundaries rather than a single undifferentiated components or utilities directory. |
| [Django](https://github.com/django/django) | Groups framework capabilities under django/ (for example db/, forms/, http/, middleware/, views/) and maintains broad behavior-oriented tests/ suites. | Stable domain capabilities deserve clear modules; tests can mirror externally observable capabilities rather than private file layouts. |
| [Axum](https://github.com/tokio-rs/axum) | Separates Rust crates such as axum/, axum-core/, axum-extra/, and axum-macros/, with crate-specific source/tests/benches and standalone examples. | Split a Rust workspace into crates when the API, dependency, release, or ownership boundary is real—not merely to create more folders. |

Benchmarking rules:

- Prefer primary repository trees, manifests, and source over blog-post folder diagrams.
- Check the project's current branch and current layout; repository architecture can change.
- Choose examples that solve a comparable problem. A framework monorepo, a desktop application, and a small single-app project should not be treated as interchangeable.
- Identify the principle behind a pattern and adapt it to this codebase's scale, runtime, team, and deployment model.
- Do not add apps/, packages/, crates/, microservices, or layers unless there is a real boundary that justifies them.
- Do not claim that a reference project uses a pattern unless its tree or implementation has been inspected.

### 3. Use GoodSale and LOOP as first-party folder-organization references

The user's own repositories are additional concrete references. Inspect their current trees and relevant source before using them; these observations describe the inspected layouts, not a requirement to duplicate every directory.

#### GoodSale — VireonNoctis/GoodSale

Observed root-level organization:

- app/ — Next.js App Router pages, route groups, layouts, loading/error states, metadata, and API route handlers.
- components/ — reusable interface components grouped in areas such as admin/, auth/, checkout/, marketplace/, onboarding/, premium/, seller/, tracking/, verification/, wallet/, and shared ui/.
- lib/ — non-route application logic and capabilities grouped in areas such as auth/, business/, delivery/, logistics/, marketplace/, payments/, shipping/, wallet/, referrals/, seo/, and supabase/.
- supabase/ — schema and ordered database migrations.
- tests/ — behavior-oriented test groups such as business, chat, data, payments, premium, referrals, and seed.
- docs/, scripts/, public/, and .github/ — documentation, operational/verification tooling, public assets, and automation.

Patterns to carry forward where appropriate:

- Keep framework-required routes and handlers in app/, but keep substantial domain logic out of route files. Route handlers should validate/translate the HTTP boundary and delegate to the owning domain/service module.
- Group feature UI by product capability; keep generic primitives in components/ui/.
- Group business logic by capability instead of placing unrelated functions in one global helper file.
- Keep schema and ordered database migrations in the database platform's established migration area.
- Organize tests around behavior/capability, not a one-to-one copy of internal source filenames.

Audit caveat: GoodSale also has a number of top-level component files and capability files directly under lib/. Treat those flatter areas as candidates to evaluate when related files begin changing together; do not bulk-move them without evidence or a coherent ownership boundary.

#### LOOP — VireonNoctis/loop-app

Observed root-level organization:

- app/ — Next.js App Router pages and API routes, including product areas such as chains, circles, communities, co-loop, creator, messages, profiles, quests, shop, and wallet.
- components/ — feature-oriented interface areas such as accounts, admin, chat, circles, communities, marketplace, onboarding, profile, reels, settings, shop, streams, team, verification, and shared ui/.
- backend/ — a separate Rust service boundary, with its own Cargo.toml, src/, route and storage modules, configuration, Docker setup, and migrations/.
- hooks/ and providers/ — shared React hooks and application providers.
- lib/ — application/domain capabilities and integrations, including auth, circles, communities, discovery, moderation, notifications, payments, privacy, quests, realtime, theming, verification, and the Rust API client.
- android/ — native Android project and platform resources.
- infra/, assets/, styles/, public/, scripts/, __tests__/, docs/, and licenses/ — deployment/infrastructure, static assets, styling, operational tooling, tests, documentation, and legal material.

Patterns to carry forward where appropriate:

- Preserve clear runtime boundaries: Next.js application, separately runnable Rust backend, and Android native project should remain distinguishable.
- Keep frontend routes in the framework's app/ structure, and keep Rust-specific source, manifests, tests, and migrations inside the backend boundary.
- Group components around product domains and keep generic design-system primitives in components/ui/.
- Keep truly cross-feature React hooks in hooks/ and app-wide providers in providers/; feature-only hooks/providers may be colocated with their owning feature when that makes ownership clearer.
- Put infrastructure and native platform assets under their own boundaries rather than mixing them with application logic.
- Keep domain capabilities identifiable. When lib/ grows into a large flat collection, assess cohesive groups such as auth/, circles/, community/, payments/, notifications/, moderation/, and theming/; consolidate only where import and change-together evidence supports it.

Audit caveat: LOOP's current lib/ contains many root-level capability files, and scripts/ contains a substantial mix of migrations, schema changes, repair scripts, seeds, and verification utilities. Treat these as opportunities for an evidence-led organization review, not proof that every script or helper must be moved immediately. Keep one canonical home for each migration and script; do not duplicate SQL or change execution order while organizing it.

Use these two repositories as first-party examples of how the user separates routes, feature UI, domain logic, backend/runtime boundaries, tests, migrations, infrastructure, and documentation. Do not assume they are perfectly organized or copy their existing rough edges into another project.

### 4. Select the folder model from actual change and deployment boundaries

Use these principles to design the target tree:

- **Separate deployables first.** Use top-level apps/ for multiple independently built/deployed applications, services/ or a clearly named backend boundary for independently run services, and platform folders such as android/ for native projects. In a Rust workspace, use crates/ or named crate directories when crate boundaries are real. A single application does not need a monorepo structure just because large repositories use one.
- **Separate reusable packages from applications.** In a genuine monorepo, packages/ or language-appropriate workspace members should contain independently reusable libraries, UI systems, configuration, clients, or domain packages. Applications consume shared packages through public interfaces; one app must not reach into another app's private source tree.
- **Organize product logic by capability.** Prefer cohesive domains such as auth/, billing/, catalog/, chat/, community/, delivery/, or payments/ when the code in each area changes together. Avoid a generic misc/ or a huge utils/ directory that hides ownership.
- **Respect framework conventions.** Keep framework-mandated route, page, layout, middleware, and handler files where the framework expects them. Use these files as thin entry points; place substantial domain behavior in the owning feature/service modules.
- **Group UI by responsibility.** Feature-specific components belong with their feature or in a feature-grouped components tree. Generic controls, primitives, and design-system elements belong in a shared UI layer. A shared component must not import a feature's private implementation.
- **Keep integrations at the boundary.** Provider/API clients, persistence adapters, storage, email, payment gateways, and external-system integrations should have explicit boundaries. Domain rules should not be coupled to vendor-specific transport or SDK details without a reason.
- **Use hooks/, providers/, and state/ deliberately.** They should contain genuinely shared cross-feature behavior. Feature-only state and hooks should normally stay with the feature that owns them.
- **Keep data ownership explicit.** Put migrations, schemas, seeds, and persistence-specific code in one clear location per data store/runtime. Separate migration history from disposable scripts and verification utilities; never create a second canonical migration directory.
- **Give tests a deliberate shape.** Choose either useful colocation or a central tests/ tree based on the existing test tooling. Distinguish unit, integration, contract, and end-to-end tests, and group them around behavior or domain. Keep fixtures and test helpers discoverable. Avoid testing only private folder structure.
- **Separate operations from source.** Keep deployment manifests, infrastructure-as-code, container configuration, CI workflows, developer scripts, data migrations, and generated build output distinguishable. Do not put generated output into source folders.
- **Make documentation discoverable.** Keep architecture decisions, runbooks, setup, API contracts, and feature guidance in predictable locations. Avoid duplicate or contradictory instructions scattered across folders.
- **Keep naming consistent.** Follow the repository's established casing and naming convention. Use clear lowercase names where the project already does so; do not rename large areas just to impose a new style.
- **Create a folder only when it earns its existence.** Do not add empty directories, one-file abstraction layers, or deeply nested structures that make navigation harder without improving ownership.

### 5. Prefer cohesive feature slices without violating runtime boundaries

A feature slice should make it easy to find the code that changes together. Depending on the framework and scale, a feature may own:

- Its public entry point or route adapter (where framework rules allow).
- UI components and feature-only hooks/state.
- Domain rules and application services.
- Persistence/provider interfaces or adapters where the feature owns them.
- Types, validation schemas, and feature-specific tests.
- Documentation for non-obvious behavior and invariants.

Do not force every feature into an identical folder template. A small feature may need one module; a mature domain may need clear domain/, application/, infrastructure/, and presentation/ boundaries. Add those layers only when they separate genuine responsibilities and change rates. Avoid deep ceremonial architecture for simple code.

### 6. Validate a folder reorganization as an architectural change

Before moving files, produce:

1. A current-tree summary and relevant dependency map.
2. A list of the identified ownership/coupling problems.
3. The target tree, with a reason for each new boundary.
4. An old-path → new-path move map.
5. A dependency-direction plan, including public interfaces and import-alias changes.
6. A test/build/documentation/configuration impact list.

After moving files:

- Update imports, aliases, manifests, code-generation paths, scripts, CI references, Docker/build contexts, deployment commands, test discovery, documentation links, and editor/tool configuration.
- Search for stale old paths, dynamic imports, case-sensitive path mismatches, generated references, and string-based file lookups.
- Verify there is one canonical implementation, migration history, schema source, or configuration owner; do not leave duplicate copies.
- Run formatter, lint, typecheck, unit/integration/e2e tests, build, and relevant packaging/deployment checks where configured and feasible.
- Inspect the final tree and dependency graph again. Confirm the new layout makes likely changes easier to locate and does not create new cross-feature imports or dependency cycles.
- Preserve runtime behavior and public import/API contracts, or provide deliberate compatibility shims when a breaking change is authorized.
- Report the exact moves, the structural reason, checks run, and checks not run.

Do not perform broad folder moves as incidental cleanup during an unrelated task. When a folder refactor is explicitly requested, complete the structural work coherently rather than stopping after creating the target folders.
