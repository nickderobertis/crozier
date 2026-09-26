# llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo crate with no Nx workspace; this test-only import shim sits in tests/ beside the golden-reach suite and is put on PYTHONPATH by `just test-fixtures-coverage`.
"""Make the POSIX-only standard-library modules unimportable, as they are on Windows.

Put this directory on `PYTHONPATH` and every Python started under it, children
included, fails `import fcntl` (and the rest) with `ImportError`. They are
built into CPython on POSIX, so a same-named file cannot shadow them; a `None`
in `sys.modules` is what the import system itself reads as "not available".
"""

import sys

ABSENT = ("fcntl", "grp", "pwd", "resource", "termios")

for name in ABSENT:
    sys.modules[name] = None  # type: ignore[assignment]
