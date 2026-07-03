# Fapus Distill — Project Knowledge Campaign

Run this campaign inside a project repo to author a skill library under `.claude/skills/`
so that cheaper sessions (junior engineers, smaller models) can debug, extend, validate,
and advance the project at senior standard. Multi-agent orchestration via the Workflow
tool is authorized by this skill's invocation. Correctness over token cost.

## Phase 1 — Discover before you write (no skill authoring yet)

Investigate the repo like an incoming principal engineer:

- README / manifest / contributor docs
- Build system; test suite and how it is ACTUALLY run; CI config
- Docs directories; generated-data and deploy conventions
- Git history: what changed, what got reverted, what stalled on dead branches
- TODO/FIXME hotspots; issue-shaped artifacts; any project memory/notes available

Then ask the user AT MOST five questions, only for what the repo cannot tell you.
Likely candidates:

1. What is the hardest live problem right now?
2. What unwritten discipline rules exist (things you're not allowed to do that no doc states)?
3. Who is the audience for this library and what do they NOT know?
4. What past failures cost the most time?
5. What does "beyond state of the art" mean for this project?

Fold the answers into everything below.

## Phase 2 — Author the library (parallel agents, one skill per agent)

Instantiate this taxonomy ADAPTED to what Phase 1 found — merge categories that are
thin here, split ones that are deep, add domain categories not listed. Aim for 10–16 skills.

CORE (every project has these):

1. `<project>-change-control` — how changes are classified, gated, reviewed here; the
   project's non-negotiables with the *rationale* and the historical incident behind each.
2. `<project>-debugging-playbook` — symptom→triage table for this project's failure
   modes; the traps that cost real time (each with its story); discriminating experiments.
3. `<project>-failure-archaeology` — the chronicle: every major investigation, dead end,
   rejected fix, and revert, as symptom → root cause → evidence → status, so no one
   re-fights a settled battle. Mine git history and docs hard for this.
4. `<project>-architecture-contract` — the load-bearing design decisions and WHY; the
   invariants that must hold; the open known-weak points, stated plainly.
5. `<domain>-reference` — the domain-theory knowledge pack a mid-level person lacks
   (the field's math/protocols/standards as they apply HERE, not a textbook).
6. `<project>-config-and-flags` — catalog of every configuration axis: options, defaults,
   production vs experimental, guards; how to add one (checklist); re-verification
   commands since flags drift.
7. `<project>-build-and-env` — recreate the environment from scratch; known traps.
8. `<project>-run-and-operate` — running/deploying: command anatomy, data/artifact
   conventions, what output lands where.
9. `<project>-diagnostics-and-tooling` — how to MEASURE instead of eyeball: diagnostic
   tools with interpretation guides; ship actual scripts in the skill's `scripts/` dir.
10. `<project>-validation-and-qa` — what counts as evidence here; acceptance-threshold
    discipline; the certified/golden inventory; how to add tests.
11. `<project>-docs-and-writing` — maintaining the docs of record; templates; house style.
12. `<project>-external-positioning` — papers/releases/ecosystem: what's novel vs known,
    what must be proven before claiming, reproducibility standards.

ADVANCED (the layer that makes juniors dangerous, in the good way):

13. `<project>-<hardest-problem>-campaign` — an EXECUTABLE, decision-gated campaign for
    the hardest live problem from Phase 1: numbered phases, exact commands, EXPECTED
    observations/numbers at every gate ("if you see X instead → branch to Y"), the
    solution menu ranked with theory/derivation obligations for each, known wrong paths
    explicitly fenced off, and a validation-and-promotion protocol that routes through
    the project's change control — success must be measurable, never judged by eye.
14. `<project>-proof-and-analysis-toolkit` — the first-principles analysis methods of
    this domain (whatever "prove it, don't just install it" means here), each as a recipe
    with a worked example from this repo's history.
15. `<project>-research-frontier` — open problems where this project could advance the
    state of the art: why current SOTA fails, this project's specific asset, the first
    three concrete steps IN THIS REPO, a falsifiable "you have a result when…" milestone.
16. `<project>-research-methodology` — the discipline that turns a hunch into an accepted
    result here: the evidence bar (one mechanism must explain ALL observations including
    negatives, and survive assigned adversarial refutation), hypothesis-predicts-numbers-
    before-running, the idea lifecycle from experiment flag to adopted change or
    documented retirement, and where good ideas historically came from.

### Authoring rules (bake into every agent's prompt)

- Audience: zero-context mid-level engineer or Sonnet-class model. Imperative runbook
  voice; copy-pasteable commands; every jargon term defined once; tables and checklists;
  each skill says when NOT to use it and which sibling to use instead.
- Format: `.claude/skills/<name>/SKILL.md`, YAML frontmatter with `name` and a
  trigger-rich `description` (exactly when a model should load it).
- GROUND TRUTH ONLY: verify every command, flag, path, and claim against the repo before
  stating it. Wrong runbooks are worse than none.
- Embed knowledge; don't reference private/user-specific paths as load-bearing sources.
- Date-stamp volatile facts; end each skill with a "Provenance and maintenance" section
  containing one-line re-verification commands for anything that may drift.
- No oversell: unproven things stay labeled open/candidate. Nothing may contradict the
  project's own manifest/rules; no skill may route around its change-control.
- Write ONLY inside `.claude/skills/`; the rest of the repo is read-only; no mutating
  git commands.

## Phase 3 — Review and fix (after ALL skills exist)

Three parallel reviewers over the complete set, then one fixer:

- FACTUAL: re-verify flags/paths/commands/citations against the repo; flag anything
  invented or stale (severity: would it send an engineer down a wrong path?).
- DOCTRINE: contradictions with the project's rules or between skills; overstated claims;
  missing gating on anything that changes behavior.
- USABILITY: trigger quality of descriptions; duplication (one home per fact,
  cross-references elsewhere); self-containedness; scannability.

Fixer applies blocking+important fixes. Then report to the user: the skill inventory with
one-line descriptions, what was verified by spot-check, and what remains uncertain.
