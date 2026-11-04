

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomLlmProvider(enum.StrEnum):
    OPENAI_COMPATIBLE = "openai_compatible"
    OLLAMA = "ollama"
    OPENROUTER = "openrouter"

    def visit(
        self,
        openai_compatible: typing.Callable[[], T_Result],
        ollama: typing.Callable[[], T_Result],
        openrouter: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomLlmProvider.OPENAI_COMPATIBLE:
            return openai_compatible()
        if self is CustomLlmProvider.OLLAMA:
            return ollama()
        if self is CustomLlmProvider.OPENROUTER:
            return openrouter()
