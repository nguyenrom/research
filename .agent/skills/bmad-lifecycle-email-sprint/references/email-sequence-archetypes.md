# Lifecycle Email Sequence Archetypes

> Reference loaded by `bmad-lifecycle-email-sprint` Phase 2 (Sequence Architecture) and Phase 3 (Copy Production). Concrete archetypes for welcome, nurture, activation, dunning, churn save, win-back, and cold outbound — with cadence, message strategy per touch, exit conditions.

## The 7 archetypes

| Archetype | Trigger | Length | Goal | Exit |
|-----------|---------|--------|------|------|
| Welcome | Signup | 3-5 emails | Activation | First key action completed |
| Nurture | Lead form (no signup yet) | 5-7 emails | Move to signup | Signup OR explicit unsubscribe |
| Activation / Onboarding | Signup with no activation in 7d | 3-4 emails | Drive aha moment | Aha moment reached OR cancel |
| Dunning | Failed payment | 4-5 emails over 21d | Recover payment | Payment recovered OR voluntary cancel |
| Churn save | Cancellation flow entered | 1-2 emails | Reduce voluntary churn | Cancel confirmed OR retain |
| Win-back | 30+ days post-cancel | 3 emails over 4 weeks | Re-engage churned user | Reactivate OR final unsubscribe |
| Cold outbound | New target account, no prior contact | 4-6 emails over 21d | Book a meeting | Reply (yes/no) OR breakup |

## 1. Welcome sequence (3-5 emails)

| # | Day | Subject formula | Body job |
|---|-----|-----------------|----------|
| 1 | 0 | "[First name], welcome to [Product] 👋" | Confirm signup; first key action CTA |
| 2 | 1-2 | "The 3 things [Product] users do first" | Reduce overwhelm; pick 1 of 3 |
| 3 | 3-5 | "How [Customer X] got [outcome] in [timeframe]" | Social proof + tactical |
| 4 | 7 | "Quick check: did [first key action] work for you?" | Activation reinforcement |
| 5 | 10-14 | Conditional: trial-to-paid OR feature deep-dive | Branch by status |

**Voice**: founder-friendly, not corporate. First-name greeting. Plain text feel even when HTML.

## 2. Nurture sequence (5-7 emails, lead → signup)

| # | Day | Subject | Job |
|---|-----|---------|-----|
| 1 | 0 | "Your [resource]" | Deliver what they signed up for |
| 2 | 2 | "Why [pain point] gets worse if you don't [thing]" | Amplify problem awareness |
| 3 | 5 | "How [customer type] solves [problem]" | Show solution patterns (not your product yet) |
| 4 | 8 | "We built [Product] for [persona] who [pain]" | Bridge to product |
| 5 | 12 | "Customer story: [Customer X] → [outcome]" | Social proof |
| 6 | 15 | "Common questions about [Product]" | Address objections inline |
| 7 | 21 | "Last email: free trial?" | Direct ask + soft unsubscribe |

**Rule**: emails 1-3 must add value WITHOUT pitching. Emails 4-7 introduce product progressively.

## 3. Activation / Onboarding sequence (3-4 emails)

Triggered when user signed up but did NOT reach aha moment by Day 7.

| # | Day | Subject | Job |
|---|-----|---------|-----|
| 1 | 7 | "[Name], stuck somewhere?" | Diagnose: ask which step blocked |
| 2 | 9 | "Watch how [Customer X] uses [Product]" | Show, not tell (video < 90s) |
| 3 | 12 | "1-on-1 setup call?" | Personal help offer (high-value users only) |
| 4 | 14 | "Last reminder: your trial ends [date]" | Trial expiration trigger |

**Aha moment** = pre-defined behavior (e.g. "first project created with 3+ collaborators"). Pull from `marketing-context.md` Section 12 (Goals & current metrics).

## 4. Dunning sequence (4-5 emails over 21 days)

Triggered by failed payment (Stripe webhook).

| # | Day | Subject | Job |
|---|-----|---------|-----|
| 1 | 0 | "Quick payment issue with your [Product] account" | Notify, soft tone, retry CTA |
| 2 | 3 | "Action needed: update your payment" | Direct, retry CTA |
| 3 | 7 | "[Name], can we help?" | Personal voice, alternative contact |
| 4 | 14 | "Final notice: account pauses in 7 days" | Urgency, retry CTA |
| 5 | 21 | "Your account is paused" | Confirms downgrade, easy reactivation |

**Smart retry timing**: payment retries happen at days 1, 3, 5, 7 (not the email cadence — these are processor retries). Coordinate with Stripe / Recurly settings.

**Recovery benchmark**: soft fail (insufficient funds) = 70%+ recovery; hard fail (card cancelled) = 40%+.

## 5. Churn save sequence (1-2 emails)

Triggered when user clicks "Cancel" but hasn't confirmed.

| # | When | Subject | Job |
|---|------|---------|-----|
| 1 | Mid-flow (in-product) | "Before you go..." | In-product save offer (pause, downgrade, discount) |
| 2 | 1 day after cancel | "[Name], anything we can fix?" | Email asking real reason; founder-voice |

**Reason → Offer mapping table** (from churn-prevention source):

| Reason | Best save offer |
|--------|------------------|
| Too expensive | Discount (20-30%, 3 months) |
| Not using enough | Pause (90-day freeze) |
| Missing feature | Roadmap commitment + early-access invite |
| Going to competitor | Honest comparison + ask why |
| Company shutting down | Wish them well, ask for referral |
| Found cheaper alternative | Counteroffer with feature parity proof |

**Health Score** (compute weekly): `Login×0.30 + Usage×0.25 + Engagement×0.25 + Support×0.20`. Score < 60 → trigger pre-emptive save outreach BEFORE they click cancel.

## 6. Win-back sequence (3 emails over 4 weeks)

Triggered 30 days after voluntary cancel.

| # | Day | Subject | Job |
|---|-----|---------|-----|
| 1 | 30 | "[Name], what could we have done better?" | Honest ask, no pitch |
| 2 | 60 | "[Product] update: [recent feature relevant to their use case]" | Value, soft return CTA |
| 3 | 90 | "Last email — staying in touch?" | Final unsubscribe option, leave door open |

After 3 win-back emails, suppress for 12 months (or forever if they unsubscribe).

## 7. Cold outbound sequence (4-6 emails over 21 days)

| # | Day | Shape | Job |
|---|-----|-------|-----|
| 1 | 0 | Observation → Problem → Proof → Ask | Open with research signal |
| 2 | 3 | Bump (no copy change, just "any thoughts?") | Reply rate boost |
| 3 | 7 | Different angle (e.g. case study from peer) | New value, new ask |
| 4 | 14 | Direct ask (specific time slot offered) | Move to meeting |
| 5 | 21 | Breakup ("closing your file unless...") | Pattern interrupt |

**4 structural shapes** (rotate across recipients):
- **OPPP**: Observation → Problem → Proof → Ask
- **SPSA**: Story → Pain → Solution → Ask
- **PEKA**: Personal → Empathy → Knowledge → Ask
- **TPMA**: Trigger event → Pain → Mitigation → Ask

**Subject line "boring/internal" rule**: 2-4 words, lowercase, like an internal email. "quick question", "intro", "[their company] x [your company]". Polished marketing subjects look like ads.

**4-level personalization** (assign per recipient based on tier):

| Tier | Personalization | Effort/email |
|------|-----------------|--------------|
| 1 (mass) | Token-only ({first_name}) | 30 sec |
| 2 (segment) | Industry + role context | 2 min |
| 3 (account) | Read company news, mention specifics | 5-10 min |
| 4 (named) | Read their work, social, references | 15-30 min |

## Universal email rules (apply to ALL archetypes)

- **One email, one job.** If you're tempted to add a P.S. with a second CTA, that's a different email.
- **Value before ask.** Even cold emails should give something (insight, data, link) before asking for time.
- **Relevance > volume.** 100 well-targeted emails beat 10,000 mass emails on every metric.
- **Clear path.** One primary CTA, one fallback, no third option.
- **Reply-to is a real human.** No `noreply@` for lifecycle / cold; use a person's address.
- **Unsubscribe is one click.** Hidden unsubscribe = spam complaints.

## Universal QA checklist (before send)

- [ ] Token rendering tested (no `{first_name}` showing literally)
- [ ] All links work + UTMs added
- [ ] Unsubscribe link present
- [ ] Suppression list applied (suppressed users excluded)
- [ ] Frequency cap respected (no user gets 2 emails same day)
- [ ] Plain-text variant exists
- [ ] Mobile preview checked
- [ ] Spam-trigger words minimized (no all-caps subject, no "FREE")
- [ ] Send time matches recipient timezone (or staggered)
- [ ] A/B test variant set up (if applicable)

For experiment design (sample size for subject-line tests, decision rules), see `bmad-cro-sprint/references/experiment-design.md`.

## Output

`{marketing_artifacts}/lifecycle/sequences/`:
- `welcome.md`
- `nurture.md`
- `activation.md`
- `dunning.md`
- `churn-save.md`
- `win-back.md`
- `cold-outbound.md`

Each file uses the cadence schema above plus full email copy.

## Cross-references

- For voice / language → `bmad-create-marketing-context/references/twelve-section-template.md` (Sections 9, 10).
- For RevOps handoff (when sequence becomes sales-led) → `bmad-revops-enablement-sprint/references/sales-enablement-asset-templates.md`.
- For tracking the cadence → `bmad-growth-audit/references/tracking-plan-template.md` (Object-Action event naming).
