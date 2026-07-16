

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CalendarType(str, enum.Enum):
    WEEKLY = "WEEKLY"
    FORTNIGHTLY = "FORTNIGHTLY"
    FOURWEEKLY = "FOURWEEKLY"
    MONTHLY = "MONTHLY"
    TWICEMONTHLY = "TWICEMONTHLY"
    QUARTERLY = "QUARTERLY"

    def visit(
        self,
        weekly: typing.Callable[[], T_Result],
        fortnightly: typing.Callable[[], T_Result],
        fourweekly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        twicemonthly: typing.Callable[[], T_Result],
        quarterly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CalendarType.WEEKLY:
            return weekly()
        if self is CalendarType.FORTNIGHTLY:
            return fortnightly()
        if self is CalendarType.FOURWEEKLY:
            return fourweekly()
        if self is CalendarType.MONTHLY:
            return monthly()
        if self is CalendarType.TWICEMONTHLY:
            return twicemonthly()
        if self is CalendarType.QUARTERLY:
            return quarterly()
