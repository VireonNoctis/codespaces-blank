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

# UI/UX Research Standards — @synsation_

This section distils the public **Build for Good UX** and **Dark Side of UX** series by [@synsation_](https://www.instagram.com/synsation_/) into implementation guidance. Use it as a practical design and engineering reference alongside the standards above. It is a synthesis of public posts and cross-posted captions/transcripts, not a verbatim transcript or a claim that every heuristic is universally valid.

**Research checked:** 12 November 2026

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

## Ethical UX — do not implement dark patterns

The “Dark Side of UX” series is a catalogue of manipulative patterns to recognize and avoid. Do not convert these into growth tactics or product requirements.

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

Research discussed in the series describes how people can apply social expectations to computers and interfaces even when they know they are interacting with software. Button copy can therefore feel like judgment rather than neutral choice.

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

## Research index — Build for Good UX (Parts 1–19)

The table maps the creator's numbered posts to the topics verified in public captions, transcripts, or indexed source pages. Summaries are paraphrases, not quotations.

| Part | Topic | Engineering takeaway | Source |
|---|---|---|---|
| 1 | UI vs UX | Visual polish is not enough; design for predictable actions, trust, and non-happy paths. | [Instagram](https://www.instagram.com/reel/DYIHYJCIAeT/) · [YouTube](https://www.youtube.com/shorts/w90jr50IvKw) |
| 2 | Loading history | Introduces loading states and how waiting experiences evolved. The indexed public caption was available; a full transcript was not retrieved. | [Instagram](https://www.instagram.com/reel/DYXxwf-BZpp/) |
| 3 | Loading patterns | Choose skeleton screens, progress bars, inline spinners, or optimistic UI based on the task. | [Instagram](https://www.instagram.com/reel/DYcbCoiIKK1/) |
| 4 | Spinner psychology | Avoid flashing loaders; contextualize waits and use progress/steps for longer operations. | [Instagram](https://www.instagram.com/reel/DYkRtX1oKKN/) · [YouTube](https://www.youtube.com/shorts/lLL5GcUlpZs) |
| 5 | Error messages | Explain what happened, why when known, and what to do; never expose backend internals or silently fail. | [Instagram](https://www.instagram.com/reel/DYr7cKLIQo6/) · [YouTube](https://www.youtube.com/shorts/_bdeeAKLO6g) |
| 6 | Forms | Make requirements visible, validate inline, prefill known data, show limits/password rules, and accept reasonable formatting. | [Instagram](https://www.instagram.com/reel/DYyzrdpIixM/) · [YouTube](https://www.youtube.com/shorts/lulIaQ41TRA) |
| 7 | Toast vs modal vs inline | Match feedback placement to severity; blocking dialogs need a way forward. | [Instagram](https://www.instagram.com/reel/DY0IImqxNQ0/) · [TikTok](https://www.tiktok.com/@synsation_/video/7657018940891155725) |
| 8 | Empty states | Explain why content is absent and provide a useful first action. | [Instagram](https://www.instagram.com/reel/DY5PkUjyhMv/) |
| 9 | Partial states | Load available content; independent sections should not wait for every other section. | [Instagram](https://www.instagram.com/reel/DY-yUBsMbml/) |
| 10 | Graceful degradation | Give each section its own data, loading, error, and retry behavior. | [Instagram](https://www.instagram.com/reel/DZIHbbIt5mc/) · [YouTube](https://www.youtube.com/shorts/WX5cvNerDm0) |
| 11 | Success states | Confirm meaningful actions clearly; keep small confirmations subtle and proportionate. | [Instagram](https://www.instagram.com/reel/DZYfsYPv1-l/) · [YouTube](https://www.youtube.com/shorts/Ja4bXssAhw8) |
| 12 | Jakob's Law | Users expect familiar patterns based on other products they use. | [Instagram](https://www.instagram.com/reel/DZmMJ_HAHBj/) · [YouTube](https://www.youtube.com/shorts/W6rCWZaADKA) |
| 13 | Jakob's Law continued | Adapt conventions to device, thumb reach, locale, and writing direction. | [Instagram](https://www.instagram.com/reel/DZ-c-4BMXIn/) · [YouTube](https://www.youtube.com/shorts/7nwR9dZgbRA) |
| 14 | Hick's Law | Reduce choice complexity through grouping, filters, and staged decisions. | [Instagram](https://www.instagram.com/reel/DayWu1zy-qz/) · [YouTube](https://www.youtube.com/shorts/ZC9KWn8-kRo) |
| 15 | Progressive disclosure | Reveal what is needed now; make advanced options discoverable without overwhelming users. | [Instagram](https://www.instagram.com/reel/DbFV7_6R8Rn/) · [YouTube](https://www.youtube.com/shorts/BQV0L-JmR4g) |
| 16 | Tesler's Law | Complexity cannot always be removed; the product should absorb avoidable work rather than offload it. | [Instagram](https://www.instagram.com/reel/DbKj0Ewuzlr/) · [YouTube](https://www.youtube.com/shorts/vgzU7UfCJns) |
| 17 | Button states | Default, hover, focus, pressed, loading, and disabled each need intentional behavior. | [Instagram](https://www.instagram.com/reel/DcjkR2PSkml/) · [YouTube](https://www.youtube.com/shorts/SWzFaVOMcK8) |
| 18 | Disabled buttons | Explain why an action is unavailable; consider enabled validation on activation when that is clearer and more accessible. | [Instagram](https://www.instagram.com/reel/DcugS9HAFAj/) |
| 19 | Fitts's Law | Use comfortable hit areas, good spacing, thumb-aware placement, and careful gesture handling. | [Instagram](https://www.instagram.com/reel/Dc2Z_OyBWtc/) · [TikTok](https://www.tiktok.com/@synsation_/video/7681515661906005262) |

## Research index — Dark Side of UX (Parts 1–5)

These posts examine manipulative patterns. The implementation standard is to recognize and avoid them.

| Part | Topic | Avoid | Source |
|---|---|---|---|
| 1 | Roach Motel / cancellation obstruction | Easy signup paired with unusually difficult cancellation or forced offline steps. | [Instagram](https://www.instagram.com/reel/DbbX47eSehN/) |
| 2 | Cancellation friction and loss aversion | Hidden cancellation controls, pause screens that obscure exit, automatic resumption without clear understanding, and pressure based on accumulated history. | [Instagram](https://www.instagram.com/reel/DbeHYe1SvFs/) · [YouTube](https://www.youtube.com/shorts/LtGzZG89v7Y) |
| 3 | Retention offers and confirm-shaming | Exit-survey funnels, repeated bargaining, discounts designed around forgotten renewals, and guilt-based decline copy. | [Instagram](https://www.instagram.com/reel/DboSoFGP5Hw/) · [YouTube](https://www.youtube.com/shorts/ChxDSVvGwSw) |
| 4 | Confirm-shaming and social pressure | Emotionally manipulative decline wording that frames a normal choice as irresponsible. | [Instagram](https://www.instagram.com/reel/Db7OvXgttSp/) |
| 5 | Variable rewards and infinite scroll | Unbounded refresh/recommendation loops designed to remove natural stopping points or exploit attention. | [Instagram](https://www.instagram.com/reel/Dcoiu8ctw-r/) |

## Source and interpretation notes

- Primary profile: [@synsation_ on Instagram](https://www.instagram.com/synsation_/).
- Public cross-posts on YouTube and TikTok were used where available to verify episode titles and spoken guidance.
- Some transcript text was machine-generated or auto-captioned. Minor errors and language mismatches are possible; the principles here are paraphrased.
- Part 2 of Build for Good UX was available through its public caption, but a complete transcript was not retrieved. Its description is intentionally limited to the loading-history introduction stated in the caption.
- Episode numbering alone is not used to infer a topic. Where a caption or full transcript was unavailable, the file records that limitation rather than inventing details.
- Timing thresholds and numerical claims in creator videos are teaching heuristics, not universal standards or independently verified benchmarks. Measure real performance and test with the product's users.
- Apply judgment to the project's audience, stack, platform, accessibility needs, security constraints, and observed behavior.
