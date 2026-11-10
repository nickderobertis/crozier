

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteMessageResponseObject(enum.StrEnum):
    THREAD_MESSAGE_DELETED = "thread.message.deleted"

    def visit(self, thread_message_deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteMessageResponseObject.THREAD_MESSAGE_DELETED:
            return thread_message_deleted()
