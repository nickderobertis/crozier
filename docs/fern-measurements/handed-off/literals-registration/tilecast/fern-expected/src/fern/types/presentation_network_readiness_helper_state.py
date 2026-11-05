

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PresentationNetworkReadinessHelperState(enum.StrEnum):
    OK = "ok"
    MISSING = "missing"
    UNHEALTHY = "unhealthy"
    UNSUPPORTED = "unsupported"

    def visit(
        self,
        ok: typing.Callable[[], T_Result],
        missing: typing.Callable[[], T_Result],
        unhealthy: typing.Callable[[], T_Result],
        unsupported: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PresentationNetworkReadinessHelperState.OK:
            return ok()
        if self is PresentationNetworkReadinessHelperState.MISSING:
            return missing()
        if self is PresentationNetworkReadinessHelperState.UNHEALTHY:
            return unhealthy()
        if self is PresentationNetworkReadinessHelperState.UNSUPPORTED:
            return unsupported()
