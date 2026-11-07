

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListSdRootResponseFilesItemType(enum.StrEnum):
    FILE = "file"
    DIR = "dir"

    def visit(self, file: typing.Callable[[], T_Result], dir: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListSdRootResponseFilesItemType.FILE:
            return file()
        if self is ListSdRootResponseFilesItemType.DIR:
            return dir()
