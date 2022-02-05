import logging
import os
import pathlib


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
            p1 = pathlib.Path(self._str)
            x = str(p1).lstrip(p1.drive)
            x = str(x).lstrip(p1.root)
            root = pathlib.Path("/")
            z = f"*{x}"
            if self.drive:
                os.chdir(p1.drive)
            y = pathlib.Path("/").glob(z)  # y is a generator
            paths = list(y)  # consumes the generator
            logging.debug(paths)
            if not paths:
                logging.warning("couldn't find a match for {}".format(self.ps))
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
        self.root = None
        self.globs_str = _str
        self.path = None
        self.initialize(_str)

    def initialize(self, _str):
        candidates = []
        for line in _str.splitlines():
            logging.debug("line:{}".format(line))
            clean = self.clean(line)
            logging.debug("path:{}".format(clean))
            if not clean:
                continue
            nrg = NonRelativeGlob(clean)
            logging.debug(nrg.path)
            if nrg.path:
                candidates.append(nrg.path)

        if candidates:
            self.path = candidates[-1]

    @classmethod
    def from_string(cls, _str):
        return cls(_str)

    def clean(self, line):
        return line.strip()
