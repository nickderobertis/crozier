

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FiringStartedEventType(enum.StrEnum):
    """
    Always `firing.started`.
    """

    FIRING_STARTED = "firing.started"

    def visit(self, firing_started: typing.Callable[[], T_Result]) -> T_Result:
        if self is FiringStartedEventType.FIRING_STARTED:
            return firing_started()
