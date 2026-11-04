

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CodeGenerationRequestEngine(enum.StrEnum):
    """
    LLM provider to use.
    """

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
        if self is CodeGenerationRequestEngine.OPENAI:
            return openai()
        if self is CodeGenerationRequestEngine.ANTHROPIC:
            return anthropic()
        if self is CodeGenerationRequestEngine.FEATHERLESS:
            return featherless()
        if self is CodeGenerationRequestEngine.GEMINI:
            return gemini()
        if self is CodeGenerationRequestEngine.LITELLM:
            return litellm()
        if self is CodeGenerationRequestEngine.MOONSHOT:
            return moonshot()
