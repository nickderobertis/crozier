

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelCapability(enum.StrEnum):
    LLM = "llm"
    EMBEDDING = "embedding"

    def visit(self, llm: typing.Callable[[], T_Result], embedding: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelCapability.LLM:
            return llm()
        if self is ModelCapability.EMBEDDING:
            return embedding()
