

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageObjectRole(enum.StrEnum):
    """
    The entity that produced the message. One of `user` or `assistant`.
    """

    USER = "user"
    ASSISTANT = "assistant"

    def visit(self, user: typing.Callable[[], T_Result], assistant: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageObjectRole.USER:
            return user()
        if self is MessageObjectRole.ASSISTANT:
            return assistant()
