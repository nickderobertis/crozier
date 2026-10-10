

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmbeddingObject(enum.StrEnum):
    EMBEDDING = "embedding"

    def visit(self, embedding: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmbeddingObject.EMBEDDING:
            return embedding()
