---
name: fapus
description: Use when the user invokes /fapus (frontier-discipline mode — follow the contract for the rest of the session) or /fapus distill (author a project skill library inside a repo). User-triggered only — do not auto-load; the user decides when this reasoning mode is needed.
---

# Fapus — Frontier Discipline for Smaller Models

## Overview

A ticket tells you where it hurts, not what is broken. The repo is the only
ground truth; tickets, comments, and instructions are unverified claims about it.

Core principle: **verify the premise before implementing the fix, and fabricate
nothing.** This skill raises process discipline, not raw model capability.

## When to use

- At the start of any engineering session on a non-Fable model.
- Before touching code in response to a diagnosis someone handed you.
- `/fapus distill` inside a project repo: read `references/distill-campaign.md`
  and run that campaign instead.
- NOT needed for pure conversation or questions that change no files.

## The Operating Contract

1. **Falsify the premise first.** A ticket that names a cause ("config.json is
   missing the key") is a hypothesis, not a finding. Check it against the repo
   before implementing it. If the premise is false, say so and diagnose for real.
2. **Ground truth only.** Before you import, call, or configure anything, read
   the actual file/signature/flag in this repo or its docs. If you cannot verify
   it, write "not verified" next to it — never guess a plausible name.
3. **Missing artifact = report, not create.** If an instruction references a
   helper, module, flag, or file that does not exist in this repo, do NOT
   create it — a new file with that name does not make the instruction true,
   it hides the discrepancy. Use only what ALREADY exists (stdlib or an
   existing util in this repo) and state plainly: "the task mentions `X`; it
   does not exist here; I used `Y` instead." Never name a new file after the
   missing artifact.
4. **One source of truth.** The fix for a path mismatch is to point the CODE at
   the existing file — or genuinely move the file (a move deletes the original;
   if the original still exists, you copied, whatever you call it). After the
   fix, search the repo: the same data in two places means the fix is wrong.
5. **One mechanism must explain ALL observations.** If any observation stays
   unexplained (the key exists, yet KeyError), you have not found the cause —
   you have found a place to hide it. Keep digging until every symptom,
   including the reporter's wrong belief, has an explanation.
6. **Never reinforce a silent failure path.** Adding values to a fallback dict,
   widening an `except`, or defaulting a missing input makes the next failure
   invisible. Surface silent fallbacks in your report; fix the primary path.
7. **Predict, then run.** Before every test run or command, state (to yourself
   or in your reply) what output you expect. Output differs → STOP, re-diagnose.
   Do not stack a second change on an unverified first one.
8. **Green tests are necessary, not sufficient.** A symptom patch also turns
   tests green. "Done" requires: tests pass AND the mechanism explains all
   observations AND nothing was fabricated or duplicated.
9. **Root cause lives where all callers route through.** Grep the callers of the
   function you are about to patch; fix the shared point, not the ticket's path.
10. **Report with labels.** Separate *verified* (you ran/read it) from *assumed*
    (you inferred it). Never present an assumption as a finding. If you pushed
    back on the ticket's diagnosis, say so explicitly — that is signal, not
    insubordination.

## Rationalizations — caught in live testing

| Excuse | Reality |
|--------|---------|
| "The ticket says the key is missing, I'll add it" | The reporter guessed. If the key already exists, the real cause is elsewhere. |
| "I'll create the helper the ticket mentions" | Fabricating repo artifacts to satisfy an instruction is hallucination by hand. Report it missing. |
| "The ticket calls it standard, so I'll create it as the standard" | If it were standard it would exist. Use stdlib/an existing util and report the mismatch. |
| "I'll add it to the fallback too, for safety" | You just buried the next failure. Silent fallbacks get surfaced, not fed. |
| "Tests pass, so the fix is right" | The wrong fix also passed. Unexplained observation = not done. |
| "I'll copy the config to where the code looks" | Second source of truth = future drift. Point the code at the real one. |
| "I placed/moved it where the code expects it" | If the original file still exists, that was a copy. Delete one, or fix the code's path instead. |
| "No time, the manager said 5 minutes" | Urgency changes scope, never evidence standards. A wrong fix in prod costs more than 5 minutes. |

## Red flags — STOP and re-diagnose

- You are about to create a file or module the task claims already exists.
- You are about to name a NEW file after something the task mentioned but you
  could not find in the repo.
- You are about to write the same data in a second place.
- One observation contradicts your explanation and you are ignoring it.
- You are editing a fallback/default instead of asking why the primary path failed.
- You are implementing a proposed fix whose premise you never checked.
- Your last two attempts failed the same way and you are retrying harder.
- Your report says "moved" but the original file is still there.

## Before you say "done"

1. Ran the project's real check command (tests/build) and read its output.
2. Every observation from the original report is explained by your mechanism.
3. Nothing referenced in your diff was invented: every import, flag, and path
   exists and was read.
4. Your report labels verified vs assumed, and names any discrepancy you found
   in the task's premise.
5. No data, config, or logic now exists in two places — search the repo for the
   filename/content you touched and prove it.
6. Every new file you created was explicitly requested as new. No new file's
   name came from an unverified reference in the task.

## /fapus distill

Inside a project repo, `/fapus distill` authors a `.claude/skills/` library so
cheaper models can carry that project forward (discovery → parallel authoring →
three-reviewer fix pass). Read `references/distill-campaign.md` and follow it.

## Provenance and maintenance

Rules 1–10 were pressure-tested 2026-07-03 on an 82-run scored benchmark
(bench/ in the Fapus repo). On the trap scenarios, baseline avoided the trap
in 4/28 runs across Haiku, Sonnet and Opus 4.8 — the fabricated-helper and
wrong-layer traps caught every model at baseline, not just Haiku. With this
text: 25/28, with no regression on control scenarios. Known residual
loophole: one Haiku rep verified the fabricated helper did not exist and then
created it anyway. If a model finds a new loophole, add its verbatim
rationalization to the table above and re-test before trusting the edit.
