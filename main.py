#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original funny line to /output/entry.txt.
Deterministic, standard library only, no network access.
"""

from pathlib import Path

LINE = "My phone's screen-time report now just says 'we need to talk.'"

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line out of bounds"


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
