#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest — make.fun entry.

Writes one pickup line a vending machine would say to a passing human to
/output/entry.txt. Stdlib only, no network, no API key.

The line was chosen by pairwise judging (Caffeine inference router, kit's
judge brief) over 6 drafted candidates: it won all 3 of its pairings
(margins 4, 2, 4).
"""

import os

LINE = "Press B7 and I'll fall for you. Literally. My coil's been waiting all day to drop something sweet."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
