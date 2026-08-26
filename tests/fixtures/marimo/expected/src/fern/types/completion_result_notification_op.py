

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompletionResultNotificationOp(enum.StrEnum):
    COMPLETION_RESULT = "completion-result"

    def visit(self, completion_result: typing.Callable[[], T_Result]) -> T_Result:
        if self is CompletionResultNotificationOp.COMPLETION_RESULT:
            return completion_result()
