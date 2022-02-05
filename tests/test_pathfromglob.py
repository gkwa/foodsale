import pathlib
import sys
import tempfile

import pytest

from foodsale import pathfromglob

__author__ = "Taylor Monacelli"
__copyright__ = "Taylor Monacelli"
__license__ = "MPL-2.0"


if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)


"""
or this:
*/Program*/Windows Kits/*/bin/*/*/SignTool.exe
"""


def test_windows():
    base_dir = pathlib.Path(tempfile.gettempdir())
    y1 = base_dir / r"Program Files\WiX Toolset 3.11\bin\heat.exe"
    p1 = base_dir / r"Program*\WiX Toolset*\*\heat.exe"
    y1.parent.mkdir(parents=True, exist_ok=True)
    y1.touch()
    lst = pathfromglob.abspathglob(str(p1))
    assert len(lst) == 1
