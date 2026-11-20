

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsCodeWeekDayType(enum.StrEnum):
    """
    Indicates a day of the week, represented as a string with a list of enumerated values.
    """

    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"
    ANY = "ANY"

    def visit(
        self,
        mon: typing.Callable[[], T_Result],
        tue: typing.Callable[[], T_Result],
        wed: typing.Callable[[], T_Result],
        thu: typing.Callable[[], T_Result],
        fri: typing.Callable[[], T_Result],
        sat: typing.Callable[[], T_Result],
        sun: typing.Callable[[], T_Result],
        any: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SimpleDataModelsCodeWeekDayType.MON:
            return mon()
        if self is SimpleDataModelsCodeWeekDayType.TUE:
            return tue()
        if self is SimpleDataModelsCodeWeekDayType.WED:
            return wed()
        if self is SimpleDataModelsCodeWeekDayType.THU:
            return thu()
        if self is SimpleDataModelsCodeWeekDayType.FRI:
            return fri()
        if self is SimpleDataModelsCodeWeekDayType.SAT:
            return sat()
        if self is SimpleDataModelsCodeWeekDayType.SUN:
            return sun()
        if self is SimpleDataModelsCodeWeekDayType.ANY:
            return any()
