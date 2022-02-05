import logging
import os
import pathlib
from typing import List


class NonRelativeGlob:
    def __init__(self, _str):
        self.glob = None
        self.cwd = pathlib.Path.cwd()
        self._str = _str
        self.drive = pathlib.Path(_str).drive
        self.path = None
        self.initialize(_str)

    def initialize(self, _str):
        try:
            p1 = pathlib.PureWindowsPath(self._str)
            logging.debug(type(p1))
            logging.debug(p1)
            logging.debug(f"{p1.drive=}")
            logging.debug(f"{p1.root=}")
            x = str(p1).lstrip(p1.drive)
            logging.debug(x)
            x = str(x).lstrip(p1.root)
            logging.debug(f"{x=}")
            root = pathlib.Path("/")
            logging.debug(f"{root=}")
            z = f"*{x}"
            logging.debug(f"{z=}")
            if self.drive:
                os.chdir(p1.drive)
            y = pathlib.Path("/").glob(z)  # y is a generator
            logging.debug(f"{y=}")
            paths = list(y)  # consumes the generator
            logging.debug(f"{paths=}")
            if not paths:
                logging.warning("couldn't find a match for {}".format(self._str))
            else:
                # naively choose one with higest version number
                last = paths[-1]
                last = last.resolve()
                logging.debug("using file with path {}".format(last))
                self.path = last

        except BaseException as ex:
            logging.exception(ex)
            raise

        finally:
            os.chdir(self.cwd)


class PathFromGlob:
    """
    # multiline string like this

    C:/Program*/Microsoft SDKs/Windows/v[!6]*/Bin/SignTool.exe
    C:/Program*/Windows Kits/*/bin/*/*/SignTool.exe

    or single glob like this:
    C:/Program*/Windows Kits/*/bin/*/*/SignTool.exe

    or this:
    */Program*/Windows Kits/*/bin/*/*/SignTool.exe
    """

    def __init__(self, _str):
        logging.debug(_str)
        self.root = None
        self.globs_str = _str
        self.path = None
        self.initialize(_str)

    def multiline(self, _str) -> List[pathlib.Path]:
        candidates = []
        for line in _str.splitlines():
            clean = line.strip()
            if not clean:
                continue
            nrg = NonRelativeGlob(clean)
            logging.debug(nrg.path)
            if nrg.path:
                candidates.append(nrg.path)
        return candidates

    def initialize(self, _str):
        candidates = self.multiline(_str)

        if candidates:
            self.path = candidates[-1]

    @classmethod
    def from_string(cls, _str):
        return cls(_str)


def main():
    _str = r"C:\Program*\WiX Toolset*\bin\heat.exe"
    p1 = PathFromGlob(_str)
    print(p1)


if __name__ == "__main__":
    main()
