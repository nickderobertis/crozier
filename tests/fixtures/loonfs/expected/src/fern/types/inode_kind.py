

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InodeKind(enum.StrEnum):
    """
    The kind of a filesystem item, which is a file or a directory.
    """

    FILE = "file"
    DIR = "dir"

    def visit(self, file: typing.Callable[[], T_Result], dir: typing.Callable[[], T_Result]) -> T_Result:
        if self is InodeKind.FILE:
            return file()
        if self is InodeKind.DIR:
            return dir()
