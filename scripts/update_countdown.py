#!/usr/bin/env python3
"""Regenerate the countdown block in README.md and assets/countdown.svg.

Honesty note: GitHub READMEs cannot run JavaScript, so a true real-time
countdown is impossible. This script is executed hourly by
.github/workflows/countdown.yml and rewrites the numbers — that is the
closest honest approximation. Deadline: 2026-07-07 00:00 Europe/Rome.
"""
import pathlib
import re
from datetime import datetime
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Rome")
DEADLINE = datetime(2026, 7, 7, 0, 0, tzinfo=TZ)
ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
SVG = ROOT / "assets" / "countdown.svg"

SVG_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="420" height="60" role="img" aria-label="countdown">
  <rect width="420" height="60" rx="8" fill="#0d1117"/>
  <text x="210" y="26" text-anchor="middle" font-family="Menlo, monospace" font-size="20" fill="#f0f6fc">{line1}</text>
  <text x="210" y="48" text-anchor="middle" font-family="Menlo, monospace" font-size="11" fill="#8b949e">{line2}</text>
</svg>
"""


def main():
    now = datetime.now(TZ)
    left = DEADLINE - now
    if left.total_seconds() <= 0:
        md = "**The deadline has passed. Fable is gone — the benchmark and the skill live on.**"
        line1, line2 = "TIME'S UP", "Fable retired 2026-07-07"
    else:
        days = left.days
        hours, rem = divmod(left.seconds, 3600)
        minutes = rem // 60
        md = (
            f"### ⏳ {days}d {hours}h {minutes:02d}m until Fable is retired\n\n"
            f"Deadline: **2026-07-07 00:00 Europe/Rome** · last refresh: "
            f"{now:%Y-%m-%d %H:%M %Z} · auto-updated hourly by GitHub Actions "
            f"(READMEs can't run JS, so this is as close to real time as it honestly gets)"
        )
        line1 = f"{days}d {hours}h {minutes:02d}m left"
        line2 = f"until 2026-07-07 00:00 Europe/Rome (hourly refresh)"

    readme = README.read_text(encoding="utf-8")
    new = re.sub(
        r"(<!-- COUNTDOWN:START -->).*?(<!-- COUNTDOWN:END -->)",
        rf"\1\n{md}\n\2",
        readme,
        flags=re.S,
    )
    README.write_text(new, encoding="utf-8")
    SVG.write_text(SVG_TEMPLATE.format(line1=line1, line2=line2), encoding="utf-8")
    print(f"countdown updated: {line1}")


if __name__ == "__main__":
    main()
