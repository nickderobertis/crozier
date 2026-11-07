

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserRole(enum.StrEnum):
    ADMIN = "admin"
    DEVELOPER = "developer"
    USER = "user"

    def visit(
        self,
        admin: typing.Callable[[], T_Result],
        developer: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserRole.ADMIN:
            return admin()
        if self is UserRole.DEVELOPER:
            return developer()
        if self is UserRole.USER:
            return user()
