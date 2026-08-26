

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StorageEntryKind(enum.StrEnum):
    DIRECTORY = "directory"
    FILE = "file"
    OBJECT = "object"

    def visit(
        self,
        directory: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
        object: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StorageEntryKind.DIRECTORY:
            return directory()
        if self is StorageEntryKind.FILE:
            return file()
        if self is StorageEntryKind.OBJECT:
            return object()
