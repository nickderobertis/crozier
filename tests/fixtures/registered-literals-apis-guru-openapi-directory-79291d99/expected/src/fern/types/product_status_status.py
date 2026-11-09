

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductStatusStatus(enum.StrEnum):
    """
    This field is deprecated in favor of the `breakdown` object, which provides more granular institution health data.

    `HEALTHY`: the majority of requests are successful
    `DEGRADED`: only some requests are successful
    `DOWN`: all requests are failing
    """

    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    DOWN = "DOWN"

    def visit(
        self,
        healthy: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        down: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProductStatusStatus.HEALTHY:
            return healthy()
        if self is ProductStatusStatus.DEGRADED:
            return degraded()
        if self is ProductStatusStatus.DOWN:
            return down()
