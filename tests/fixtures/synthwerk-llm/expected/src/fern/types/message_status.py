

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageStatus(enum.StrEnum):
    """
    - `streaming`: the answer is still being written.
    - `completed`: the answer is complete.
    - `failed`: the model call failed. `content` holds the partial answer.
    - `canceled`: the client closed the stream. `content` holds the partial answer.
    """

    STREAMING = "streaming"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"

    def visit(
        self,
        streaming: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageStatus.STREAMING:
            return streaming()
        if self is MessageStatus.COMPLETED:
            return completed()
        if self is MessageStatus.FAILED:
            return failed()
        if self is MessageStatus.CANCELED:
            return canceled()
