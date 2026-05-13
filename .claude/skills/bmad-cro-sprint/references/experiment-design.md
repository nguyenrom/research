# Experiment Design Reference

> Reference loaded by `bmad-cro-sprint`, `bmad-copy-conversion-sprint`, `bmad-paid-acquisition-sprint`, and `bmad-monetization-sprint` whenever an A/B experiment is being designed. Owner: `bmad-growth-analyst`.

## Hypothesis Template (canonical)

> **Because** <observation / data point>, **we believe** <change> **will cause** <metric movement> **for** <audience segment>.

Example:
> Because 38% of pricing-page visitors scroll to the FAQ but only 4% click the FAQ before pricing decision, we believe surfacing the top-3 FAQ inline above the price tiers will cause pricing-page → trial-start conversion to lift 8-12% for first-time visitors.

A hypothesis without all four parts is incomplete. Don't ship it.

## ICE Scoring (prioritization)

For every candidate experiment in the backlog:

| Dimension | Definition | Score 1-10 |
|---|---|---|
| Impact | If this wins, how big is the lift? | 10 = double-digit %, 5 = single-digit %, 1 = trivial |
| Confidence | How sure are we it'll win? | 10 = same change won 3 times before, 1 = pure guess |
| Ease | How fast/cheap to ship? | 10 = copy edit (1 day), 1 = full re-engineer |

ICE score = (Impact + Confidence + Ease) / 3.

Backlog sort: highest ICE first. Skip the top item if it would block other tests.

## Sample Size Math

You need a sample-size calculation BEFORE starting any test.

Inputs:
- Baseline conversion rate (call it `p_0`) — measured from last 30-day data
- Minimum Detectable Effect (`MDE`) — the smallest lift you'd ship for. Default 5-10% relative, or 1-2 percentage points absolute.
- Statistical power: 0.8 (80%)
- Significance level: 0.05 (95% confidence, 2-tailed)

Formula (rough — use a calculator like Evan Miller's for production):

```
n_per_variant ≈ 16 × p_0 × (1 - p_0) / MDE^2
```

Example: baseline 5% (p_0 = 0.05), absolute MDE 1pp (MDE = 0.01):
n ≈ 16 × 0.05 × 0.95 / (0.01)^2 ≈ 7,600 per variant ≈ 15,200 total.

If your traffic can't reach 15,200 in 14-21 days, the test isn't powered. Either:
- Increase MDE (only if you only care about big wins)
- Test on a higher-traffic surface
- Test multiple bigger changes simultaneously (less precise but fits traffic)
- Don't run the test — make the change based on qualitative signal

## MDE Quick Reference (per variant, p_0 ≈ baseline)

| Baseline | Absolute MDE | Relative MDE | Sample / variant |
|---|---|---|---|
| 2% | 0.5pp | 25% rel | ~12,500 |
| 2% | 1pp | 50% rel | ~3,200 |
| 5% | 1pp | 20% rel | ~7,600 |
| 5% | 2pp | 40% rel | ~1,900 |
| 10% | 2pp | 20% rel | ~3,600 |
| 10% | 5pp | 50% rel | ~600 |

Multiply per-variant by number of variants for total traffic needed.

## Peeking Problem Rule

DO NOT call a test as soon as the dashboard shows a green winner. Either:

- **Fixed-horizon (default)**: declare winner ONLY at pre-committed sample size or duration, whichever is later.
- **Sequential testing**: use a sequential test (Optimizely Stats Engine, mSPRT, Bayesian) that adjusts for repeated peeking.

Peeking at a fixed-horizon test inflates false-positive rate from 5% to 25-50% within 10 peeks. You will ship things that don't actually work.

## Guardrail Metrics

Every test has a primary metric AND guardrails. Guardrails are metrics that MUST NOT degrade.

Standard guardrails:
- Page-load time
- Bounce rate
- Reverse-funnel drop-off (e.g., if testing "view pricing → start trial", guard against "view pricing → leave site")
- Site error rate
- Refund / churn rate (if test affects pricing or activation)

If a guardrail breaches, halt the test EVEN IF the primary is winning.

## Decision Rules (encoded)

Pre-write the decision rule before starting:

| Outcome | Action |
|---|---|
| Primary metric wins ≥ MDE, guardrails OK | Ship variant |
| Primary metric ties (within MDE), guardrails OK | Keep control (or ship simpler variant) |
| Primary metric loses, guardrails OK | Keep control, archive learnings |
| Any guardrail breach | Halt early, revert to control, debug |
| Test runs > 28 days, no signal | Halt — sample size was wrong, redesign |

## Experiment Velocity Targets

Healthy growth team:
- 4-8 experiments per month per major surface (signup, pricing, dashboard)
- Win rate 20-30% (lower = backlog quality issues; higher = MDE is too generous)
- Time-to-decision per test: 14-21 days

If velocity is below 4/month, the test design or ship cycle is the constraint, not ideas.

## Experiment Playbook Entry (write one for every test)

```yaml
- id: <YYYYMMDD-short-slug>
  hypothesis: <full template above>
  primary_metric: <metric name>
  baseline: <pre-test value>
  mde: <absolute or relative>
  sample_size_required: <n_per_variant × variants>
  duration_estimate: <days>
  guardrails: [list]
  decision_rule: <pre-committed>
  status: design|live|halted|won|lost|tied
  result: <only fill after horizon>
  decision: ship|hold|kill
  learnings: <2-4 bullets>
  next_test_idea: <optional>
```

Save the playbook entry to `{marketing_artifacts}/experiments/playbook/<id>.yaml`.

## Output

`{marketing_artifacts}/experiments/`:
- `hypothesis.md` (per test, Because-We Believe-Will Cause-For)
- `sample-size-table.md` (the calculation)
- `ice-prioritized-backlog.md` (full backlog ranked)
- `playbook/<id>.yaml` (one per test, archived after decision)
