

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableCableLengthUnit(enum.StrEnum):
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
        if self is WritableCableLengthUnit.KM:
            return km()
        if self is WritableCableLengthUnit.M:
            return m()
        if self is WritableCableLengthUnit.CM:
            return cm()
        if self is WritableCableLengthUnit.MI:
            return mi()
        if self is WritableCableLengthUnit.FT:
            return ft()
        if self is WritableCableLengthUnit.IN:
            return in_()
