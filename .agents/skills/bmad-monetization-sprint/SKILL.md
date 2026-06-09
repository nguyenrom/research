---
name: bmad-monetization-sprint
description: Run pricing, packaging, value metric, freemium/trial, monetization, pricing page, and paywall/upgrade strategy work. Use when the user says "MNS" or needs monetization strategy.
---

# Monetization Sprint Workflow

**Goal:** Produce a pricing and monetization plan that aligns buyer segments, value delivered, package structure, upgrade moments, and experiment path.

**Your Role:** Workflow facilitator coordinating with the Monetization Strategist, CRO Strategist, Growth Analyst, Content Architect, and RevOps Strategist.

## References

- `references/paywall-trigger-taxonomy.md` — 4-category trigger taxonomy (feature gate / usage limit / trial expiration / time-based), Respect-the-No rule, frequency caps, dark-pattern blacklist, screen design 5 elements. Required reading for Phase 3 (Conversion Surfaces).

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

Greet `{user_name}`, speaking in `{communication_language}`. Ask whether the decision is about price level, packaging, value metric, free plan/trial, annual discount, pricing page, paywall, or upgrade path.

### Step 6: Execute Append Steps

Execute `{workflow.activation_steps_append}`.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/monetization-sprint.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

### Phase 1: Monetization Baseline

**Lead agent:** bmad-monetization-strategist

1. **Current Pricing Audit** — Capture plans, prices, value metric, limits, trial/free plan, conversion, churn, expansion, and buyer objections. → output: `pricing-audit.md`
2. **Segment & Willingness Evidence** — Map buyer segments, use cases, budget owners, alternatives, willingness signals, and evidence gaps. → output: `willingness-evidence.md`

### Phase 2: Package Strategy

**Lead agent:** bmad-monetization-strategist

1. **Value Metric Scorecard** — Score candidate value metrics by value alignment, predictability, fairness, simplicity, and measurability. → output: `value-metric-scorecard.md`
2. **Tier & Packaging Map** — Define packages, feature fences, usage limits, buyer segments, expansion logic, and downgrade risk. Present packaging proposal and downgrade-risk analysis to user before pricing-page work. → output: `package-map.md` → gate: `user_approval`
3. **Trial / Freemium Decision** — Evaluate free plan, trial, reverse trial, usage caps, sales-led demo, and hybrid options. → output: `free-trial-freemium-decision.md`

### Phase 3: Conversion Surfaces

**Lead agent:** bmad-cro-strategist + bmad-content-architect

1. **Pricing Page Copy** — Draft pricing page hierarchy, plan names, CTAs, comparison table, FAQs, proof, and objection handling. → output: `pricing-page-copy.md`
2. **Paywall / Upgrade Moments** — Define upgrade triggers, message, proof, offer, fallback, and tracking. → output: `paywall-upgrade-plan.md`

### Phase 4: Experiment & Rollout

**Lead agent:** bmad-growth-analyst + bmad-revops-strategist

1. **Experiment Plan** — Define pricing tests, package tests, paywall tests, cohorts, metrics, risk controls, and decision rules. → output: `monetization-experiment-plan.md`
2. **Rollout Plan** — Define customer communication, grandfathering, sales enablement, billing/CRM changes, and support handling. Confirm legal, finance, and support readiness before customer comms go live. → output: `pricing-rollout-plan.md` → gate: `rollout_readiness`

### Completion

Append a final **Summary** to `outputFile`, then recommend `bmad-cro-sprint` for page/upgrade optimization or `bmad-revops-enablement-sprint` for sales rollout.

