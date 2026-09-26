

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileNodeType(enum.StrEnum):
    FILE = "file"
    DIRECTORY = "directory"

    def visit(self, file: typing.Callable[[], T_Result], directory: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileNodeType.FILE:
            return file()
        if self is FileNodeType.DIRECTORY:
            return directory()
