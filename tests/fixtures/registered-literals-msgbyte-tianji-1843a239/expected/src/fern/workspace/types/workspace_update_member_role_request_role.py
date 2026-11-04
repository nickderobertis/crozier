

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WorkspaceUpdateMemberRoleRequestRole(enum.StrEnum):
    OWNER = "owner"
    ADMIN = "admin"
    READ_ONLY = "readOnly"

    def visit(
        self,
        owner: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        read_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkspaceUpdateMemberRoleRequestRole.OWNER:
            return owner()
        if self is WorkspaceUpdateMemberRoleRequestRole.ADMIN:
            return admin()
        if self is WorkspaceUpdateMemberRoleRequestRole.READ_ONLY:
            return read_only()
