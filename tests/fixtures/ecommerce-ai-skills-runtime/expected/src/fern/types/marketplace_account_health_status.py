

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarketplaceAccountHealthStatus(enum.StrEnum):
    UNCHECKED = "unchecked"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    MISCONFIGURED = "misconfigured"

    def visit(
        self,
        unchecked: typing.Callable[[], T_Result],
        healthy: typing.Callable[[], T_Result],
        unhealthy: typing.Callable[[], T_Result],
        misconfigured: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarketplaceAccountHealthStatus.UNCHECKED:
            return unchecked()
        if self is MarketplaceAccountHealthStatus.HEALTHY:
            return healthy()
        if self is MarketplaceAccountHealthStatus.UNHEALTHY:
            return unhealthy()
        if self is MarketplaceAccountHealthStatus.MISCONFIGURED:
            return misconfigured()
