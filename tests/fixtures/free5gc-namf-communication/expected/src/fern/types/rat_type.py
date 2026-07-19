

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RatType(enum.StrEnum):
    NR = "NR"
    EUTRA = "EUTRA"
    WLAN = "WLAN"
    VIRTUAL = "VIRTUAL"

    def visit(
        self,
        nr: typing.Callable[[], T_Result],
        eutra: typing.Callable[[], T_Result],
        wlan: typing.Callable[[], T_Result],
        virtual: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RatType.NR:
            return nr()
        if self is RatType.EUTRA:
            return eutra()
        if self is RatType.WLAN:
            return wlan()
        if self is RatType.VIRTUAL:
            return virtual()
