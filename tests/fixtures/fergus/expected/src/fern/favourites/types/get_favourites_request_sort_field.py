

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFavouritesRequestSortField(enum.StrEnum):
    NAME = "name"
    CREATED_AT = "createdAt"
    SORT_ORDER = "sortOrder"

    def visit(
        self,
        name: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        sort_order: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetFavouritesRequestSortField.NAME:
            return name()
        if self is GetFavouritesRequestSortField.CREATED_AT:
            return created_at()
        if self is GetFavouritesRequestSortField.SORT_ORDER:
            return sort_order()
