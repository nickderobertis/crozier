

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AiConfigMode(enum.StrEnum):
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
        if self is AiConfigMode.AGENT:
            return agent()
        if self is AiConfigMode.ASK:
            return ask()
        if self is AiConfigMode.CODE_MODE:
            return code_mode()
        if self is AiConfigMode.MANUAL:
            return manual()
