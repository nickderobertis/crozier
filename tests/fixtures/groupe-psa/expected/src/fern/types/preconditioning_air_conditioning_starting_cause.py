

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreconditioningAirConditioningStartingCause(enum.StrEnum):
    """
    starting cause
    """

    IMMEDIATE = "Immediate"
    SCHEDULED = "Scheduled"

    def visit(self, immediate: typing.Callable[[], T_Result], scheduled: typing.Callable[[], T_Result]) -> T_Result:
        if self is PreconditioningAirConditioningStartingCause.IMMEDIATE:
            return immediate()
        if self is PreconditioningAirConditioningStartingCause.SCHEDULED:
            return scheduled()
