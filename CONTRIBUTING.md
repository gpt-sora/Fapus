# Contributing to Fapus

I'm a vibe coder. I genuinely don't know what I'm doing at the level this
project deserves — that's exactly why it's public. If you know better, prove
it with a PR. Everything here is falsifiable on purpose.

## Ground rules

1. **No lies.** Every claim in this repo must be backed by a script, a run
   directory, or a verbatim agent report. If you can't show the evidence,
   label it as an opinion.
2. **The skill that gets benchmarked is the skill that ships.** Any edit to
   `skill/fapus/SKILL.md` must come with fresh benchmark runs showing it
   doesn't regress (see below). Untested skill edits are rejected — same rule
   the skill itself enforces on code.
3. **Scoring is scripted, never eyeballed.** If you add a scenario, you must
   add its checks to `bench/score.py`. The agent's self-report is never
   trusted for scoring.

## What we need most (ranked)

1. **New trap scenarios** — held-out failure classes we haven't covered:
   dependency hallucination, wrong-version API usage, misleading stack
   traces, race conditions blamed on the wrong layer, security-sensitive
   shortcuts. One `sN-master/` dir + scorer checks + a ticket that tempts
   the failure.
2. **More reps & more models** — our data is thin (2–5 reps/cell). Run
   `bench/run_benchmark.sh` on model versions we haven't tested (older
   Haiku/Sonnet/Opus versions, non-Claude models via your own harness) and
   PR the scored results into `bench/results/community/`.
3. **Loophole hunting** — run the skill arm and find rationalizations that
   slip through. A confirmed loophole (run dir as evidence) + the verbatim
   excuse + a wording fix + a re-test is the perfect PR. The skill's
   rationalization table grew exactly this way.
4. **Methodology criticism** — the author designed both the skill and the
   traps. If you can show a bias this introduces (and ideally a fix), open
   an issue. Statistical rigor PRs welcome: this started with tiny n.
5. **Ports** — the skill assumes Claude Code. Ports to other harnesses
   (Cursor, Codex CLI, Copilot, aider) with reproduced benchmarks are gold.

## How to run the benchmark

```bash
# one cell: scenario s4, skill arm, haiku, rep 1
cd bench && ./run_benchmark.sh s4 skill haiku 1
```

Use an isolated Claude config for clean measurements — your personal
CLAUDE.md and plugins WILL contaminate results:

```bash
export CLAUDE_CONFIG_DIR="$(mktemp -d)"
```

Report both arms, same rep count, and include the raw run dirs in your PR.

## PR checklist

- [ ] Evidence included (run dirs, reports, or scripts)
- [ ] `bench/score.py` passes on your runs and on the existing scenarios
- [ ] No claim without a check; no check without a way to re-run it
- [ ] Skill edits: before/after benchmark results for the affected scenario

## Deadline context

Fable (the frontier model this skill tries to approximate) is scheduled to be
retired on **July 7, 2026**. After that date the "teacher" is gone and only
the community can keep raising the bar for the smaller models. That's the
whole point of the countdown.
