

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTablesFoldersRequestSortBy(enum.StrEnum):
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
        if self is ListTablesFoldersRequestSortBy.NAME:
            return name()
        if self is ListTablesFoldersRequestSortBy.CREATED_AT:
            return created_at()
        if self is ListTablesFoldersRequestSortBy.UPDATED_AT:
            return updated_at()
