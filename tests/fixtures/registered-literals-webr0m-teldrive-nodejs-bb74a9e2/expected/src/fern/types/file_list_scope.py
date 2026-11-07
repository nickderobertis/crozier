

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileListScope(enum.StrEnum):
    FOLDER = "folder"
    DRIVE = "drive"
    RECURSIVE = "recursive"

    def visit(
        self,
        folder: typing.Callable[[], T_Result],
        drive: typing.Callable[[], T_Result],
        recursive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileListScope.FOLDER:
            return folder()
        if self is FileListScope.DRIVE:
            return drive()
        if self is FileListScope.RECURSIVE:
            return recursive()
