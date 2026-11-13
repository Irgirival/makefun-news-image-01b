#!/usr/bin/env python3
"""news-image-01 entry: copy the prepared front-page image to the output dir.

Reads image.png sitting next to this script and writes it, byte for byte,
as entry.png inside MAKEFUN_OUTPUT_DIR (default /output). Deterministic:
the same input always produces the same output. No image processing is
done here — the front page was composed beforehand and is copied as-is.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    source = HERE / "image.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
