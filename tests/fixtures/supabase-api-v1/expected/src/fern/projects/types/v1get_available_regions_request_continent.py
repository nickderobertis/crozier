

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1GetAvailableRegionsRequestContinent(enum.StrEnum):
    NA = "NA"
    SA = "SA"
    EU = "EU"
    AF = "AF"
    AS = "AS"
    OC = "OC"
    AN = "AN"

    def visit(
        self,
        na: typing.Callable[[], T_Result],
        sa: typing.Callable[[], T_Result],
        eu: typing.Callable[[], T_Result],
        af: typing.Callable[[], T_Result],
        as_: typing.Callable[[], T_Result],
        oc: typing.Callable[[], T_Result],
        an: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1GetAvailableRegionsRequestContinent.NA:
            return na()
        if self is V1GetAvailableRegionsRequestContinent.SA:
            return sa()
        if self is V1GetAvailableRegionsRequestContinent.EU:
            return eu()
        if self is V1GetAvailableRegionsRequestContinent.AF:
            return af()
        if self is V1GetAvailableRegionsRequestContinent.AS:
            return as_()
        if self is V1GetAvailableRegionsRequestContinent.OC:
            return oc()
        if self is V1GetAvailableRegionsRequestContinent.AN:
            return an()
