

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SetUploadPermissionsRequestNewPermission(enum.StrEnum):
    """
    Select the permission for selected group
    """

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
        if self is SetUploadPermissionsRequestNewPermission.NONE:
            return none()
        if self is SetUploadPermissionsRequestNewPermission.READ_ONLY:
            return read_only()
        if self is SetUploadPermissionsRequestNewPermission.READ_WRITE:
            return read_write()
        if self is SetUploadPermissionsRequestNewPermission.CLEARING_ADMIN:
            return clearing_admin()
        if self is SetUploadPermissionsRequestNewPermission.ADMIN:
            return admin()
