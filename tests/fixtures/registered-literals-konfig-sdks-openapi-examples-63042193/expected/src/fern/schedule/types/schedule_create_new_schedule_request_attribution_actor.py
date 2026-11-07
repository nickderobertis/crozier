

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleCreateNewScheduleRequestAttributionActor(enum.StrEnum):
    """
    The attribution-actor of the scheduled pipeline.
    """

    CURRENT = "current"
    SYSTEM = "system"

    def visit(self, current: typing.Callable[[], T_Result], system: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScheduleCreateNewScheduleRequestAttributionActor.CURRENT:
            return current()
        if self is ScheduleCreateNewScheduleRequestAttributionActor.SYSTEM:
            return system()
