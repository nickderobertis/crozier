

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Weekday(str, enum.Enum):
    """
    The days of the week.
    """

    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"

    def visit(
        self,
        mon: typing.Callable[[], T_Result],
        tue: typing.Callable[[], T_Result],
        wed: typing.Callable[[], T_Result],
        thu: typing.Callable[[], T_Result],
        fri: typing.Callable[[], T_Result],
        sat: typing.Callable[[], T_Result],
        sun: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Weekday.MON:
            return mon()
        if self is Weekday.TUE:
            return tue()
        if self is Weekday.WED:
            return wed()
        if self is Weekday.THU:
            return thu()
        if self is Weekday.FRI:
            return fri()
        if self is Weekday.SAT:
            return sat()
        if self is Weekday.SUN:
            return sun()
