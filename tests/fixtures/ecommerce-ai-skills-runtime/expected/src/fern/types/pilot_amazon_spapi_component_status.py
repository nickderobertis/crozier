

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotAmazonSpapiComponentStatus(enum.StrEnum):
    MISSING = "missing"
    UNHEALTHY = "unhealthy"
    STALE = "stale"
    MISSING_CREDENTIALS = "missing_credentials"
    READY = "ready"

    def visit(
        self,
        missing: typing.Callable[[], T_Result],
        unhealthy: typing.Callable[[], T_Result],
        stale: typing.Callable[[], T_Result],
        missing_credentials: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PilotAmazonSpapiComponentStatus.MISSING:
            return missing()
        if self is PilotAmazonSpapiComponentStatus.UNHEALTHY:
            return unhealthy()
        if self is PilotAmazonSpapiComponentStatus.STALE:
            return stale()
        if self is PilotAmazonSpapiComponentStatus.MISSING_CREDENTIALS:
            return missing_credentials()
        if self is PilotAmazonSpapiComponentStatus.READY:
            return ready()
