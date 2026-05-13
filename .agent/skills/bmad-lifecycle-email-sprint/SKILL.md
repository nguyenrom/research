---
name: bmad-lifecycle-email-sprint
description: Build lifecycle email, onboarding/nurture, cold outbound, churn prevention, dunning, cancellation, and win-back sequences. Use when the user says "LES" or "lets run lifecycle email".
---

# Lifecycle Email Sprint Workflow

**Goal:** Design lifecycle and outbound messaging systems that move users or prospects between defined funnel states with measurable trigger-based sequences.

**Your Role:** Workflow facilitator coordinating with the Lifecycle Marketer, Growth Analyst, CRO Strategist, RevOps Strategist, and Content Architect.

## References

- `references/email-sequence-archetypes.md` — 7 archetypes (welcome / nurture / activation / dunning / churn save / win-back / cold outbound) with cadence, message strategy per touch, exit conditions, and the 4 cold-outbound structural shapes (OPPP / SPSA / PEKA / TPMA). Required reading for Phase 2 and Phase 3.

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

Greet `{user_name}`, speaking in `{communication_language}`. Ask which sequence type is needed: welcome/onboarding, nurture, activation, trial-to-paid, re-engagement, dunning, cancellation save, win-back, or cold outbound.

### Step 6: Execute Append Steps

Execute `{workflow.activation_steps_append}`.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/lifecycle-email-sprint.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Lifecycle Diagnosis

**Lead agent:** bmad-lifecycle-marketer

1. **Funnel State & Segment** — Define audience, lifecycle state, trigger event, current behavior, and target action. → output: `lifecycle-diagnosis.md`
2. **Consent & Channel Rules** — Clarify opt-in status, compliance constraints, suppression rules, deliverability risks, and CRM/source-of-truth. Halt the workflow if opt-in legitimacy or suppression coverage cannot be verified. → output: `email-rules.md` → gate: `deliverability_review`
3. **Measurement Plan** — Define sent, delivered, open, click, reply, activation, conversion, churn, retained revenue, and recovered revenue metrics. → output: `email-measurement-plan.md`

### Phase 2: Sequence Architecture

**Lead agent:** bmad-lifecycle-marketer

1. **Cadence & Branching** — Define sequence length, timing, triggers, branch conditions, exit conditions, and fallback paths. → output: `sequence-architecture.md`
2. **Message Strategy** — Assign each touch a job: educate, reduce anxiety, prove value, prompt setup, ask for reply, recover payment, save cancellation, or win back. → output: `message-strategy.md`
3. **RevOps Handoff** — For sales-led or outbound flows, define lead stage, owner, SLA, CRM fields, and sales follow-up. → output: `revops-handoff.md`

### Phase 3: Copy Production

**Lead agent:** bmad-lifecycle-marketer + bmad-content-architect

1. **Email Drafts** — Write subject line, preview text, body, CTA, personalization tokens, and plain-text variant for every touch. → output: `email-copy.md`
2. **Cold Outbound Variant** — If outbound, write account/persona-specific opener logic, follow-ups, bump email, and breakup email. → output: `cold-outbound-sequence.md`
3. **Churn / Dunning Variant** — If retention, write save offers, pause copy, payment recovery, exit survey, and win-back copy. → output: `retention-sequence.md`

### Phase 4: QA & Experiment Plan

**Lead agent:** bmad-growth-analyst

1. **QA Checklist** — Verify segmentation, tokens, links, unsubscribe, tracking, attribution, frequency, and suppression. Block send until every QA item is checked off. → output: `email-qa-checklist.md` → gate: `user_approval`
2. **Experiment Backlog** — Define tests for subject, offer, cadence, CTA, segment, and timing. → output: `lifecycle-experiment-backlog.md`

### Completion

Append a final **Summary** to `outputFile`, then recommend `bmad-growth-audit` or `bmad-revops-enablement-sprint` based on operational gaps.

