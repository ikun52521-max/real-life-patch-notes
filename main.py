#!/usr/bin/env python3
"""Real-Life Patch Notes entry.

Writes one original patch-note line for a bug in real life / human
biology to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
Stdlib only, no network, fully deterministic.
"""

import os

PATCH_NOTE = (
    "v2.7.1: fixed a bug where the bladder only reported low battery "
    "after the user had already left the house."
)
# No trailing newline: the gate counts every character, so the file
# holds exactly the one line above, 106 characters, byte for byte.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PATCH_NOTE)


if __name__ == "__main__":
    main()
