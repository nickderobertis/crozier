

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentSayResponseNextActionsItem(enum.StrEnum):
    SAY = "say"
    CHECK = "check"
    FINISH = "finish"
    FINAL = "final"
    COLLECT = "collect"
    CLOSE = "close"

    def visit(
        self,
        say: typing.Callable[[], T_Result],
        check: typing.Callable[[], T_Result],
        finish: typing.Callable[[], T_Result],
        final: typing.Callable[[], T_Result],
        collect: typing.Callable[[], T_Result],
        close: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentSayResponseNextActionsItem.SAY:
            return say()
        if self is AgentSayResponseNextActionsItem.CHECK:
            return check()
        if self is AgentSayResponseNextActionsItem.FINISH:
            return finish()
        if self is AgentSayResponseNextActionsItem.FINAL:
            return final()
        if self is AgentSayResponseNextActionsItem.COLLECT:
            return collect()
        if self is AgentSayResponseNextActionsItem.CLOSE:
            return close()
