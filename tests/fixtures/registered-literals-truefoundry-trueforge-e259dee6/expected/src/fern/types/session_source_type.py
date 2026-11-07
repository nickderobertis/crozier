

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionSourceType(enum.StrEnum):
    """
    When set, returns only sessions created by this source type.
    """

    SCHEDULE = "schedule"

    def visit(self, schedule: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionSourceType.SCHEDULE:
            return schedule()
