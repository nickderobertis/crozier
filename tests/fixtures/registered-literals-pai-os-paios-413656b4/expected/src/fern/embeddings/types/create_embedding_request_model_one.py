

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateEmbeddingRequestModelOne(enum.StrEnum):
    TEXT_EMBEDDING_ADA002 = "text-embedding-ada-002"
    TEXT_EMBEDDING3SMALL = "text-embedding-3-small"
    TEXT_EMBEDDING3LARGE = "text-embedding-3-large"

    def visit(
        self,
        text_embedding_ada002: typing.Callable[[], T_Result],
        text_embedding3small: typing.Callable[[], T_Result],
        text_embedding3large: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateEmbeddingRequestModelOne.TEXT_EMBEDDING_ADA002:
            return text_embedding_ada002()
        if self is CreateEmbeddingRequestModelOne.TEXT_EMBEDDING3SMALL:
            return text_embedding3small()
        if self is CreateEmbeddingRequestModelOne.TEXT_EMBEDDING3LARGE:
            return text_embedding3large()
