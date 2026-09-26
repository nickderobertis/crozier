

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentMode(enum.StrEnum):
    SUBAGENT = "subagent"
    PRIMARY = "primary"
    ALL = "all"

    def visit(
        self,
        subagent: typing.Callable[[], T_Result],
        primary: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentMode.SUBAGENT:
            return subagent()
        if self is AgentMode.PRIMARY:
            return primary()
        if self is AgentMode.ALL:
            return all_()
