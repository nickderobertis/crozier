

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QuayRepoPermission(enum.StrEnum):
    """
    Allowed Quay repository roles for a robot account.
    """

    READ = "read"
    WRITE = "write"
    ADMIN = "admin"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QuayRepoPermission.READ:
            return read()
        if self is QuayRepoPermission.WRITE:
            return write()
        if self is QuayRepoPermission.ADMIN:
            return admin()
