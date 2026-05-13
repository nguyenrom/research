# Seven Sweeps Editing Framework

> Reference loaded by Phase 3 of `bmad-copy-conversion-sprint`. Apply EVERY sweep in order — skipping any sweep is incomplete editing. Loop back if a later sweep surfaces issues a prior sweep missed.

## The Seven Sweeps (in order)

| # | Sweep | Question being asked | Common edits |
|---|---|---|---|
| 1 | Clarity | Can a 12-year-old understand this in one read? | Cut jargon, replace abstract claims with plain language, break long sentences |
| 2 | Voice | Does this sound like the brand / persona — or like a generic LinkedIn post? | Replace corporate clichés with the brand's actual rhythm, contractions, opinions |
| 3 | So What | Why should the reader care? | Add the reader's outcome to every feature claim ("X means you can Y") |
| 4 | Prove It | What evidence backs each promise? | Add numbers, screenshots, customer names, case data, links to public proof |
| 5 | Specificity | Are claims concrete enough to be testable? | Replace "fast" → "loads in 1.4s", "scalable" → "handles 10k req/s on a $20 instance" |
| 6 | Heightened Emotion | Is this writing felt, or merely understood? | Use sensory language, before/after vivid contrast, named pain points, victory moments |
| 7 | Zero Risk | What might still cause hesitation at the CTA? | Add money-back guarantee language, free-trial reminders, no-credit-card line, FAQ at bottom |

## Mandatory Loopback Rule

After completing Sweep 7, RE-READ Sweep 1's pass to confirm new specificity (Sweep 5) and emotion (Sweep 6) didn't introduce new clarity issues. A second loopback is only required if any sweep produced 3+ edits.

## Expert Panel Scoring

After all 7 sweeps, score the final copy with 3-5 named personas. Each persona scores on a 1-10 rubric. Target average: 8+ across the panel.

### Suggested rubric (per persona)

- **Comprehension** (1-10): Did I understand it on first read?
- **Relevance** (1-10): Does it speak to my situation?
- **Credibility** (1-10): Did I believe the claims?
- **Desire** (1-10): Do I want to act?
- **Action clarity** (1-10): Do I know exactly what happens if I click?

Sum of 5 scores ÷ 5 = persona's overall. Average across the 3-5 panelists. If overall < 8, revisit the 1-2 weakest dimensions and re-sweep.

## Refresh vs Rewrite Matrix

| Existing copy state | Action |
|---|---|
| Baseline conversion + brand voice intact | Refresh: 7 sweeps only |
| Baseline conversion broken, voice intact | Refresh + restructure (sweeps + Phase 2 Section Copy redo) |
| Voice off-brand, conversion OK | Rewrite voice + sweeps 1-3 |
| Both broken | Full rewrite (start Phase 2 from scratch) |

## Output requirements

For each sweep, produce a labeled section with:
- Before
- After
- Reason (1-2 lines tying back to the sweep's question)

Save to `clarity-edits.md`, `voice-edits.md`, `so-what-edits.md`, `prove-it-edits.md`, `specificity-edits.md`, `heightened-emotion-edits.md`, `zero-risk-edits.md`.

The Phase 3 SKILL.md currently lists only 4 sweep files for backward compatibility. When running this workflow, use ALL SEVEN sweep file names above and supersede the SKILL.md's 4-file list.
