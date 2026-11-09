

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchEntitiesRequestSort(enum.StrEnum):
    """
    The field on which to sort results. Defaults to `relevance`, which orders
    results by search score (highest first). When set to `relevance`, the
    `order` parameter is ignored. Use `id`, `name`, `createdAt`, or
    `updatedAt` to sort by a specific field.
    """

    ID = "id"
    NAME = "name"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"
    RELEVANCE = "relevance"

    def visit(
        self,
        id: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        relevance: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchEntitiesRequestSort.ID:
            return id()
        if self is SearchEntitiesRequestSort.NAME:
            return name()
        if self is SearchEntitiesRequestSort.CREATED_AT:
            return created_at()
        if self is SearchEntitiesRequestSort.UPDATED_AT:
            return updated_at()
        if self is SearchEntitiesRequestSort.RELEVANCE:
            return relevance()
