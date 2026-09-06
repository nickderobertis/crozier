

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageAttemptExhaustedEventType(enum.StrEnum):
    MESSAGE_ATTEMPT_EXHAUSTED = "message.attempt.exhausted"

    def visit(self, message_attempt_exhausted: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageAttemptExhaustedEventType.MESSAGE_ATTEMPT_EXHAUSTED:
            return message_attempt_exhausted()
