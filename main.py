"""Entry point: write the catalogue photograph to /output/entry.png.

UNDO-1 edition: the tabletop undo machine is caught mid-use, its
rider half old, half young again, a split-second after the UNDO press.
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
