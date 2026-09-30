

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InferredFunctionResponseType(enum.StrEnum):
    INFERRED = "inferred"

    def visit(self, inferred: typing.Callable[[], T_Result]) -> T_Result:
        if self is InferredFunctionResponseType.INFERRED:
            return inferred()
