

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthCheckStatus(enum.StrEnum):
    UP = "UP"
    DOWN = "DOWN"

    def visit(self, up: typing.Callable[[], T_Result], down: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthCheckStatus.UP:
            return up()
        if self is HealthCheckStatus.DOWN:
            return down()
