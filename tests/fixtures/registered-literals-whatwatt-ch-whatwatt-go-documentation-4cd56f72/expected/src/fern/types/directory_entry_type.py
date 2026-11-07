

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DirectoryEntryType(enum.StrEnum):
    FILE = "file"
    DIR = "dir"

    def visit(self, file: typing.Callable[[], T_Result], dir: typing.Callable[[], T_Result]) -> T_Result:
        if self is DirectoryEntryType.FILE:
            return file()
        if self is DirectoryEntryType.DIR:
            return dir()
