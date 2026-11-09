

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateCompletionRequestModelOne(enum.StrEnum):
    GPT35TURBO_INSTRUCT = "gpt-3.5-turbo-instruct"
    DAVINCI002 = "davinci-002"
    BABBAGE002 = "babbage-002"

    def visit(
        self,
        gpt35turbo_instruct: typing.Callable[[], T_Result],
        davinci002: typing.Callable[[], T_Result],
        babbage002: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateCompletionRequestModelOne.GPT35TURBO_INSTRUCT:
            return gpt35turbo_instruct()
        if self is CreateCompletionRequestModelOne.DAVINCI002:
            return davinci002()
        if self is CreateCompletionRequestModelOne.BABBAGE002:
            return babbage002()
