

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotCountComponentStatus(enum.StrEnum):
    MISSING = "missing"
    READY = "ready"

    def visit(self, missing: typing.Callable[[], T_Result], ready: typing.Callable[[], T_Result]) -> T_Result:
        if self is PilotCountComponentStatus.MISSING:
            return missing()
        if self is PilotCountComponentStatus.READY:
            return ready()
