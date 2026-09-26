

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTablesRequestSortBy(enum.StrEnum):
    """
    Field used to sort the result. Sorting by `name` is case-sensitive and follows the storage collation, so do not rely on a case-insensitive order.
    """

    NAME = "name"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"

    def visit(
        self,
        name: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListTablesRequestSortBy.NAME:
            return name()
        if self is ListTablesRequestSortBy.CREATED_AT:
            return created_at()
        if self is ListTablesRequestSortBy.UPDATED_AT:
            return updated_at()
