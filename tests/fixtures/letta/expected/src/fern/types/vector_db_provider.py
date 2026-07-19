

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VectorDbProvider(enum.StrEnum):
    """
    Supported vector database providers for archival memory
    """

    NATIVE = "native"
    TPUF = "tpuf"
    PINECONE = "pinecone"

    def visit(
        self,
        native: typing.Callable[[], T_Result],
        tpuf: typing.Callable[[], T_Result],
        pinecone: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VectorDbProvider.NATIVE:
            return native()
        if self is VectorDbProvider.TPUF:
            return tpuf()
        if self is VectorDbProvider.PINECONE:
            return pinecone()
