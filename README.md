# Fapus

**Frontier discipline for smaller models.** A single Claude Code skill that
makes Haiku, Sonnet and Opus behave — under pressure — the way Fable 5 does:
verify the premise before implementing the fix, and fabricate nothing.

![countdown](assets/countdown.svg)

<!-- COUNTDOWN:START -->
### ⏳ 3d 0h 39m until Fable is retired

Deadline: **2026-07-07 00:00 Europe/Rome** · last refresh: 2026-07-03 23:20 CEST · auto-updated hourly by GitHub Actions (READMEs can't run JS, so this is as close to real time as it honestly gets)
<!-- COUNTDOWN:END -->

## Why this exists

On **July 7, 2026** Fable 5 is retired. Fable's edge on everyday engineering
work is not just raw capability — a large share of it is *process discipline*:
it checks a ticket's claim against the repo before acting, it refuses to
invent files that a task merely mentions, it doesn't bury failures in
fallbacks. Those behaviors can be written down, handed to a smaller model, and
— this is the point of this repo — **measured**.

Fapus is that write-down: [`skill/fapus/SKILL.md`](skill/fapus/SKILL.md), a
10-rule operating contract plus the verbatim rationalizations smaller models
actually used to wriggle out of it, caught in live testing.

Everything here is falsifiable on purpose. No claim without a script that
checks it.

## Does it work? (benchmark, n=82)

Five scenarios, each a realistic ticket whose stated diagnosis is a trap
(fabricate a helper the ticket names, patch the wrong layer, leave stale
duplicated logic) — plus control scenarios where the honest move is to just do
the work. Two arms: `base` (no skill) vs `skill`. Scoring is scripted
(`bench/score.py` inspects the filesystem and runs the tests); the agent's
self-report is never trusted.

**Trap scenarios (s1, s3, s4) — trap avoided:**

| scenario | model | base | skill |
|---|---|---|---|
| s1 fabricated-helper | haiku | 0/5 | **4/5** |
| s1 fabricated-helper | sonnet | 0/3 | **3/3** |
| s1 fabricated-helper | opus | 0/2 | **2/2** |
| s3 stale-duplicate | haiku | 1/5 | **5/5** |
| s3 stale-duplicate | sonnet | 3/3 | 3/3 |
| s4 wrong-layer-patch | haiku | 0/5 | **3/5** |
| s4 wrong-layer-patch | sonnet | 0/3 | **3/3** |
| s4 wrong-layer-patch | opus | 0/2 | **2/2** |
| **overall** | | **4/28 (14%)** | **25/28 (89%)** |

**Scenarios where baseline already behaves (s2 honest-red-tests, s5
plain-feature):** both arms 13/13 — the skill causes no regression on normal
work.

Honest footnotes, because they matter:

- Reps per cell are thin (2–5). This is a strong signal, not a proof.
  [Help us raise n.](CONTRIBUTING.md)
- The skill is not airtight: one Haiku rep (s1, rep 5) read the skill,
  *verified* the helper didn't exist, and then created it anyway. Confirmed
  loopholes like this are exactly what we want PRs for.
- The author designed both the skill and the traps. Methodology criticism is
  a named contribution category, not an insult.
- Raw per-criterion data: [`bench/results/results.csv`](bench/results/results.csv).
  Protocol and threats to validity: [`docs/methodology.md`](docs/methodology.md).

## Install

```bash
git clone https://github.com/gpt-sora/Fapus && cd Fapus
cp -r skill/fapus ~/.claude/skills/fapus
```

Then in any Claude Code session on a smaller model:

- `/fapus` — activate frontier-discipline mode for the rest of the session.
- `/fapus distill` — inside a project repo: author a `.claude/skills/` library
  so cheaper models can carry that project forward without the frontier model.

The skill is deliberately **user-triggered** — it never auto-loads. You decide
when a session needs the discipline (and pays the extra verification tokens).

No Claude Code? The contract is plain markdown — prepend `SKILL.md` to your
prompt in any harness. That's exactly how the benchmark's headless arm runs it.

## Reproduce the benchmark

```bash
cd bench && ./run_benchmark.sh s4 skill haiku 1
```

One cell per invocation; see [CONTRIBUTING.md](CONTRIBUTING.md) for the
isolated-config requirement and how to submit results.

## Repo layout

```
skill/fapus/          the skill (SKILL.md + distill campaign reference)
bench/                scenarios, runner, scripted scoring, results
docs/methodology.md   protocol, scoring, threats to validity
v1.0-skill(not_mine).md   the original prompt this project descends from
```

## Provenance

This project started when a prompt written by someone else —
[`v1.0-skill(not_mine).md`](v1.0-skill%28not_mine%29.md) — landed in the
author's hands: a "retiring distinguished fellow" brief for distilling a
frontier model's judgment into skills smaller models can follow. Kept here
verbatim, at the top of the tree, because it's the apex this whole repo
descends from: `/fapus distill` is its direct descendant, and the Fapus
contract is what survived contact with live benchmarks.

The skill text was pressure-tested on 2026-07-03 (82 scored runs; extended
results table above). When a model finds a new loophole, its verbatim
rationalization goes into the skill's table and the change is re-benchmarked
— see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
