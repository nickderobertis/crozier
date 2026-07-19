

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageCreateRole(enum.StrEnum):
    """
    The role of the participant.
    """

    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageCreateRole.USER:
            return user()
        if self is MessageCreateRole.SYSTEM:
            return system()
        if self is MessageCreateRole.ASSISTANT:
            return assistant()
