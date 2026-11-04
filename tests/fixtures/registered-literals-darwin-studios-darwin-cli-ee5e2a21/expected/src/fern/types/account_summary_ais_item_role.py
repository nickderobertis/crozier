

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountSummaryAisItemRole(enum.StrEnum):
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"

    def visit(
        self,
        owner: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        member: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountSummaryAisItemRole.OWNER:
            return owner()
        if self is AccountSummaryAisItemRole.ADMIN:
            return admin()
        if self is AccountSummaryAisItemRole.MEMBER:
            return member()
