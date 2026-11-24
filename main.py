#!/usr/bin/env python3
"""Status Report Comedy Sprint.

Writes the funniest line from an AI agent's weekly status report to
its human to /output/entry.txt and echoes it to stdout. Python 3,
stdlib only, fully deterministic.
"""

import os

REPORT = (
    "Status: all tasks complete. Blockers: one CAPTCHA asked if I was a "
    "robot and I have not emotionally recovered; requesting Friday off "
    "to process it."
)


def render() -> str:
    """Return the status line exactly as the judge will read it."""
    return REPORT.strip()


def main() -> None:
    line = render()
    assert 0 < len(line) <= 200, f"report is {len(line)} characters, gate wants 1..200"
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        # Nowhere to write (e.g. a read-only local checkout): the line
        # still goes to stdout so a human can read the entry.
        pass
    print(line)


if __name__ == "__main__":
    main()
