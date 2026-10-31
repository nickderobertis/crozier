

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FilteredAdminUserType(enum.StrEnum):
    USER = "user"
    ADMIN = "admin"

    def visit(self, user: typing.Callable[[], T_Result], admin: typing.Callable[[], T_Result]) -> T_Result:
        if self is FilteredAdminUserType.USER:
            return user()
        if self is FilteredAdminUserType.ADMIN:
            return admin()
