

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserAccessLevel(enum.StrEnum):
    NONE = "none"
    READ_ONLY = "read_only"
    READ_WRITE = "read_write"
    CLEARING_ADMIN = "clearing_admin"
    ADMIN = "admin"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        read_only: typing.Callable[[], T_Result],
        read_write: typing.Callable[[], T_Result],
        clearing_admin: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserAccessLevel.NONE:
            return none()
        if self is UserAccessLevel.READ_ONLY:
            return read_only()
        if self is UserAccessLevel.READ_WRITE:
            return read_write()
        if self is UserAccessLevel.CLEARING_ADMIN:
            return clearing_admin()
        if self is UserAccessLevel.ADMIN:
            return admin()
