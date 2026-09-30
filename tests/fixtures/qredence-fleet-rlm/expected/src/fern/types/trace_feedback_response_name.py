

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TraceFeedbackResponseName(enum.StrEnum):
    USER_FEEDBACK = "user_feedback"

    def visit(self, user_feedback: typing.Callable[[], T_Result]) -> T_Result:
        if self is TraceFeedbackResponseName.USER_FEEDBACK:
            return user_feedback()
