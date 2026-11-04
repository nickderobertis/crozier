

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionSourceScheduleType(enum.StrEnum):
    """
    Session was created by a schedule run.
    """

    SCHEDULE = "schedule"

    def visit(self, schedule: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionSourceScheduleType.SCHEDULE:
            return schedule()
