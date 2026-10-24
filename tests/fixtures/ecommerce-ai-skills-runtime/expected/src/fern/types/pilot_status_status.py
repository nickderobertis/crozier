

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotStatusStatus(enum.StrEnum):
    READY = "ready"
    ATTENTION = "attention"
    BLOCKED = "blocked"

    def visit(
        self,
        ready: typing.Callable[[], T_Result],
        attention: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PilotStatusStatus.READY:
            return ready()
        if self is PilotStatusStatus.ATTENTION:
            return attention()
        if self is PilotStatusStatus.BLOCKED:
            return blocked()
