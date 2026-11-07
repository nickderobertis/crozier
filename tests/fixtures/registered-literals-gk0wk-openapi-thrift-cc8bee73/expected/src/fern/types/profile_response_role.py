

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProfileResponseRole(enum.StrEnum):
    USER = "user"
    ADMIN = "admin"
    REVIEWER = "reviewer"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        reviewer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProfileResponseRole.USER:
            return user()
        if self is ProfileResponseRole.ADMIN:
            return admin()
        if self is ProfileResponseRole.REVIEWER:
            return reviewer()
