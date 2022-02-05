import os
import pathlib
import re
from typing import List


def abspathglob(*globs: List[str], remove_re: List[str] = None) -> List[pathlib.Path]:
    paths = set()

    for _str in globs:
        absolute = pathlib.Path(_str)
        relative = str(absolute).lstrip(absolute.anchor)
        cwd = pathlib.Path.cwd()
        try:
            os.chdir(absolute.anchor)
            glob = pathlib.Path(absolute.anchor).glob(relative)
        finally:
            os.chdir(cwd)

        for path in list(glob):
            paths.add(path)

    if remove_re:
        for path in paths:
            for regex in remove_re:
                if re.search(regex, str(path)):
                    paths.remove(path)

    return list(paths)


def main():
    pass


if __name__ == "__main__":
    main()
