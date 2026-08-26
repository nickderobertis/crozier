

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoStrictExecutionErrorType(enum.StrEnum):
    STRICT_EXCEPTION = "strict-exception"

    def visit(self, strict_exception: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoStrictExecutionErrorType.STRICT_EXCEPTION:
            return strict_exception()
