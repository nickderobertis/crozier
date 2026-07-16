

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OtoroshiHealthDatastore(str, enum.Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    UNREACHABLE = "unreachable"

    def visit(
        self,
        healthy: typing.Callable[[], T_Result],
        unhealthy: typing.Callable[[], T_Result],
        unreachable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OtoroshiHealthDatastore.HEALTHY:
            return healthy()
        if self is OtoroshiHealthDatastore.UNHEALTHY:
            return unhealthy()
        if self is OtoroshiHealthDatastore.UNREACHABLE:
            return unreachable()
