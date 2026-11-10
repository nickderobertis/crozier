

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateFineTuningJobRequestModelOne(enum.StrEnum):
    BABBAGE002 = "babbage-002"
    DAVINCI002 = "davinci-002"
    GPT35TURBO = "gpt-3.5-turbo"

    def visit(
        self,
        babbage002: typing.Callable[[], T_Result],
        davinci002: typing.Callable[[], T_Result],
        gpt35turbo: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateFineTuningJobRequestModelOne.BABBAGE002:
            return babbage002()
        if self is CreateFineTuningJobRequestModelOne.DAVINCI002:
            return davinci002()
        if self is CreateFineTuningJobRequestModelOne.GPT35TURBO:
            return gpt35turbo()
