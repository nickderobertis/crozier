

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LocationType(enum.StrEnum):
    """
    Type of the shop
    """

    CHEMIST = "chemist"
    BEVERAGES = "beverages"
    KIOSK = "kiosk"
    NEWSAGENT = "newsagent"
    CONVENIENCE = "convenience"

    def visit(
        self,
        chemist: typing.Callable[[], T_Result],
        beverages: typing.Callable[[], T_Result],
        kiosk: typing.Callable[[], T_Result],
        newsagent: typing.Callable[[], T_Result],
        convenience: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LocationType.CHEMIST:
            return chemist()
        if self is LocationType.BEVERAGES:
            return beverages()
        if self is LocationType.KIOSK:
            return kiosk()
        if self is LocationType.NEWSAGENT:
            return newsagent()
        if self is LocationType.CONVENIENCE:
            return convenience()
