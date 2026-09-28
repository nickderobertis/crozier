

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LegState(enum.StrEnum):
    """
    Leg Status
    """

    TERMINATED = "terminated"

    def visit(self, terminated: typing.Callable[[], T_Result]) -> T_Result:
        if self is LegState.TERMINATED:
            return terminated()
