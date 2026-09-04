

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthStatusServicesExternalApis(enum.StrEnum):
    UP = "up"
    DOWN = "down"

    def visit(self, up: typing.Callable[[], T_Result], down: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthStatusServicesExternalApis.UP:
            return up()
        if self is HealthStatusServicesExternalApis.DOWN:
            return down()
