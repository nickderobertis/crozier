

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppCatalogPageItemsItemStatus(enum.StrEnum):
    TRADABLE = "tradable"
    DISPLAY_ONLY = "display_only"
    NOT_IN_APP = "not_in_app"
    UNAVAILABLE = "unavailable"

    def visit(
        self,
        tradable: typing.Callable[[], T_Result],
        display_only: typing.Callable[[], T_Result],
        not_in_app: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppCatalogPageItemsItemStatus.TRADABLE:
            return tradable()
        if self is AppCatalogPageItemsItemStatus.DISPLAY_ONLY:
            return display_only()
        if self is AppCatalogPageItemsItemStatus.NOT_IN_APP:
            return not_in_app()
        if self is AppCatalogPageItemsItemStatus.UNAVAILABLE:
            return unavailable()
