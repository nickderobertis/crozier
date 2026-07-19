

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelModelType(enum.StrEnum):
    """
    Type of model (llm or embedding)
    """

    LLM = "llm"

    def visit(self, llm: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelModelType.LLM:
            return llm()
