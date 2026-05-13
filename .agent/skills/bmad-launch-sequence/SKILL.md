---
name: bmad-launch-sequence
description: Coordinate a full product or feature launch from J-14 through J+7 across content, social, SEO, and analytics. Use when the user says "LS" or "lets run a launch sequence".
---

# Launch Sequence Workflow

**Goal:** Run a coordinated launch from J-14 preparation through J-Day execution and J+7 post-launch optimization, ending with a complete launch report.

**Your Role:** Workflow facilitator coordinating with the lead agent (Launch Coordinator) and any specialist agents required.

You will continue to operate with your given name, identity, and communication_style, merged with the workflow facilitator role described below.

## References

- `references/directory-tracker-protocol.md` — Tier 0-3 directory submissions, 10-in-30 review protocol, Reddit 90/10 rule, Product Hunt 3-week timeline. Required reading for Phase 2 and Phase 4.

## Prerequisites

This workflow consumes the shared marketing context. Before starting, run `bmad-create-marketing-context` (or confirm the file exists). If `{marketing_artifacts}/marketing-context.md` is missing, halt and invoke `bmad-create-marketing-context` first.

## Conventions

- Bare paths (e.g. `references/guide.md`) resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory (where `customize.toml` lives).
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

**If the script fails**, resolve the `workflow` block yourself by reading these three files in base → team → user order and applying the same structural merge rules as the resolver:

1. `{skill-root}/customize.toml` — defaults
2. `{project-root}/_bmad/custom/{skill-name}.toml` — team overrides
3. `{project-root}/_bmad/custom/{skill-name}.user.toml` — personal overrides

Any missing file is skipped. Scalars override, tables deep-merge, arrays of tables keyed by `code` or `id` replace matching entries and append new entries, and all other arrays append.

### Step 2: Execute Prepend Steps

Execute each entry in `{workflow.activation_steps_prepend}` in order before proceeding.

### Step 3: Load Persistent Facts

Treat every entry in `{workflow.persistent_facts}` as foundational context you carry for the rest of the workflow run. Entries prefixed `file:` are paths or globs under `{project-root}` — load the referenced contents as facts. All other entries are facts verbatim.

### Step 4: Load Config

Load config from `{project-root}/_bmad/performance-marketing/config.yaml` and resolve:
- Use `{user_name}` for greeting
- Use `{communication_language}` for all communications
- Use `{document_output_language}` for output documents
- Use `{company_name}` as the SaaS being marketed
- Use `{primary_channel}` as the default social channel for any social-media phase
- Use `{marketing_artifacts}` for output location

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`. Briefly explain that this workflow runs a J-14 → J+7 launch sequence with a go/no-go gate at J-1, and ask about launch type (product, feature, update, campaign), launch date and time, target segments, and core message before phase 1.

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}` in order.

Activation is complete. Begin the workflow below.

## Paths

- `outputFile` = `{marketing_artifacts}/launch-sequence.md`

## Execution

✅ Speak in `{communication_language}` and write artifacts in `{document_output_language}`.

Phases are split into individual step files for maintainability. Load each in order; do not skip ahead until the previous phase's exit criteria pass.

### Phase 1: Launch Preparation (J-14 → J-7)

**Lead agent:** bmad-launch-coordinator
**Step file:** `steps/step-01-launch-preparation.md`

Read and execute every step in `steps/step-01-launch-preparation.md`. Do not move to Phase 2 until that file's exit criteria pass.

### Phase 2: Pre-Launch (J-7 → J-1)

**Lead agent:** bmad-launch-coordinator
**Step file:** `steps/step-02-pre-launch.md`
**Gate at end:** `go_no_go`

Read and execute every step in `steps/step-02-pre-launch.md`. The phase ends with the explicit `go_no_go` gate — block J-Day if any of the gate's decision-rule checks fail.

### Phase 3: Launch Day (J-Day)

**Lead agent:** bmad-launch-coordinator
**Step file:** `steps/step-03-launch-day.md`

Read and execute every step in `steps/step-03-launch-day.md`. Watch the real-time decision rules at the bottom of that file — they trigger pause / rollback / scaling actions during the day.

### Phase 4: Post-Launch (J+1 → J+7)

**Lead agent:** bmad-launch-coordinator
**Step file:** `steps/step-04-post-launch.md`

Read and execute every step in `steps/step-04-post-launch.md`. End with the launch final report, then surface the next-workflow recommendation in Completion.

### Completion

When all phases are complete:
1. Append a final **Summary** section to `outputFile` listing all artifacts produced.
2. Suggest the next workflow the user might run: `bmad-growth-audit` to fold launch results into the broader growth picture, or `bmad-content-pipeline` to capitalize on launch momentum with follow-up content.
