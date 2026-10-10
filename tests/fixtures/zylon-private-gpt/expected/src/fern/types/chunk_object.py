

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChunkObject(enum.StrEnum):
    CONTEXT_CHUNK = "context.chunk"

    def visit(self, context_chunk: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChunkObject.CONTEXT_CHUNK:
            return context_chunk()
