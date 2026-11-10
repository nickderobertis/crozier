

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestionEventZeroType(enum.StrEnum):
    TRACE_CREATE = "trace-create"

    def visit(self, trace_create: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestionEventZeroType.TRACE_CREATE:
            return trace_create()
