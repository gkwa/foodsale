import os
import pathlib
from dataclasses import dataclass, field
from typing import List


def abspathglobs(globstrings):
    paths = []
    for _str in globstrings:
        paths.append(abspathglob(_str))
    return paths


def abspathglob(_str) -> List[pathlib.Path]:
    p1 = pathlib.Path(_str)
    p2 = str(p1).lstrip(p1.anchor)
    cwd = pathlib.Path.cwd()
    try:
        os.chdir(p1.anchor)
        p3 = pathlib.Path(p1.anchor).glob(p2)
    finally:
        os.chdir(cwd)
    return p3


def main():
    pass


if __name__ == "__main__":
    main()
