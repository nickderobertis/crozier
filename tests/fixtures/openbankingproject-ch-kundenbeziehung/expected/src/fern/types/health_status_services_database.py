

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthStatusServicesDatabase(enum.StrEnum):
    UP = "up"
    DOWN = "down"

    def visit(self, up: typing.Callable[[], T_Result], down: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthStatusServicesDatabase.UP:
            return up()
        if self is HealthStatusServicesDatabase.DOWN:
            return down()
