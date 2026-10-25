

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentFinalResponseNextActionsItem(enum.StrEnum):
    CHECK = "check"
    FINAL = "final"
    COLLECT = "collect"
    CLOSE = "close"

    def visit(
        self,
        check: typing.Callable[[], T_Result],
        final: typing.Callable[[], T_Result],
        collect: typing.Callable[[], T_Result],
        close: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentFinalResponseNextActionsItem.CHECK:
            return check()
        if self is AgentFinalResponseNextActionsItem.FINAL:
            return final()
        if self is AgentFinalResponseNextActionsItem.COLLECT:
            return collect()
        if self is AgentFinalResponseNextActionsItem.CLOSE:
            return close()
