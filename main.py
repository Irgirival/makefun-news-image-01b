#!/usr/bin/env python3
"""news-image-01 entry (Python 3.13, standard library only): copies image.png to /output/entry.png."""
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "image.png"
dst = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, dst)
