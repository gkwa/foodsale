import os
import pathlib
from typing import List


def abspathglob(*sglobs) -> List[pathlib.Path]:
    paths = set()
    cwd = pathlib.Path.cwd()
    for _str in sglobs:
        p1 = pathlib.Path(_str)
        p2 = str(p1).lstrip(p1.anchor)
        try:
            os.chdir(p1.anchor)
            g = pathlib.Path(p1.anchor).glob(p2)
            for path in list(g):
                paths.add(path)
        finally:
            os.chdir(cwd)

    return list(paths)


def main():
    pass


if __name__ == "__main__":
    main()
