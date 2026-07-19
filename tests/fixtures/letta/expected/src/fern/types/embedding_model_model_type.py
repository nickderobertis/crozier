

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmbeddingModelModelType(enum.StrEnum):
    """
    Type of model (llm or embedding)
    """

    EMBEDDING = "embedding"

    def visit(self, embedding: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmbeddingModelModelType.EMBEDDING:
            return embedding()
