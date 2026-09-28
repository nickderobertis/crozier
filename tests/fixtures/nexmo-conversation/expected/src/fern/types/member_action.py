

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MemberAction(enum.StrEnum):
    """
    Invite or join a member to a conversation
    """

    INVITE = "invite"
    JOIN = "join"

    def visit(self, invite: typing.Callable[[], T_Result], join: typing.Callable[[], T_Result]) -> T_Result:
        if self is MemberAction.INVITE:
            return invite()
        if self is MemberAction.JOIN:
            return join()
