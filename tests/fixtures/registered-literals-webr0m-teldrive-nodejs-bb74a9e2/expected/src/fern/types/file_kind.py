

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileKind(enum.StrEnum):
    FILE = "file"
    FOLDER = "folder"

    def visit(self, file: typing.Callable[[], T_Result], folder: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileKind.FILE:
            return file()
        if self is FileKind.FOLDER:
            return folder()
