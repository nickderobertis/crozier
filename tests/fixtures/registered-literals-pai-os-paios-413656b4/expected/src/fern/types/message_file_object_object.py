

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageFileObjectObject(enum.StrEnum):
    """
    The object type, which is always `thread.message.file`.
    """

    THREAD_MESSAGE_FILE = "thread.message.file"

    def visit(self, thread_message_file: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageFileObjectObject.THREAD_MESSAGE_FILE:
            return thread_message_file()
