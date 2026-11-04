

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MembershipRole(enum.StrEnum):
    """
    The role of the member
    """

    OWNER = "owner"
    MEMBER = "member"

    def visit(self, owner: typing.Callable[[], T_Result], member: typing.Callable[[], T_Result]) -> T_Result:
        if self is MembershipRole.OWNER:
            return owner()
        if self is MembershipRole.MEMBER:
            return member()
