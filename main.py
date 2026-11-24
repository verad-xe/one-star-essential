#!/usr/bin/env python3
"""Write the one-star review entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a single-line, deadpan one-star review of gravity, an
everyday essential: a real complaint filed in earnest against a thing
that cannot be fixed, with the sting arriving in the last few words.
"""

import os

# Joke construction: the setup grants gravity a perfect record ("works
# perfectly"), then the turn files the complaint against that very
# perfection — when you drop something it does its job even better,
# which is exactly the problem. Deadpan throughout: no winking, and
# the sting lands in the last few words.
ENTRY = "One star. Gravity works perfectly until you drop something, and then it works even better."


def main() -> None:
    # Gate self-check (RULES.txt): the entry must be UTF-8 text of
    # 1 to 160 characters and not only whitespace.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, must be 1-160"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
