

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolDefinitionModeItem(enum.StrEnum):
    AGENT = "agent"
    ASK = "ask"
    CODE_MODE = "code_mode"
    MANUAL = "manual"

    def visit(
        self,
        agent: typing.Callable[[], T_Result],
        ask: typing.Callable[[], T_Result],
        code_mode: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToolDefinitionModeItem.AGENT:
            return agent()
        if self is ToolDefinitionModeItem.ASK:
            return ask()
        if self is ToolDefinitionModeItem.CODE_MODE:
            return code_mode()
        if self is ToolDefinitionModeItem.MANUAL:
            return manual()
