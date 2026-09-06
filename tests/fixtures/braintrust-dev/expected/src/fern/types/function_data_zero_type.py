

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataZeroType(enum.StrEnum):
    PROMPT = "prompt"

    def visit(self, prompt: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataZeroType.PROMPT:
            return prompt()
