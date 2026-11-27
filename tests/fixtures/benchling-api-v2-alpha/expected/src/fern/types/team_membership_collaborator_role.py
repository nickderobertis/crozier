

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TeamMembershipCollaboratorRole(enum.StrEnum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"

    def visit(self, admin: typing.Callable[[], T_Result], member: typing.Callable[[], T_Result]) -> T_Result:
        if self is TeamMembershipCollaboratorRole.ADMIN:
            return admin()
        if self is TeamMembershipCollaboratorRole.MEMBER:
            return member()
