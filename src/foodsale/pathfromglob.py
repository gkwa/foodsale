import os
import pathlib
from typing import List


def abspathglobs(globstrings) -> List[pathlib.Path]:
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
        g = pathlib.Path(p1.anchor).glob(p2)
        lst = list(g)
    finally:
        os.chdir(cwd)
    return lst


def main():
    pass


if __name__ == "__main__":
    main()
