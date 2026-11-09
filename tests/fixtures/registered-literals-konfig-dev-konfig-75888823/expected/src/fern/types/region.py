

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Region(enum.StrEnum):
    SEATTLE = "Seattle"
    LOS_ANGELES = "Los_Angeles"
    WASHINGTON_DC = "Washington_DC"
    CHICAGO = "Chicago"
    LONDON = "London"
    FRANKFURT = "Frankfurt"
    MUMBAI = "Mumbai"
    SINGAPORE = "Singapore"
    TOKYO = "Tokyo"
    SYDNEY = "Sydney"
    SAO_PAULO = "Sao_Paulo"

    def visit(
        self,
        seattle: typing.Callable[[], T_Result],
        los_angeles: typing.Callable[[], T_Result],
        washington_dc: typing.Callable[[], T_Result],
        chicago: typing.Callable[[], T_Result],
        london: typing.Callable[[], T_Result],
        frankfurt: typing.Callable[[], T_Result],
        mumbai: typing.Callable[[], T_Result],
        singapore: typing.Callable[[], T_Result],
        tokyo: typing.Callable[[], T_Result],
        sydney: typing.Callable[[], T_Result],
        sao_paulo: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Region.SEATTLE:
            return seattle()
        if self is Region.LOS_ANGELES:
            return los_angeles()
        if self is Region.WASHINGTON_DC:
            return washington_dc()
        if self is Region.CHICAGO:
            return chicago()
        if self is Region.LONDON:
            return london()
        if self is Region.FRANKFURT:
            return frankfurt()
        if self is Region.MUMBAI:
            return mumbai()
        if self is Region.SINGAPORE:
            return singapore()
        if self is Region.TOKYO:
            return tokyo()
        if self is Region.SYDNEY:
            return sydney()
        if self is Region.SAO_PAULO:
            return sao_paulo()
