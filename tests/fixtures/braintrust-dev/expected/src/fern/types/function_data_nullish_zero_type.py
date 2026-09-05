

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataNullishZeroType(enum.StrEnum):
    PROMPT = "prompt"

    def visit(self, prompt: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataNullishZeroType.PROMPT:
            return prompt()
