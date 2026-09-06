

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptParserNullishType(enum.StrEnum):
    LLM_CLASSIFIER = "llm_classifier"

    def visit(self, llm_classifier: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptParserNullishType.LLM_CLASSIFIER:
            return llm_classifier()
