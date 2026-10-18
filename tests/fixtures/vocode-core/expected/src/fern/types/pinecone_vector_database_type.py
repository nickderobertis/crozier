

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PineconeVectorDatabaseType(enum.StrEnum):
    VECTOR_DATABASE_PINECONE = "vector_database_pinecone"

    def visit(self, vector_database_pinecone: typing.Callable[[], T_Result]) -> T_Result:
        if self is PineconeVectorDatabaseType.VECTOR_DATABASE_PINECONE:
            return vector_database_pinecone()
