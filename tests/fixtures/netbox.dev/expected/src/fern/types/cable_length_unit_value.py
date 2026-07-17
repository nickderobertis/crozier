

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CableLengthUnitValue(enum.StrEnum):
    KM = "km"
    M = "m"
    CM = "cm"
    MI = "mi"
    FT = "ft"
    IN = "in"

    def visit(
        self,
        km: typing.Callable[[], T_Result],
        m: typing.Callable[[], T_Result],
        cm: typing.Callable[[], T_Result],
        mi: typing.Callable[[], T_Result],
        ft: typing.Callable[[], T_Result],
        in_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CableLengthUnitValue.KM:
            return km()
        if self is CableLengthUnitValue.M:
            return m()
        if self is CableLengthUnitValue.CM:
            return cm()
        if self is CableLengthUnitValue.MI:
            return mi()
        if self is CableLengthUnitValue.FT:
            return ft()
        if self is CableLengthUnitValue.IN:
            return in_()
