

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogWellKnownModelProviderType(enum.StrEnum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE_GEMINI = "google-gemini"
    FIREWORKS = "fireworks"
    ZAI = "zai"
    MOONSHOT = "moonshot"
    ALIBABA = "alibaba"
    TOGETHER = "together"

    def visit(
        self,
        openai: typing.Callable[[], T_Result],
        anthropic: typing.Callable[[], T_Result],
        google_gemini: typing.Callable[[], T_Result],
        fireworks: typing.Callable[[], T_Result],
        zai: typing.Callable[[], T_Result],
        moonshot: typing.Callable[[], T_Result],
        alibaba: typing.Callable[[], T_Result],
        together: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogWellKnownModelProviderType.OPENAI:
            return openai()
        if self is CatalogWellKnownModelProviderType.ANTHROPIC:
            return anthropic()
        if self is CatalogWellKnownModelProviderType.GOOGLE_GEMINI:
            return google_gemini()
        if self is CatalogWellKnownModelProviderType.FIREWORKS:
            return fireworks()
        if self is CatalogWellKnownModelProviderType.ZAI:
            return zai()
        if self is CatalogWellKnownModelProviderType.MOONSHOT:
            return moonshot()
        if self is CatalogWellKnownModelProviderType.ALIBABA:
            return alibaba()
        if self is CatalogWellKnownModelProviderType.TOGETHER:
            return together()
