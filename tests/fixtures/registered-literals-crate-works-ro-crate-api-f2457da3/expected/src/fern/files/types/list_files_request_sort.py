

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListFilesRequestSort(enum.StrEnum):
    ID = "id"
    FILENAME = "filename"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"

    def visit(
        self,
        id: typing.Callable[[], T_Result],
        filename: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListFilesRequestSort.ID:
            return id()
        if self is ListFilesRequestSort.FILENAME:
            return filename()
        if self is ListFilesRequestSort.CREATED_AT:
            return created_at()
        if self is ListFilesRequestSort.UPDATED_AT:
            return updated_at()
