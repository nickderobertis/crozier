

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmissionClass(enum.StrEnum):
    """
    Vehicle's Euro emissions standard
    """

    ZERO = "zero"
    EURO1 = "euro_1"
    EURO2 = "euro_2"
    EURO3 = "euro_3"
    EURO4 = "euro_4"
    EURO5 = "euro_5"
    EURO6 = "euro_6"

    def visit(
        self,
        zero: typing.Callable[[], T_Result],
        euro1: typing.Callable[[], T_Result],
        euro2: typing.Callable[[], T_Result],
        euro3: typing.Callable[[], T_Result],
        euro4: typing.Callable[[], T_Result],
        euro5: typing.Callable[[], T_Result],
        euro6: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmissionClass.ZERO:
            return zero()
        if self is EmissionClass.EURO1:
            return euro1()
        if self is EmissionClass.EURO2:
            return euro2()
        if self is EmissionClass.EURO3:
            return euro3()
        if self is EmissionClass.EURO4:
            return euro4()
        if self is EmissionClass.EURO5:
            return euro5()
        if self is EmissionClass.EURO6:
            return euro6()
