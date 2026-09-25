

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreconditioningBaseAirConditioningStartingCause(enum.StrEnum):
    """
    starting cause
    """

    IMMEDIATE = "Immediate"
    SCHEDULED = "Scheduled"

    def visit(self, immediate: typing.Callable[[], T_Result], scheduled: typing.Callable[[], T_Result]) -> T_Result:
        if self is PreconditioningBaseAirConditioningStartingCause.IMMEDIATE:
            return immediate()
        if self is PreconditioningBaseAirConditioningStartingCause.SCHEDULED:
            return scheduled()
