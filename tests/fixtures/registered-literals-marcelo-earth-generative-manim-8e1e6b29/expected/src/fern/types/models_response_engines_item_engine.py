

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelsResponseEnginesItemEngine(enum.StrEnum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"
    FEATHERLESS = "featherless"
    LITELLM = "litellm"
    MOONSHOT = "moonshot"

    def visit(
        self,
        openai: typing.Callable[[], T_Result],
        anthropic: typing.Callable[[], T_Result],
        gemini: typing.Callable[[], T_Result],
        featherless: typing.Callable[[], T_Result],
        litellm: typing.Callable[[], T_Result],
        moonshot: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ModelsResponseEnginesItemEngine.OPENAI:
            return openai()
        if self is ModelsResponseEnginesItemEngine.ANTHROPIC:
            return anthropic()
        if self is ModelsResponseEnginesItemEngine.GEMINI:
            return gemini()
        if self is ModelsResponseEnginesItemEngine.FEATHERLESS:
            return featherless()
        if self is ModelsResponseEnginesItemEngine.LITELLM:
            return litellm()
        if self is ModelsResponseEnginesItemEngine.MOONSHOT:
            return moonshot()
