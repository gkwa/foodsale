import pathlib

from signit import pathfromglob


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
