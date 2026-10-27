

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateChatMemberRequestRolesItem(enum.StrEnum):
    OWNER = "owner"
    MEMBER = "member"

    def visit(self, owner: typing.Callable[[], T_Result], member: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateChatMemberRequestRolesItem.OWNER:
            return owner()
        if self is UpdateChatMemberRequestRolesItem.MEMBER:
            return member()
