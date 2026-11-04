

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatGenerationRequestEngine(enum.StrEnum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    FEATHERLESS = "featherless"
    GEMINI = "gemini"
    LITELLM = "litellm"
    MOONSHOT = "moonshot"

    def visit(
        self,
        openai: typing.Callable[[], T_Result],
        anthropic: typing.Callable[[], T_Result],
        featherless: typing.Callable[[], T_Result],
        gemini: typing.Callable[[], T_Result],
        litellm: typing.Callable[[], T_Result],
        moonshot: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatGenerationRequestEngine.OPENAI:
            return openai()
        if self is ChatGenerationRequestEngine.ANTHROPIC:
            return anthropic()
        if self is ChatGenerationRequestEngine.FEATHERLESS:
            return featherless()
        if self is ChatGenerationRequestEngine.GEMINI:
            return gemini()
        if self is ChatGenerationRequestEngine.LITELLM:
            return litellm()
        if self is ChatGenerationRequestEngine.MOONSHOT:
            return moonshot()
