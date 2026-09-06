

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class SiteMembershipUserType(enum.StrEnum):
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
        if self is SiteMembershipUserType.MEMBER:
            return member()
        if self is SiteMembershipUserType.GUEST:
            return guest()
        if self is SiteMembershipUserType.REVIEWER:
            return reviewer()
        if self is SiteMembershipUserType.CLIENT:
            return client()
