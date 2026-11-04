

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelProviderType(enum.StrEnum):
    ANTHROPIC = "anthropic"
    BEDROCK = "bedrock"
    CEREBRAS = "cerebras"
    CHUTES = "chutes"
    COHERE = "cohere"
    DEEPSEEK = "deepseek"
    GEMINI = "gemini"
    GITHUB = "github"
    GROQ = "groq"
    WATSONX = "watsonx"
    JAN = "jan"
    MISTRAL = "mistral"
    MOONSHOT = "moonshot"
    NVIDIA = "nvidia"
    OLLAMA = "ollama"
    OPENAI = "openai"
    OPENROUTER = "openrouter"
    PERPLEXITY = "perplexity"
    TOGETHER = "together"
    VOYAGE = "voyage"
    RITS = "rits"
    OTHER = "other"

    def visit(
        self,
        anthropic: typing.Callable[[], T_Result],
        bedrock: typing.Callable[[], T_Result],
        cerebras: typing.Callable[[], T_Result],
        chutes: typing.Callable[[], T_Result],
        cohere: typing.Callable[[], T_Result],
        deepseek: typing.Callable[[], T_Result],
        gemini: typing.Callable[[], T_Result],
        github: typing.Callable[[], T_Result],
        groq: typing.Callable[[], T_Result],
        watsonx: typing.Callable[[], T_Result],
        jan: typing.Callable[[], T_Result],
        mistral: typing.Callable[[], T_Result],
        moonshot: typing.Callable[[], T_Result],
        nvidia: typing.Callable[[], T_Result],
        ollama: typing.Callable[[], T_Result],
        openai: typing.Callable[[], T_Result],
        openrouter: typing.Callable[[], T_Result],
        perplexity: typing.Callable[[], T_Result],
        together: typing.Callable[[], T_Result],
        voyage: typing.Callable[[], T_Result],
        rits: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ModelProviderType.ANTHROPIC:
            return anthropic()
        if self is ModelProviderType.BEDROCK:
            return bedrock()
        if self is ModelProviderType.CEREBRAS:
            return cerebras()
        if self is ModelProviderType.CHUTES:
            return chutes()
        if self is ModelProviderType.COHERE:
            return cohere()
        if self is ModelProviderType.DEEPSEEK:
            return deepseek()
        if self is ModelProviderType.GEMINI:
            return gemini()
        if self is ModelProviderType.GITHUB:
            return github()
        if self is ModelProviderType.GROQ:
            return groq()
        if self is ModelProviderType.WATSONX:
            return watsonx()
        if self is ModelProviderType.JAN:
            return jan()
        if self is ModelProviderType.MISTRAL:
            return mistral()
        if self is ModelProviderType.MOONSHOT:
            return moonshot()
        if self is ModelProviderType.NVIDIA:
            return nvidia()
        if self is ModelProviderType.OLLAMA:
            return ollama()
        if self is ModelProviderType.OPENAI:
            return openai()
        if self is ModelProviderType.OPENROUTER:
            return openrouter()
        if self is ModelProviderType.PERPLEXITY:
            return perplexity()
        if self is ModelProviderType.TOGETHER:
            return together()
        if self is ModelProviderType.VOYAGE:
            return voyage()
        if self is ModelProviderType.RITS:
            return rits()
        if self is ModelProviderType.OTHER:
            return other()
