

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListEntitiesRequestSort(enum.StrEnum):
    ID = "id"
    NAME = "name"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"

    def visit(
        self,
        id: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListEntitiesRequestSort.ID:
            return id()
        if self is ListEntitiesRequestSort.NAME:
            return name()
        if self is ListEntitiesRequestSort.CREATED_AT:
            return created_at()
        if self is ListEntitiesRequestSort.UPDATED_AT:
            return updated_at()
