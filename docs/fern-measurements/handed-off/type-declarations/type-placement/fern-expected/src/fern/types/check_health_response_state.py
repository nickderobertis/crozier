

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CheckHealthResponseState(enum.StrEnum):
    UP = "up"
    DEGRADED = "degraded"

    def visit(self, up: typing.Callable[[], T_Result], degraded: typing.Callable[[], T_Result]) -> T_Result:
        if self is CheckHealthResponseState.UP:
            return up()
        if self is CheckHealthResponseState.DEGRADED:
            return degraded()
