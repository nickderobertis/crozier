

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionCallResultNotificationOp(enum.StrEnum):
    FUNCTION_CALL_RESULT = "function-call-result"

    def visit(self, function_call_result: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionCallResultNotificationOp.FUNCTION_CALL_RESULT:
            return function_call_result()
