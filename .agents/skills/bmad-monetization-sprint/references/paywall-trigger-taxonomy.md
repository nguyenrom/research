# Paywall & Upgrade Trigger Taxonomy

> Reference loaded by `bmad-monetization-sprint` Phase 3 (Paywall / Upgrade Moments) and `bmad-cro-sprint` for paywall UX work. Owner: `bmad-monetization-strategist` jointly with `bmad-cro-strategist`.

## Trigger Taxonomy (4 categories)

Every paywall fires from one of these. Mixing them in a single screen creates noise.

### 1. Feature Gate
User attempts a feature that requires an upgrade.
- **When**: User clicks "Export to PDF" on free plan.
- **Pattern**: Inline modal with "This is a Pro feature. Try free for 14 days."
- **What works**: Show the user EXACTLY what they tried to do, in a preview.
- **Risk**: Frustration if feature seems basic. Test a free alternative path.

### 2. Usage Limit
User has consumed their quota.
- **When**: 100/100 API calls used in current period.
- **Pattern**: Banner + email + in-app toast warning at 80%, 90%, 100%.
- **What works**: Show usage trajectory ("you'll hit 100% by Tuesday at this rate").
- **Risk**: Hard cuts feel punitive. Provide grace mode (slow but functional).

### 3. Trial Expiration
Trial ends, must convert.
- **When**: Day 14 of 14-day trial.
- **Pattern**: 7-day, 3-day, 1-day countdown email + in-app banner. End-of-trial: full-screen with "save your work" + 1-click upgrade.
- **What works**: Make the workspace data clearly visible behind the modal — they're protecting THEIR data.
- **Risk**: Hard wall on day 15 = high churn. Allow read-only after expiration.

### 4. Time-Based (cohort/seasonal)
Time-based promotional or seasonal triggers.
- **When**: Black Friday, anniversary, mid-quarter pricing test.
- **Pattern**: Banner site-wide, email blast, email auto-send to free users with usage.
- **What works**: Real, visible deadline. Genuine offer (not fake countdown).
- **Risk**: Train users to wait for sales.

## "Respect the No" Rule

If a user dismisses a paywall:
- They MUST NOT see the same paywall again within 24 hours.
- They MUST NOT see it more than 3 times total (across all sessions).
- If they upgrade and downgrade later, reset the counter to 0.
- Provide a "stop showing me upgrade offers" toggle in settings.

Violating this rule increases unsubscribe rate by 40-60% within 30 days. Subjective irritation compounds.

## Frequency Capping

| Trigger type | Max impressions per user / month |
|---|---|
| Feature gate | unlimited (user is intentionally hitting it) |
| Usage limit | unlimited (status quo, not promotional) |
| Trial expiration | 5 (all expiry-related touches) |
| Time-based | 2 |

## Dark-Pattern Blacklist (DO NOT USE)

These tactics convert short-term but destroy retention and brand trust. Forbidden:

- ❌ Confirm-shaming ("No thanks, I don't want to grow my business")
- ❌ Hidden recurring charges or surprise renewals
- ❌ Decoy that traps users in wrong tier
- ❌ Fake countdowns that reset on refresh
- ❌ Fake stock counts ("Only 2 left at this price!" for a digital product)
- ❌ Pre-checked add-ons at checkout
- ❌ Retention surveys that gate cancellation behind 5+ screens (Roach Motel)
- ❌ Drip-feed cancellation (must call to cancel)
- ❌ Auto-upgrade with surprise email after the fact

## Trigger Map Template

`{marketing_artifacts}/monetization/paywalls/trigger-map.md`:

| Trigger | Category | Free user state | Message | Offer | Fallback | Tracking event |
|---|---|---|---|---|---|---|
| Export to PDF clicked | Feature Gate | active free | "Export is Pro" | 14d trial, no card | Provide JSON export | paywall_export_triggered |
| API quota 100% | Usage Limit | active free | "Quota reached" | Upgrade now | Read-only until renewal | paywall_quota_triggered |
| Trial day 12 | Trial Exp | trialing | "3 days left" + show data | 20% off annual | Read-only mode | paywall_trial_d12 |
| Black Friday | Time-Based | active free | "30% off annual" | 30% off, 7 days | Standard pricing | paywall_bf_seen |

## Screen Designs (5 elements)

Every paywall screen has:

1. **Header** — names what was attempted ("Export to PDF" / "100/100 API calls used")
2. **Plan benefits** — 3-5 bullets, the user's job mapping NOT generic features
3. **Pricing** — visible, not hidden behind another click
4. **Primary CTA** — "Try Pro Free" or "Upgrade — $X/mo" — high contrast
5. **Secondary action** — "Continue with limited" or "Maybe later" — visible, NOT hidden, NOT confirm-shamed

## A/B Test Framework

Most-impactful tests:
- Headline: outcome-focused vs feature-focused
- Number of bullets: 3 vs 5 vs 7
- Primary-CTA copy: "Upgrade" vs "Try Free" vs "Get Pro"
- Plan presentation: monthly-only vs monthly+annual toggle
- Free-trial length: 7 vs 14 vs 30 days
- Card-required vs no-card-required trial

Power tests with experiment-design reference (`../bmad-cro-sprint/references/experiment-design.md`).

## Output

`{marketing_artifacts}/monetization/paywalls/`:
- `trigger-map.md` (the table above, populated)
- `screen-designs.md` (each trigger with the 5 elements)
- `frequency-rules.md` (capping schedule)
- `respect-the-no.md` (the rule + how it's enforced in code)
- `ab-tests.md` (experiment plan)
