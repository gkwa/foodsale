import logging
import pathlib
import sys
import tempfile

import pytest

from foodsale import pathfromglob
from foodsale.skeleton import fib, main

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
    y1.parent.mkdir(parents=True, exist_ok=True)
    y1.touch()
    glob = pathfromglob.abspathglob(str(y1))
    result = list(glob)
    assert len(result) == 1
