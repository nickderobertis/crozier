

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageAttemptRecoveredEventType(enum.StrEnum):
    MESSAGE_ATTEMPT_RECOVERED = "message.attempt.recovered"

    def visit(self, message_attempt_recovered: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageAttemptRecoveredEventType.MESSAGE_ATTEMPT_RECOVERED:
            return message_attempt_recovered()
