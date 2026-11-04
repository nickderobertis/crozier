

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileSort(enum.StrEnum):
    NAME = "name"
    UPDATED_AT = "updatedAt"
    SIZE = "size"
    ID = "id"

    def visit(
        self,
        name: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        size: typing.Callable[[], T_Result],
        id: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileSort.NAME:
            return name()
        if self is FileSort.UPDATED_AT:
            return updated_at()
        if self is FileSort.SIZE:
            return size()
        if self is FileSort.ID:
            return id()
