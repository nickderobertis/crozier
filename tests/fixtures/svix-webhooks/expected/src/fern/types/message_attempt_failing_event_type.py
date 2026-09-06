

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageAttemptFailingEventType(enum.StrEnum):
    MESSAGE_ATTEMPT_FAILING = "message.attempt.failing"

    def visit(self, message_attempt_failing: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageAttemptFailingEventType.MESSAGE_ATTEMPT_FAILING:
            return message_attempt_failing()
