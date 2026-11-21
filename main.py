"""Entry point: write the catalogue photograph to /output/entry.png.

Mid-action finish-line edition: the SNAILPOWER treadmill is caught
mid-use, its rider a split-second from breaking the finish tape.
The photograph ships in this repository as asset.jpg, beside this file.
The program simply copies its bytes to the output path.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(HERE, "asset.jpg")
OUTPUT = os.path.join("/output", "entry.png")


def main() -> None:
    # The output directory may not exist yet in the grading sandbox.
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(ASSET, OUTPUT)


if __name__ == "__main__":
    main()
