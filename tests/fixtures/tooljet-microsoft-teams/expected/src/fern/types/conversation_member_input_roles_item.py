

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConversationMemberInputRolesItem(enum.StrEnum):
    OWNER = "owner"
    MEMBER = "member"

    def visit(self, owner: typing.Callable[[], T_Result], member: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConversationMemberInputRolesItem.OWNER:
            return owner()
        if self is ConversationMemberInputRolesItem.MEMBER:
            return member()
