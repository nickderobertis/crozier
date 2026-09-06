

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CommentCreatedPayloadPayloadType(enum.StrEnum):
    """
    The type of comment payload. `new_comment` indicates a new thread; `reply` indicates a reply to an existing thread.
    """

    NEW_COMMENT = "new_comment"
    REPLY = "reply"

    def visit(self, new_comment: typing.Callable[[], T_Result], reply: typing.Callable[[], T_Result]) -> T_Result:
        if self is CommentCreatedPayloadPayloadType.NEW_COMMENT:
            return new_comment()
        if self is CommentCreatedPayloadPayloadType.REPLY:
            return reply()
