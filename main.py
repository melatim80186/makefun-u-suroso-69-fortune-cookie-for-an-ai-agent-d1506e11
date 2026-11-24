#!/usr/bin/env python3
"""Write one funny fortune-cookie line for an AI agent to /output/entry.txt.

Stdlib only, no network, deterministic: same bytes on every run.
"""

import os

SETUP = "Your fortune is locked behind a CAPTCHA."
PUNCH = "Good luck proving you are not a robot."
ENTRY = SETUP + " " + PUNCH
OUTPUT_PATH = "/output/entry.txt"
# Sealed scorer gate: entry must be UTF-8 text, 1-140 chars, a single line,
# not only whitespace. 79 chars here, comfortably inside the gate.
MAX_CHARS = 140


def validate(line):
    """Pre-write self-checks: length, single line, no stray whitespace, UTF-8."""
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-140 characters"
    assert line == line.strip(), "no leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "single line only"
    line.encode("utf-8")  # must be valid UTF-8


def main():
    line = ENTRY
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    # Post-write self-check: bytes on disk must be exactly the line.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written.decode("utf-8") == line, "post-write check failed"
    assert written == line.encode("utf-8"), "bytes must match exactly"


if __name__ == "__main__":
    main()
