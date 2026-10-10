

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenAiCompletionModel(enum.StrEnum):
    PRIVATE_GPT = "private-gpt"

    def visit(self, private_gpt: typing.Callable[[], T_Result]) -> T_Result:
        if self is OpenAiCompletionModel.PRIVATE_GPT:
            return private_gpt()
