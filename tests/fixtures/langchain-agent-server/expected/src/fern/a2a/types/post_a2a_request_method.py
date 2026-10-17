

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostA2ARequestMethod(enum.StrEnum):
    """
    The method to invoke
    """

    MESSAGE_SEND = "message/send"
    MESSAGE_STREAM = "message/stream"
    TASKS_GET = "tasks/get"
    TASKS_CANCEL = "tasks/cancel"

    def visit(
        self,
        message_send: typing.Callable[[], T_Result],
        message_stream: typing.Callable[[], T_Result],
        tasks_get: typing.Callable[[], T_Result],
        tasks_cancel: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostA2ARequestMethod.MESSAGE_SEND:
            return message_send()
        if self is PostA2ARequestMethod.MESSAGE_STREAM:
            return message_stream()
        if self is PostA2ARequestMethod.TASKS_GET:
            return tasks_get()
        if self is PostA2ARequestMethod.TASKS_CANCEL:
            return tasks_cancel()
