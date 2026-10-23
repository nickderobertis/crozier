

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAppCatalogRequestStatus(enum.StrEnum):
    TRADABLE = "tradable"
    DISPLAY_ONLY = "display_only"
    UNAVAILABLE = "unavailable"

    def visit(
        self,
        tradable: typing.Callable[[], T_Result],
        display_only: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAppCatalogRequestStatus.TRADABLE:
            return tradable()
        if self is GetAppCatalogRequestStatus.DISPLAY_ONLY:
            return display_only()
        if self is GetAppCatalogRequestStatus.UNAVAILABLE:
            return unavailable()
