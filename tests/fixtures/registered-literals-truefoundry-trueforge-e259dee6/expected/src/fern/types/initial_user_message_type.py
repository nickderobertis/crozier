

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InitialUserMessageType(enum.StrEnum):
    """
    Initial message type.
    """

    USER_MESSAGE = "user.message"

    def visit(self, user_message: typing.Callable[[], T_Result]) -> T_Result:
        if self is InitialUserMessageType.USER_MESSAGE:
            return user_message()
