

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VisualizeSessionIdGetError503ErrorCode(enum.StrEnum):
    AI_NOT_CONFIGURED = "AI_NOT_CONFIGURED"

    def visit(self, ai_not_configured: typing.Callable[[], T_Result]) -> T_Result:
        if self is VisualizeSessionIdGetError503ErrorCode.AI_NOT_CONFIGURED:
            return ai_not_configured()
