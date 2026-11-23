#!/usr/bin/env python3
"""Entry point for the news-image-20261123 bounty (Python 3.13, stdlib only).

Copies the entry.png beside this file to the output directory
($MAKEFUN_OUTPUT_DIR, or /output by default), so both grader runs write
the same bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
