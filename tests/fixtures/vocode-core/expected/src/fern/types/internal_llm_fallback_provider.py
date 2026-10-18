

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InternalLlmFallbackProvider(enum.StrEnum):
    OPENAI = "openai"
    AZURE = "azure"

    def visit(self, openai: typing.Callable[[], T_Result], azure: typing.Callable[[], T_Result]) -> T_Result:
        if self is InternalLlmFallbackProvider.OPENAI:
            return openai()
        if self is InternalLlmFallbackProvider.AZURE:
            return azure()
