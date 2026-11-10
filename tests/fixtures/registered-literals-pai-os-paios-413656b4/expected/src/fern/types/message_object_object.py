

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageObjectObject(enum.StrEnum):
    """
    The object type, which is always `thread.message`.
    """

    THREAD_MESSAGE = "thread.message"

    def visit(self, thread_message: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageObjectObject.THREAD_MESSAGE:
            return thread_message()
