# Bullseye Channel Selection + ICE Prioritization

> Reference loaded by `bmad-marketing-strategy` Phase 2 (Strategy Development) and Phase 3 (Action Planning). The framework Max Growth uses to pick 2-3 priority channels and rank initiatives.

## Why bullseye

Most early-stage SaaS over-invest in 5-8 channels at once and burn out. The bullseye framework forces ruthless prioritization: pick 3 to test, double down on what works, kill the rest.

## The 3-ring framework

```
                    ┌──────────────────┐
                    │   OUTER RING     │
                    │  (long-shot)     │
                    │                  │
                    │  ┌────────────┐  │
                    │  │ MIDDLE     │  │
                    │  │ (probable) │  │
                    │  │            │  │
                    │  │  ┌──────┐  │  │
                    │  │  │INNER │  │  │
                    │  │  │(test)│  │  │
                    │  │  └──────┘  │  │
                    │  └────────────┘  │
                    └──────────────────┘
```

- **Outer ring** — every channel that exists, no filter. Brainstorm all 19+ Bullseye-traction channels (SEO, content, paid search, paid social, viral, social ads, display, offline ads, email, business dev, sales, affiliate, existing platforms, trade shows, speaking, community building, PR, unconventional PR, engineering as marketing).
- **Middle ring** — channels plausible for THIS product/stage/team given resources, talent, and ICP behavior.
- **Inner ring** — top 3 candidates to actually test in the next 4-6 weeks.

## Channel-stage fit matrix

Not every channel works at every SaaS stage. Use this as a sanity filter before promoting from outer → middle ring:

| Stage | Channels that work | Channels that DON'T |
|-------|---------------------|----------------------|
| Pre-PMF (0–$10K MRR) | Founder-led sales, community, content with founder voice, narrow-niche communities | Paid acquisition, PR, agencies |
| Post-PMF ($10K–$100K MRR) | SEO, content, social, lifecycle email, light paid (LinkedIn, Reddit, niche), partnerships | Mass display ads, expensive PR, big-budget paid search |
| Scaling ($100K+ MRR) | Mature SEO + content engine, paid acquisition (Google + Meta + LinkedIn), PR, partnerships, events, ABM | Reliance on a single channel for >50% of acquisition (concentration risk) |

## Budget × stage filter

| Budget | Allowed channels |
|--------|-------------------|
| < $1K/month | Organic only (SEO, content, social, community, lifecycle) |
| $1K–$5K/month | Organic + paid experiments ($300-500 budget per test) |
| $5K–$25K/month | Balanced organic + paid; one paid channel at scale |
| $25K+/month | Full mix, agency-augmented, multi-channel attribution required |

## ICE scoring (initiative prioritization within a channel)

For each candidate initiative on the chosen channel, score:

| Dimension | What it asks | Score 1-10 |
|-----------|--------------|-----------|
| Impact | If this works, how much revenue / pipeline / signups does it move? | 10 = double-digit % shift; 5 = single-digit; 1 = trivial |
| Confidence | How sure are we this works for OUR product / ICP / stage? | 10 = same play won 3 times before; 1 = pure guess |
| Ease | How fast and cheap to ship? | 10 = same-day, no engineering; 1 = 6-week build |

**ICE score = (Impact + Confidence + Ease) / 3.**

Rank backlog by ICE score, top-down. Skip the #1 if it blocks others; otherwise sequence is the score order.

## Prioritization mistakes to avoid

| Mistake | Fix |
|---------|-----|
| Picking inner-ring channels you LIKE, not ones that fit ICP | Defer to ICP behavior (where do they actually hang out?) |
| Killing inner-ring channels at week 2 | Give each inner test 4-6 weeks minimum (channel signal needs that much time) |
| Promoting all 3 inner-ring to "winner" because none was decisive | Force a ranking: which moved the needle most? Even if all 3 were marginal, pick one and double down |
| Adding a 4th channel before killing one | Hard rule: 2-3 channels max for early-stage |
| Confidence-only or impact-only ranking | ICE is 3-axis; prevents "hopefully" prioritization |

## Sprint cycle

```
Week 1: Brainstorm outer → filter to middle → narrow to inner 3
Week 2-5: Run inner-3 in parallel with explicit budget caps and decision rules
Week 6: Review results vs. baseline. Promote 1 winner, kill 1, retest 1 with iteration.
Week 7-12: Double down on winner; explore next candidate from middle ring.
```

## Output

`{marketing_artifacts}/strategy/`:
- `bullseye-outer-ring.md` — full brainstorm.
- `bullseye-middle-ring.md` — filtered to plausible.
- `bullseye-inner-ring.md` — top 3 with hypothesis, budget, decision rule.
- `ice-backlog.md` — ranked initiatives within chosen channels.
- `channel-decision-log.md` — record of which channel made it / didn't, why.

## Cross-references

- For experiment design rigor on channel tests → `bmad-cro-sprint/references/experiment-design.md`.
- For paid-channel architecture once a paid channel is in inner ring → `bmad-paid-acquisition-sprint/references/channel-architecture-presets.md`.
- For the marketing context that informs channel-fit → `bmad-create-marketing-context/references/twelve-section-template.md`.
