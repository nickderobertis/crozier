

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SetUploadPermissionsRequestPublicPermission(enum.StrEnum):
    """
    Select the public permission for this upload
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
        if self is SetUploadPermissionsRequestPublicPermission.NONE:
            return none()
        if self is SetUploadPermissionsRequestPublicPermission.READ_ONLY:
            return read_only()
        if self is SetUploadPermissionsRequestPublicPermission.READ_WRITE:
            return read_write()
        if self is SetUploadPermissionsRequestPublicPermission.CLEARING_ADMIN:
            return clearing_admin()
        if self is SetUploadPermissionsRequestPublicPermission.ADMIN:
            return admin()
