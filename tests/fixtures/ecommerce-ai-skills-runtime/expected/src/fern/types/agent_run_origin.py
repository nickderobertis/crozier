

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentRunOrigin(enum.StrEnum):
    MANUAL = "manual"
    DAILY_OPS = "daily_ops"

    def visit(self, manual: typing.Callable[[], T_Result], daily_ops: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentRunOrigin.MANUAL:
            return manual()
        if self is AgentRunOrigin.DAILY_OPS:
            return daily_ops()
