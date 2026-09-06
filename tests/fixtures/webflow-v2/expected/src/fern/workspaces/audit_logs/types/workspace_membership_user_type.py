

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class WorkspaceMembershipUserType(enum.StrEnum):
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
        if self is WorkspaceMembershipUserType.MEMBER:
            return member()
        if self is WorkspaceMembershipUserType.GUEST:
            return guest()
        if self is WorkspaceMembershipUserType.REVIEWER:
            return reviewer()
        if self is WorkspaceMembershipUserType.CLIENT:
            return client()
