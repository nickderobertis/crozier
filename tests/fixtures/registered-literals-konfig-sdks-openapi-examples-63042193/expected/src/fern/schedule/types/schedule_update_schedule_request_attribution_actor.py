

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleUpdateScheduleRequestAttributionActor(enum.StrEnum):
    """
    The attribution-actor of the scheduled pipeline.
    """

    CURRENT = "current"
    SYSTEM = "system"

    def visit(self, current: typing.Callable[[], T_Result], system: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScheduleUpdateScheduleRequestAttributionActor.CURRENT:
            return current()
        if self is ScheduleUpdateScheduleRequestAttributionActor.SYSTEM:
            return system()
