#!/usr/bin/env python3
"""Write the one-star review entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a single-line, deadpan one-star review of gravity, an
everyday essential: a real complaint filed in earnest against a thing
that cannot be fixed, with the sting arriving in the last few words.
"""

import os

ENTRY = "One star. Gravity works perfectly until you drop something, and then it works even better."


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
