

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountSummaryActiveAiRole(enum.StrEnum):
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"

    def visit(
        self,
        owner: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        member: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountSummaryActiveAiRole.OWNER:
            return owner()
        if self is AccountSummaryActiveAiRole.ADMIN:
            return admin()
        if self is AccountSummaryActiveAiRole.MEMBER:
            return member()
