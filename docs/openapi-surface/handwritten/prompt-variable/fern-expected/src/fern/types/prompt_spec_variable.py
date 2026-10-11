

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptSpecVariable(enum.StrEnum):
    PS1 = "$PS1"

    def visit(self, ps1: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptSpecVariable.PS1:
            return ps1()
