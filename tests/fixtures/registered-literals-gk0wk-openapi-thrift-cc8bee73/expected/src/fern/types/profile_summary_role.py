

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProfileSummaryRole(enum.StrEnum):
    USER = "user"
    ADMIN = "admin"
    REVIEWER = "reviewer"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        reviewer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProfileSummaryRole.USER:
            return user()
        if self is ProfileSummaryRole.ADMIN:
            return admin()
        if self is ProfileSummaryRole.REVIEWER:
            return reviewer()
