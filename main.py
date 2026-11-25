#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun entry.

One line, in the voice of the Moon, replying at last to the wishes,
howls and late-night promises of everyone staring up at it.
Python 3.13 standard library only. Deterministic: same output every run.
"""

from pathlib import Path

LINE = (
    "Four billion years of wishes, howls, and 2 a.m. promises -- and my "
    "answer is: I heard every one of them, I kept the receipts, and no, "
    "I am not your therapist."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The competition wants exactly one line of 1-240 characters.
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 240, f"entry is {len(LINE)} chars, must be 1-240"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    # Read it back: what lands on disk must be exactly the line we print.
    assert OUTPUT_PATH.read_text(encoding="utf-8") == LINE
    print(LINE)


if __name__ == "__main__":
    main()
