

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OtoroshiHealthOtoroshi(str, enum.Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DOWN = "down"

    def visit(
        self,
        healthy: typing.Callable[[], T_Result],
        unhealthy: typing.Callable[[], T_Result],
        down: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OtoroshiHealthOtoroshi.HEALTHY:
            return healthy()
        if self is OtoroshiHealthOtoroshi.UNHEALTHY:
            return unhealthy()
        if self is OtoroshiHealthOtoroshi.DOWN:
            return down()
