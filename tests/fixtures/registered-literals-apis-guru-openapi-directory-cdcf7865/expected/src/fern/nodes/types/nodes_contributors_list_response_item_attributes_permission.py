

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class NodesContributorsListResponseItemAttributesPermission(enum.StrEnum):
    """
    The permission level of the contributor. The default value is 'write'.
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
        if self is NodesContributorsListResponseItemAttributesPermission.READ:
            return read()
        if self is NodesContributorsListResponseItemAttributesPermission.WRITE:
            return write()
        if self is NodesContributorsListResponseItemAttributesPermission.ADMIN:
            return admin()
