

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TestApiApiV1TestapiPostRequestProvider(enum.StrEnum):
    """
    LLM Provider
    """

    GEMINI = "gemini"
    OPENAI = "openai"
    OLLAMA = "ollama"
    MISTRAL = "mistral"

    def visit(
        self,
        gemini: typing.Callable[[], T_Result],
        openai: typing.Callable[[], T_Result],
        ollama: typing.Callable[[], T_Result],
        mistral: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TestApiApiV1TestapiPostRequestProvider.GEMINI:
            return gemini()
        if self is TestApiApiV1TestapiPostRequestProvider.OPENAI:
            return openai()
        if self is TestApiApiV1TestapiPostRequestProvider.OLLAMA:
            return ollama()
        if self is TestApiApiV1TestapiPostRequestProvider.MISTRAL:
            return mistral()
