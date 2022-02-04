import pathlib

from foodsale import pathfromglob

"""
>>> import pathlib
>>> import os
>>>
>>> _str = r"C:\Program*\WiX Toolset*\bin\heat.exe"
>>> 
>>> x = str(p1).lstrip(p1.drive)
>>> x = str(x).lstrip(p1.root)
>>> root = pathlib.Path("/")
>>> z = f"*{x}"
>>> print(z)
*Program*\WiX Toolset*\bin\heat.exe
>>> os.chdir("c:")
>>> y = pathlib.Path("/").glob(z)
>>> print(y)
<generator object Path.glob at 0x0000026FE9F96820>
>>> print(list(y))
[WindowsPath('/Program Files (x86)/WiX Toolset v3.11/bin/heat.exe')]
>>>
"""


def test1():
    _str = r"C:\Program*\WiX Toolset*\bin\heat.exe"
    p1 = pathfromglob.PathFromGlob(_str)
    print(p1.drive)


def test():
    x = "C:/Program*/Windows Kits/*/bin/*/*/SignTool.exe"
    y = pathfromglob.PathFromGlob(x)
    print(y)


def test_pathfromglob():
    def rmtree(root):
        if not root.exists():
            return

        for p in root.iterdir():
            if p.is_dir():
                rmtree(p)
            else:
                p.unlink()
        root.rmdir()

    root = pathlib.Path("/tmp/signit_test_1")
    rmtree(root)

    test = root / "test.txt"
    test.parent.mkdir(parents=True, exist_ok=True)
    test.write_text("")

    path = pathfromglob.PathFromGlob.from_string("t*/sig*/test.txt").path
