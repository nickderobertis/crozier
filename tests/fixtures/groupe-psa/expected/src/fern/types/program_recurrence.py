

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProgramRecurrence(enum.StrEnum):
    """
    Determines the recurrence of the program.
    * None: means no recurrence.
    * Daily: repeated over the week.
    """

    NONE = "None"
    DAILY = "Daily"

    def visit(self, none: typing.Callable[[], T_Result], daily: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProgramRecurrence.NONE:
            return none()
        if self is ProgramRecurrence.DAILY:
            return daily()
