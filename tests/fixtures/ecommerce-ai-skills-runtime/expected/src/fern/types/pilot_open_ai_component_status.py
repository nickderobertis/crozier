

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotOpenAiComponentStatus(enum.StrEnum):
    MISSING = "missing"
    READY = "ready"

    def visit(self, missing: typing.Callable[[], T_Result], ready: typing.Callable[[], T_Result]) -> T_Result:
        if self is PilotOpenAiComponentStatus.MISSING:
            return missing()
        if self is PilotOpenAiComponentStatus.READY:
            return ready()
