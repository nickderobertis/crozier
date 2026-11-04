

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserRole(enum.StrEnum):
    OWNER = "owner"
    ADMIN = "admin"
    USER = "user"

    def visit(
        self,
        owner: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserRole.OWNER:
            return owner()
        if self is UserRole.ADMIN:
            return admin()
        if self is UserRole.USER:
            return user()
