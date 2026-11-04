

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActUpdateRequestCompletionKind(enum.StrEnum):
    FEEDBACK = "feedback"

    def visit(self, feedback: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActUpdateRequestCompletionKind.FEEDBACK:
            return feedback()
