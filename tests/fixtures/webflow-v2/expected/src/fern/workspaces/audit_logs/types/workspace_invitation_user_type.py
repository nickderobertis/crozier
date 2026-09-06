

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class WorkspaceInvitationUserType(enum.StrEnum):
    MEMBER = "member"
    GUEST = "guest"
    REVIEWER = "reviewer"
    CLIENT = "client"

    def visit(
        self,
        member: typing.Callable[[], T_Result],
        guest: typing.Callable[[], T_Result],
        reviewer: typing.Callable[[], T_Result],
        client: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkspaceInvitationUserType.MEMBER:
            return member()
        if self is WorkspaceInvitationUserType.GUEST:
            return guest()
        if self is WorkspaceInvitationUserType.REVIEWER:
            return reviewer()
        if self is WorkspaceInvitationUserType.CLIENT:
            return client()
