# Sales Enablement Asset Templates

> Reference loaded by `bmad-revops-enablement-sprint` Phase 3 (Sales Enablement Assets). Concrete templates for the highest-leverage seller assets: pitch deck, one-pager, demo script, battlecard, objection doc, persona card, ROI calculator, case study brief, playbook.

## The 9 standard assets

| Asset | Length | Refresh cadence | Owner |
|-------|--------|-----------------|-------|
| Pitch deck | 10-12 slides | Quarterly | Marketing + Sales lead |
| One-pager | 1 page (PDF) | Quarterly | Marketing |
| Demo script | 20-30 min flow | Monthly | Sales + Product |
| Battlecard (per competitor) | 1-2 pages | Monthly (when competitor moves) | RevOps |
| Objection doc | 1 spreadsheet | Continuously updated | Sales + RevOps |
| Persona card | 1 page each | Quarterly | Marketing |
| ROI calculator | 1 spreadsheet/calculator | Quarterly | Sales engineering |
| Case study brief | 1 page each | After every deal close | Marketing |
| Sales playbook | 5-15 pages | Quarterly | Sales lead |

## 1. Pitch deck — 10-12 slide framework

```
Slide 1  → Title: company + tagline + presenter
Slide 2  → The world today (the problem stated as a customer's frustration)
Slide 3  → Why this is broken now (trend / shift / urgency)
Slide 4  → Existing alternatives + why they fail (3-5 alternatives, 1 line each)
Slide 5  → Our solution (1 sentence, 1 visual)
Slide 6  → How it works (3-5 steps; this is NOT feature-tour)
Slide 7  → The proof (3-5 customer outcomes with numbers)
Slide 8  → Differentiation (us vs. top 1-2 competitors)
Slide 9  → Pricing or business model (transparent, no surprises)
Slide 10 → Team / company credibility (founders, customer count, funding)
Slide 11 → What's next (CTA: trial, pilot, demo, follow-up)
Slide 12 → Q&A / contact
```

**Anti-patterns**:
- Slide 2-3 = product features (problem comes first, ALWAYS).
- Slide 7 = stock photos of happy customers (named customers + numbers, or skip).
- Slide 10 = team-photo-heavy (one team slide max; spend the real estate on proof).

## 2. One-pager — single sheet PDF

Layout (top-to-bottom):

```
┌──────────────────────────────────────┐
│ LOGO        [Tagline — 6 words]      │
├──────────────────────────────────────┤
│ THE PROBLEM                           │
│ 2 sentences, named persona's pain    │
├──────────────────────────────────────┤
│ THE SOLUTION                          │
│ 1 sentence + 3 capability bullets    │
├──────────────────────────────────────┤
│ PROOF                                 │
│ 3 customer outcomes (named, numbers) │
│ Logo strip                            │
├──────────────────────────────────────┤
│ HOW WE'RE DIFFERENT                   │
│ Vs. [Competitor 1]: [1 line]         │
│ Vs. doing nothing: [1 line]          │
├──────────────────────────────────────┤
│ NEXT STEP                             │
│ CTA + URL + contact                   │
└──────────────────────────────────────┘
```

Test: a stranger reading for 30 seconds should know what we sell, who it's for, and the next step.

## 3. Demo script — 20-30 minute flow

```
Minute 0-2   : Frame (why we're meeting, agenda, "stop me anytime")
Minute 2-7   : Discovery (5-7 questions to confirm pain + decision criteria)
Minute 7-22  : Walkthrough mapped to discovered pain
                ├── ALWAYS show: core feature 1, 2, 3 (whatever happens)
                ├── CONDITIONAL on discovery: persona-specific features
                └── Skip what they didn't ask about
Minute 22-27 : Pricing (only if they qualified; otherwise schedule follow-up)
Minute 27-30 : Close: define the next step, lock in date
```

**Discovery questions** (the 5-7):
1. What problem prompted you to look at us today?
2. How are you handling that today? (manual? competitor? not at all?)
3. What's working and what's broken with the current approach?
4. Who else is involved in this decision?
5. What does "success" look like for you in 90 days?
6. What's your timeline?
7. What would make this NOT a fit?

If demo dive starts before discovery, the demo is wrong. Sales rep follows a discovery-first script even if it feels rushed.

## 4. Battlecard (per competitor) — 1-2 pages

```markdown
# Battlecard: [Us] vs. [Competitor]

## TL;DR
- We win when: [3 specific scenarios]
- They win when: [2 specific scenarios — be honest]

## Strength matrix
| Capability | Us | [Competitor] | Notes |
|------------|----|--------------| ----- |
| [Feature/job 1] | ✅ Strong | ⚠️ Weak | [Specific differentiator] |
| [Feature/job 2] | ⚠️ OK | ✅ Strong | [Acknowledge honestly] |
| ...

## How they sell against us
- Their pitch: "[exact phrasing they use]"
- The truth: [honest counter]
- Our proof: [customer / data]

## How we sell against them
- Wedge 1: [pain we address that they don't]
- Wedge 2: [data point that flips a deal]
- Wedge 3: [customer reference willing to talk to prospects]

## When NOT to sell against them
[Scenarios where we should refer the prospect to them or to a third option.
This builds trust with prospects and prevents losing deals to "we evaluated everyone".]

## Talking points
- [10-second pitch when prospect mentions them]
- [30-second deep cut when they push back]
- [Email-friendly forwardable version]

## Public assets
- Public comparison page URL: ...
- Independent review citing both: ...

## Last updated: YYYY-MM-DD by [owner]
```

## 5. Objection doc — 3-part structure per objection

```yaml
- objection: "Your product is too expensive."
  category: pricing
  frequency: high
  acknowledge: "Totally hear that — we're not the cheapest option."
  reframe: "We price based on value delivered. The teams who get
            the most ROI are the ones doing X, Y, Z volume."
  proof: "[Customer Name] cut $40K/year of [tool stack] and replaced
          it with us at $12K. Their case study is here: [URL]."
  escalation: "If price is truly a blocker, we have a starter tier
              at $X for under-Y-seats. Let's see if it fits."
```

Acknowledge → Reframe → Proof. NEVER skip the acknowledge — the prospect feels dismissed.

Maintain top 10-15 objections in `objection-doc.md`; new patterns get added monthly.

## 6. Persona card — 1 page per persona

```
┌──────────────────────────────────────────────────┐
│  [Persona name + role + photo/avatar]            │
│  e.g. "Director of Demand Gen at $5-50M ARR SaaS" │
├──────────────────────────────────────────────────┤
│  TOP 3 JOBS                                       │
│  1. ...                                           │
│  2. ...                                           │
│  3. ...                                           │
├──────────────────────────────────────────────────┤
│  TOP 3 PAINS                                      │
│  1. ...                                           │
│  2. ...                                           │
│  3. ...                                           │
├──────────────────────────────────────────────────┤
│  WHAT THEY READ                                   │
│  [3-5 specific publications / podcasts / people]  │
├──────────────────────────────────────────────────┤
│  WHERE THEY HANG OUT                              │
│  [3-5 specific channels]                          │
├──────────────────────────────────────────────────┤
│  TRIGGER EVENTS                                   │
│  [3-5 events that make them shop for solutions]   │
├──────────────────────────────────────────────────┤
│  ANTI-PATTERN                                     │
│  Looks similar but is NOT this persona: [...]     │
└──────────────────────────────────────────────────┘
```

Pull from `marketing-context.md` Section 3 directly.

## 7. ROI calculator — sheet structure

Inputs (prospect fills in):
- Current cost (tool stack + people-hours)
- Current volume / scale
- Current pain metric (e.g. hours/month, errors/quarter)

Outputs (auto-calculated):
- Projected savings (1 year)
- Payback period (months)
- 3-year ROI

Validation rules:
- Inputs that produce nonsensical outputs are flagged (e.g. unrealistic baselines).
- Conservative defaults — do NOT inflate; over-promising = churn.

## 8. Case study brief — 1 page each

```
- Customer: [Name + logo + size + industry]
- Persona contacted: [name + role]
- Problem: 2-3 sentences in customer's words
- Why us: 1 sentence
- Solution: how they implemented (3-5 bullets)
- Outcome: 3 quantified results (within 90 days, 6 months, 12 months)
- Quote: 1 strong testimonial (verbatim, name, role)
- Approval status: Public / NDA only / Anonymous
- Asset: full case study URL OR draft path
```

## 9. Sales playbook — 5-15 pages

Master document linking everything together:

```
1. ICP definition (link to persona cards)
2. Disqualification criteria (who we should not sell to)
3. The discovery framework (5-7 questions)
4. The demo script (link to demo asset)
5. The pricing conversation (when, how)
6. The proposal template
7. Common objections (link to objection doc)
8. Battlecards (link per competitor)
9. Closing motions: trial → contract path
10. Handoff to CSM
```

Sales playbook is the table of contents for the rest of the assets — it tells reps what to use when.

## Output

`{marketing_artifacts}/revops/sales-enablement/`:
- `pitch-deck-outline.md` (slide-by-slide structure)
- `one-pager.md`
- `demo-script.md`
- `battlecards/<competitor>.md` (one per competitor)
- `objection-doc.md`
- `persona-cards/<persona>.md` (one per persona)
- `roi-calculator-spec.md` (inputs/outputs/formulas)
- `case-study-briefs/<customer>.md` (one per customer)
- `sales-playbook.md` (master)

## Cross-references

- For persona content → `bmad-create-marketing-context/references/twelve-section-template.md` (Section 3).
- For competitive intel feeding battlecards → `bmad-customer-research-sprint/references/voc-mining-protocols.md`.
- For objections → `bmad-create-marketing-context/references/twelve-section-template.md` (Section 7).
