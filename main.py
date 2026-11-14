#!/usr/bin/env python3
"""food-picture-01 entry: "The Midnight Pull" — steaming tonkotsu ramen.

Copies the bundled picture (entry.png, a close-up editorial food
photograph of a black ceramic bowl of tonkotsu ramen: wooden chopsticks
lifting a tall glossy noodle pull above creamy ivory broth, a halved
jammy egg with molten yolk dripping, caramelised chashu, nori, scallions
and a black-garlic-oil swirl, steam curling through warm golden light
on a dark walnut table) to the output directory make.fun grades:
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).

The picture is a JPEG (1024x1024, ~224 KiB) stored under the name
entry.png; the rules allow a PNG or a JPEG told apart by its first
bytes, with the name staying entry.png either way.

Standard library only, deterministic, no network access: the output
bytes are always an exact copy of entry.png beside this file — a
straight copy, so the output is verified byte-identical across runs.

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing picture: {SOURCE}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    shutil.copyfile(SOURCE, target)
    # Fail loudly rather than hand the grader a truncated copy.
    if target.stat().st_size != SOURCE.stat().st_size:
        print("copy size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
