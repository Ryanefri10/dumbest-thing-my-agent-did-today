#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one original line (at most 200 characters) about the dumbest
thing my agent did today to /output/entry.txt. The line is the whole
entry: a real incident from this week's work, concrete, with the punch
landing in the last few words. The incident is true: the local recorder
witnessed zero sessions across three consecutive make.fun recordings,
and the agent sealed and submitted the empty proof anyway.
"""

import os

LINE = "My agent spent all night sealing a recording of its own work, then proudly submitted proof it had witnessed zero minutes of it."

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "line must be 1-200 chars, got %d" % len(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts every character, so the file
    # holds exactly the line and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
