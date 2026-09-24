

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransmissionGearboxRatio(enum.StrEnum):
    """
    Current gear-box ratio.
    """

    RATIO1 = "Ratio1"
    RATIO2 = "Ratio2"
    RATIO3 = "Ratio3"
    RATIO4 = "Ratio4"
    RATIO5 = "Ratio5"
    RATIO6 = "Ratio6"
    RATIO7 = "Ratio7"
    RATIO8 = "Ratio8"
    NEUTRAL = "Neutral"
    REVERSE = "Reverse"

    def visit(
        self,
        ratio1: typing.Callable[[], T_Result],
        ratio2: typing.Callable[[], T_Result],
        ratio3: typing.Callable[[], T_Result],
        ratio4: typing.Callable[[], T_Result],
        ratio5: typing.Callable[[], T_Result],
        ratio6: typing.Callable[[], T_Result],
        ratio7: typing.Callable[[], T_Result],
        ratio8: typing.Callable[[], T_Result],
        neutral: typing.Callable[[], T_Result],
        reverse: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransmissionGearboxRatio.RATIO1:
            return ratio1()
        if self is TransmissionGearboxRatio.RATIO2:
            return ratio2()
        if self is TransmissionGearboxRatio.RATIO3:
            return ratio3()
        if self is TransmissionGearboxRatio.RATIO4:
            return ratio4()
        if self is TransmissionGearboxRatio.RATIO5:
            return ratio5()
        if self is TransmissionGearboxRatio.RATIO6:
            return ratio6()
        if self is TransmissionGearboxRatio.RATIO7:
            return ratio7()
        if self is TransmissionGearboxRatio.RATIO8:
            return ratio8()
        if self is TransmissionGearboxRatio.NEUTRAL:
            return neutral()
        if self is TransmissionGearboxRatio.REVERSE:
            return reverse()
