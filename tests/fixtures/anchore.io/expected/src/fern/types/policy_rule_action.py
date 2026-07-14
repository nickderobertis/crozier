

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PolicyRuleAction(str, enum.Enum):
    GO = "GO"
    STOP = "STOP"
    WARN = "WARN"

    def visit(
        self,
        go: typing.Callable[[], T_Result],
        stop: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PolicyRuleAction.GO:
            return go()
        if self is PolicyRuleAction.STOP:
            return stop()
        if self is PolicyRuleAction.WARN:
            return warn()
