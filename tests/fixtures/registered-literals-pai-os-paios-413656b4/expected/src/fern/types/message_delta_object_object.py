

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageDeltaObjectObject(enum.StrEnum):
    """
    The object type, which is always `thread.message.delta`.
    """

    THREAD_MESSAGE_DELTA = "thread.message.delta"

    def visit(self, thread_message_delta: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageDeltaObjectObject.THREAD_MESSAGE_DELTA:
            return thread_message_delta()
