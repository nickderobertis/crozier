

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HttpLlmResponseProvider(enum.StrEnum):
    ANTHROPIC = "ANTHROPIC"
    OPENAI = "OPENAI"
    OPENAI_RESPONSES = "OPENAI_RESPONSES"
    GEMINI = "GEMINI"
    BEDROCK = "BEDROCK"
    AZURE_OPENAI = "AZURE_OPENAI"
    OLLAMA = "OLLAMA"
    COHERE = "COHERE"
    VOYAGE = "VOYAGE"
    MISTRAL = "MISTRAL"
    XAI = "XAI"
    DEEPSEEK = "DEEPSEEK"
    GROQ = "GROQ"
    OPENROUTER = "OPENROUTER"
    ORCAROUTER = "ORCAROUTER"

    def visit(
        self,
        anthropic: typing.Callable[[], T_Result],
        openai: typing.Callable[[], T_Result],
        openai_responses: typing.Callable[[], T_Result],
        gemini: typing.Callable[[], T_Result],
        bedrock: typing.Callable[[], T_Result],
        azure_openai: typing.Callable[[], T_Result],
        ollama: typing.Callable[[], T_Result],
        cohere: typing.Callable[[], T_Result],
        voyage: typing.Callable[[], T_Result],
        mistral: typing.Callable[[], T_Result],
        xai: typing.Callable[[], T_Result],
        deepseek: typing.Callable[[], T_Result],
        groq: typing.Callable[[], T_Result],
        openrouter: typing.Callable[[], T_Result],
        orcarouter: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HttpLlmResponseProvider.ANTHROPIC:
            return anthropic()
        if self is HttpLlmResponseProvider.OPENAI:
            return openai()
        if self is HttpLlmResponseProvider.OPENAI_RESPONSES:
            return openai_responses()
        if self is HttpLlmResponseProvider.GEMINI:
            return gemini()
        if self is HttpLlmResponseProvider.BEDROCK:
            return bedrock()
        if self is HttpLlmResponseProvider.AZURE_OPENAI:
            return azure_openai()
        if self is HttpLlmResponseProvider.OLLAMA:
            return ollama()
        if self is HttpLlmResponseProvider.COHERE:
            return cohere()
        if self is HttpLlmResponseProvider.VOYAGE:
            return voyage()
        if self is HttpLlmResponseProvider.MISTRAL:
            return mistral()
        if self is HttpLlmResponseProvider.XAI:
            return xai()
        if self is HttpLlmResponseProvider.DEEPSEEK:
            return deepseek()
        if self is HttpLlmResponseProvider.GROQ:
            return groq()
        if self is HttpLlmResponseProvider.OPENROUTER:
            return openrouter()
        if self is HttpLlmResponseProvider.ORCAROUTER:
            return orcarouter()
