

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IntegrationHealthStatus(enum.StrEnum):
    ACTIVE = "active"
    DEGRADED = "degraded"
    BROKEN = "broken"
    UNKNOWN = "unknown"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        broken: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IntegrationHealthStatus.ACTIVE:
            return active()
        if self is IntegrationHealthStatus.DEGRADED:
            return degraded()
        if self is IntegrationHealthStatus.BROKEN:
            return broken()
        if self is IntegrationHealthStatus.UNKNOWN:
            return unknown()
