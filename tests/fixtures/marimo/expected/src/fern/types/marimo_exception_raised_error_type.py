

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoExceptionRaisedErrorType(enum.StrEnum):
    EXCEPTION = "exception"

    def visit(self, exception: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoExceptionRaisedErrorType.EXCEPTION:
            return exception()
