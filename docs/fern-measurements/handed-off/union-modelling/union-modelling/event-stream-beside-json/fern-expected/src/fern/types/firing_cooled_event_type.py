

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FiringCooledEventType(enum.StrEnum):
    """
    Always `firing.cooled`.
    """

    FIRING_COOLED = "firing.cooled"

    def visit(self, firing_cooled: typing.Callable[[], T_Result]) -> T_Result:
        if self is FiringCooledEventType.FIRING_COOLED:
            return firing_cooled()
