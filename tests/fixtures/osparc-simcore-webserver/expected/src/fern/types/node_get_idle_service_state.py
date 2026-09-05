

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeGetIdleServiceState(enum.StrEnum):
    IDLE = "idle"

    def visit(self, idle: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeGetIdleServiceState.IDLE:
            return idle()
