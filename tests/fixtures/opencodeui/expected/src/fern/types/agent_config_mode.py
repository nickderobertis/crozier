

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentConfigMode(enum.StrEnum):
    SUBAGENT = "subagent"
    PRIMARY = "primary"
    ALL = "all"

    def visit(
        self,
        subagent: typing.Callable[[], T_Result],
        primary: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentConfigMode.SUBAGENT:
            return subagent()
        if self is AgentConfigMode.PRIMARY:
            return primary()
        if self is AgentConfigMode.ALL:
            return all_()
