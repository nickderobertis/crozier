

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotTenantReadinessStatus(enum.StrEnum):
    READY = "ready"
    BLOCKED = "blocked"

    def visit(self, ready: typing.Callable[[], T_Result], blocked: typing.Callable[[], T_Result]) -> T_Result:
        if self is PilotTenantReadinessStatus.READY:
            return ready()
        if self is PilotTenantReadinessStatus.BLOCKED:
            return blocked()
