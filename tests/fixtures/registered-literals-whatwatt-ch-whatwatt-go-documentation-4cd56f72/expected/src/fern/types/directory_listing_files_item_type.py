

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DirectoryListingFilesItemType(enum.StrEnum):
    FILE = "file"
    DIR = "dir"

    def visit(self, file: typing.Callable[[], T_Result], dir: typing.Callable[[], T_Result]) -> T_Result:
        if self is DirectoryListingFilesItemType.FILE:
            return file()
        if self is DirectoryListingFilesItemType.DIR:
            return dir()
