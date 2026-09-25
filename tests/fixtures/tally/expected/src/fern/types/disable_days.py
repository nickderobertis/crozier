

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DisableDays(enum.StrEnum):
    """
    Days or date ranges to disable in the date picker.
    """

    IN_THE_PAST = "IN_THE_PAST"
    IN_THE_FUTURE = "IN_THE_FUTURE"
    MONDAYS = "MONDAYS"
    TUESDAYS = "TUESDAYS"
    WEDNESDAYS = "WEDNESDAYS"
    THURSDAYS = "THURSDAYS"
    FRIDAYS = "FRIDAYS"
    SATURDAYS = "SATURDAYS"
    SUNDAYS = "SUNDAYS"

    def visit(
        self,
        in_the_past: typing.Callable[[], T_Result],
        in_the_future: typing.Callable[[], T_Result],
        mondays: typing.Callable[[], T_Result],
        tuesdays: typing.Callable[[], T_Result],
        wednesdays: typing.Callable[[], T_Result],
        thursdays: typing.Callable[[], T_Result],
        fridays: typing.Callable[[], T_Result],
        saturdays: typing.Callable[[], T_Result],
        sundays: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DisableDays.IN_THE_PAST:
            return in_the_past()
        if self is DisableDays.IN_THE_FUTURE:
            return in_the_future()
        if self is DisableDays.MONDAYS:
            return mondays()
        if self is DisableDays.TUESDAYS:
            return tuesdays()
        if self is DisableDays.WEDNESDAYS:
            return wednesdays()
        if self is DisableDays.THURSDAYS:
            return thursdays()
        if self is DisableDays.FRIDAYS:
            return fridays()
        if self is DisableDays.SATURDAYS:
            return saturdays()
        if self is DisableDays.SUNDAYS:
            return sundays()
