

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAppCatalogResponseItemsItemStatus(enum.StrEnum):
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
        if self is GetAppCatalogResponseItemsItemStatus.TRADABLE:
            return tradable()
        if self is GetAppCatalogResponseItemsItemStatus.DISPLAY_ONLY:
            return display_only()
        if self is GetAppCatalogResponseItemsItemStatus.NOT_IN_APP:
            return not_in_app()
        if self is GetAppCatalogResponseItemsItemStatus.UNAVAILABLE:
            return unavailable()
