#!/usr/bin/env python3
"""make.fun news-image-20261118 entry (Python 3.13, standard library only).

The entry image is the entry.png held in this repository: a newspaper-style
front page summing up the world's news of Wednesday 18 November 2026, drawn
with real rendered text (PIL + DejaVu). This program deterministically copies
it to /output/entry.png. No network access.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SOURCE = Path(__file__).resolve().with_name("entry.png")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SOURCE, OUTPUT_DIR / "entry.png")
