

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenAiProviderSmokeRequestProvider(enum.StrEnum):
    OPENAI = "openai"

    def visit(self, openai: typing.Callable[[], T_Result]) -> T_Result:
        if self is OpenAiProviderSmokeRequestProvider.OPENAI:
            return openai()
