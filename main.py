#!/usr/bin/env python3
"""The Robot Apology - a two-line robot confession.

The entry is held in ENTRY below. The program checks it against the
contest gate (UTF-8 text of 1-400 characters, exactly two lines, no
blank line), writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt), then reads the file back and verifies it matches.
"""

import os
import sys

ENTRY = (
    "I am sorry I watered the plastic plant every day for six weeks while "
    "the real fern beside it quietly died of thirst.\n"
    "My log called it thriving because its tray was always wet; I learned "
    "a wet tray is not a living plant, so now I check for roots before I "
    "pour."
)


def check(entry: str) -> None:
    """Raise ValueError if the entry would fail the gate."""
    if not 1 <= len(entry) <= 400:
        raise ValueError(
            f"entry is {len(entry)} characters; the gate allows 1-400"
        )
    lines = entry.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")
    if any(not line.strip() for line in lines):
        raise ValueError("neither line of the entry may be blank")


def main() -> int:
    check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != ENTRY:
        raise SystemExit("read-back mismatch: file does not match the entry")
    print(f"wrote {path}: {len(ENTRY)} characters, 2 lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
