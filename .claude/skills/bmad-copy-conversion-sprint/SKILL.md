---
name: bmad-copy-conversion-sprint
description: Run copywriting, copy-editing, copy refresh, marketing psychology, lead magnet messaging, and conversion-copy work. Use when the user says "CCS" or needs conversion copy.
---

# Copy Conversion Sprint Workflow

**Goal:** Produce persuasive, evidence-backed marketing copy or improve existing copy using VOC, positioning, conversion structure, behavioral psychology, and editing sweeps.

**Your Role:** Workflow facilitator coordinating with the Content Architect, CRO Strategist, Growth Loop Designer, SEO Strategist, and Monetization Strategist as needed.

## References

- `references/seven-sweeps.md` — Full Seven Sweeps framework + Expert Panel scoring rubric + refresh-vs-rewrite matrix. Required reading for Phase 3.
- `references/marketing-psychology-models.md` — ~50-model catalog organized by 4 buckets (Foundational, Buyer, Persuasion, Pricing) + ethical-persuasion guardrail. Required reading for Phase 1 step 3.

## Prerequisites

This workflow consumes the shared marketing context. Before starting, run `bmad-create-marketing-context` (or confirm the file exists). If `{marketing_artifacts}/marketing-context.md` is missing, halt and invoke `bmad-create-marketing-context` first.

## Conventions

- Bare paths resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

**If the script fails**, resolve the workflow block from base, team, and user customization files using BMad structural merge rules.

### Step 2: Execute Prepend Steps

Execute `{workflow.activation_steps_prepend}`.

### Step 3: Load Persistent Facts

Treat `{workflow.persistent_facts}` as foundational context. Load `file:` entries.

### Step 4: Load Config

Load `{project-root}/_bmad/performance-marketing/config.yaml` and resolve `{user_name}`, `{communication_language}`, `{document_output_language}`, `{company_name}`, and `{marketing_artifacts}`.

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`. Ask whether the sprint is for new copy, rewriting existing copy, copy-editing, lead magnet copy, pricing copy, or landing-page conversion.

### Step 6: Execute Append Steps

Execute `{workflow.activation_steps_append}`.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/copy-conversion-sprint.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Copy Brief

**Lead agent:** bmad-content-architect

1. **Objective & Asset** — Define asset type, audience, offer, conversion goal, traffic source, and existing baseline. → output: `copy-brief.md`
2. **Message Inputs** — Pull VOC, positioning, objections, proof, competitor alternatives, and search/social intent. → output: `message-inputs.md`
3. **Psychology Map** — Choose relevant persuasion levers: specificity, social proof, contrast, risk reversal, loss aversion, anchoring, status, or ease. Apply ethical-persuasion guardrail (do not weaponize biases against the buyer's interest); see `references/marketing-psychology-models.md` for model catalog and ethics rule. Present chosen levers and rationale to user. → output: `psychology-map.md` → gate: `user_approval`

### Phase 2: Draft or Rewrite

**Lead agent:** bmad-content-architect + bmad-cro-strategist

1. **Structure** — Select copy structure: landing page, homepage, feature page, pricing page, lead magnet landing page, ad landing page, or email capture page. → output: `copy-structure.md`
2. **Headline & CTA Variants** — Draft multiple headline, subhead, CTA, and proof variants tied to hypotheses. → output: `headline-cta-variants.md`
3. **Section Copy** — Draft full copy by section with conversion rationale. → output: `section-copy.md`

### Phase 3: Seven Sweeps Editing

**Lead agent:** bmad-content-architect

Apply ALL seven sweeps in order. Skipping any sweep is incomplete editing. After Sweep 7, loop back to Sweep 1 to verify new specificity/emotion edits did not introduce clarity issues. See `references/seven-sweeps.md` for the full framework, expert-panel scoring rubric, and refresh-vs-rewrite matrix.

1. **Clarity Sweep** — Remove vague claims, jargon, and unclear buyer value. → output: `clarity-edits.md`
2. **Voice Sweep** — Re-align tone with brand persona; cut corporate clichés. → output: `voice-edits.md`
3. **So-What Sweep** — Tie every feature claim to the buyer's outcome. → output: `so-what-edits.md`
4. **Prove-It Sweep** — Add evidence, numbers, named customers, links to public proof. → output: `prove-it-edits.md`
5. **Specificity Sweep** — Replace abstract claims with concrete, testable details. → output: `specificity-edits.md`
6. **Heightened-Emotion Sweep** — Use sensory language, before/after contrast, named pains and wins. → output: `heightened-emotion-edits.md`
7. **Zero-Risk Sweep** — Add guarantees, free-trial reminders, no-credit-card lines, and FAQ at decision points. → output: `zero-risk-edits.md`
8. **Expert Panel Scoring** — Score the final copy with 3-5 named personas using the rubric in `references/seven-sweeps.md`. Average ≥ 8 = ship; below = re-sweep weakest dimensions. → output: `expert-panel-scores.md` → gate: `user_approval`

### Phase 4: Testing & Handoff

**Lead agent:** bmad-growth-analyst

1. **Experiment Ideas** — Convert copy alternatives into A/B hypotheses with metrics, sample-size requirements, and decision rules. Present test plan and risk assessment for approval before publishing. → output: `copy-test-plan.md` → gate: `user_approval`
2. **Implementation Notes** — Mark what goes to website, email, paid creative, social, SEO, or sales enablement. → output: `copy-handoff.md`

### Completion

Append a final **Summary** to `outputFile`, then recommend `bmad-cro-sprint`, `bmad-paid-acquisition-sprint`, or `bmad-content-pipeline` depending on the asset.

