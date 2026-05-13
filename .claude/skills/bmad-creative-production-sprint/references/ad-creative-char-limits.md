# Ad Creative — Char Limits, Angle Taxonomy, 3-Wave Generation

> Reference loaded by `bmad-creative-production-sprint` Phase 2 (Copy & Asset Variations) and Phase 3 (Platform Adaptation). Per-platform character constraints, the 8-angle taxonomy, and the 3-wave generation method.

## Per-platform char limits (current as of 2026)

| Platform | Field | Limit | Notes |
|----------|-------|-------|-------|
| **Google RSA** | Headline (×15) | 30 chars | Pin headline 1 to keyword |
| | Description (×4) | 90 chars | First desc shown most |
| | Path (×2) | 15 chars | Display URL only |
| | Final URL | unlimited | Use UTMs |
| **Meta (Facebook + Instagram feed)** | Primary text | 125 chars | Beyond = "...see more" |
| | Headline | 27 chars | Bottom card |
| | Description | 27 chars | Optional, link preview |
| | Image text | < 20% of image area | Penalty if exceeded |
| **Meta Stories / Reels** | Caption | 2,200 chars | But truncated at 125 |
| | Video length | 15-90s for ads | 15s for skippable |
| **LinkedIn (Sponsored Content)** | Intro text | 150 chars | Above the fold |
| | Headline | 70 chars | Bold under intro |
| | Description | 100 chars | Optional |
| | Single image | 1200×627px | 1.91:1 aspect |
| | Document ad | 1200×1500px | Carousel format |
| **LinkedIn (Message Ads)** | Subject | 60 chars | Inbox display |
| | Body | 1,500 chars | Plain text only |
| **X (Twitter)** | Tweet | 280 chars | Promoted Tweet |
| | Header img | 1500×500px | Profile asset |
| | Card description | 70 chars | Below image |
| **TikTok** | Caption | 80 chars | Under video |
| | Display name | 80 chars | Brand profile |
| | Video length | 9-60s for ads | 15-25s sweet spot |
| **Pinterest** | Pin title | 100 chars | Above pin |
| | Pin description | 500 chars | SEO-relevant |
| | Display URL | 65 chars | Visible domain |
| **YouTube TrueView** | Headline | 25 chars | Companion banner |
| | Description | 70 chars × 2 | Two-line |
| | Video length | 6s (bumper) / 15s (non-skip) / 30s+ (skip) | |
| **Reddit Promoted Posts** | Title | 300 chars | Like a regular post |
| | Body | 40,000 chars | But brevity wins |

Validate against these limits BEFORE QA. Any creative exceeding cuts gets visually clipped on the platform.

## 8-angle taxonomy

Every ad belongs to one of 8 persuasion angles. Healthy creative matrix has at least 4 angles in rotation per ad set / campaign.

| Angle | What it leverages | Example headline |
|-------|-------------------|------------------|
| **Pain** | Reader recognition of own problem | "Tired of pricing that punishes growth?" |
| **Outcome** | Desired end state | "Hit your $1M ARR in 12 months" |
| **Social proof** | Others have done it | "10,000+ founders trust [Product]" |
| **Curiosity** | Open loop, info gap | "The 1-hour weekly habit that compounded our pipeline 5×" |
| **Comparison** | Vs. competitor / alternative | "Why we left HubSpot for [Product]" |
| **Urgency** | Scarcity, deadline | "Pricing changes Jan 1 — lock in 2026 rates" |
| **Identity** | Tribe / status | "For founders who measure twice and cut once" |
| **Contrarian** | Against conventional wisdom | "Stop A/B testing. Do this instead." |

A creative matrix that's all "outcome" angles fatigues fast — Meta and LinkedIn algorithms punish single-angle saturation.

## 3-wave generation method

Don't generate ads sequentially. Generate in 3 waves to avoid groupthink:

### Wave 1 — Core (4-6 variants)
- 1 angle: outcome
- 1 angle: social proof
- 1 angle: pain
- Conservative copy, on-brand voice
- Goal: stable performers, low risk

### Wave 2 — Extend (4-6 variants)
- Take the top performer of Wave 1.
- Vary: headline, image, CTA — one variable at a time.
- Goal: incremental wins via creative iteration.

### Wave 3 — Wild card (3-4 variants)
- Off-brand angle (contrarian, unusual format, deliberately weird).
- Often the surprise winner.
- Allocate 10-15% of budget here.
- Goal: discover non-obvious winners.

Total: 11-16 variants per major launch. This is the volume Meta/LinkedIn algorithms need to learn.

## Creative quality bar

Before sending to platform:

- [ ] Headline ≤ char limit; first 30 chars carry the value prop.
- [ ] Image text < 20% of image area (Meta penalty).
- [ ] CTA copy is action + benefit, not just "Learn More".
- [ ] LP message-match: ad headline keyword reappears in LP H1.
- [ ] Mobile preview checked (most impressions are mobile).
- [ ] Audio-off preview checked for video (captions burned in).
- [ ] No ALL CAPS shouting except brand-acronym.
- [ ] Brand colors / logo visible within first 1 second of video.

## Test plan template (per creative)

```yaml
- creative_id: 2026-q2-pain-01
  angle: pain
  wave: 1
  copy:
    headline: "Tired of pricing that punishes growth?"
    primary_text: "..."
    cta: "See our flat-rate"
  visual: ad-creatives/q2/pain-01.jpg
  hypothesis: "Pain framing on pricing-page traffic outperforms outcome framing for switchers"
  primary_metric: signup_rate
  baseline: 2.1%
  mde: +0.5pp absolute
  guardrails: [bounce_rate, refund_rate]
  budget_per_day: $50
  expected_duration: 14 days
```

For full experiment design (sample-size math, peeking rule, decision rules) → `bmad-cro-sprint/references/experiment-design.md`.

## Output

`{marketing_artifacts}/creative/`:
- `creative-angle-matrix.md` — 8 angles × what works for each persona.
- `wave-plan.md` — wave 1 / 2 / 3 variants with hypothesis per creative.
- `<platform>/creative-specs.md` — adapted copy + assets per platform.
- `production-checklist.md` — QA gates before publish (the quality bar above).

## Cross-references

- For paid channel architecture → `bmad-paid-acquisition-sprint/references/channel-architecture-presets.md`.
- For seven-sweep editing on the body copy → `bmad-copy-conversion-sprint/references/seven-sweeps.md`.
- For test design → `bmad-cro-sprint/references/experiment-design.md`.
