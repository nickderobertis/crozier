

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OperationKind(enum.StrEnum):
    PROFILING = "profiling"
    TRACING = "tracing"

    def visit(self, profiling: typing.Callable[[], T_Result], tracing: typing.Callable[[], T_Result]) -> T_Result:
        if self is OperationKind.PROFILING:
            return profiling()
        if self is OperationKind.TRACING:
            return tracing()
