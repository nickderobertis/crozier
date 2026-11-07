

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WorkspaceInviteRequestRole(enum.StrEnum):
    ADMIN = "admin"
    READ_ONLY = "readOnly"

    def visit(self, admin: typing.Callable[[], T_Result], read_only: typing.Callable[[], T_Result]) -> T_Result:
        if self is WorkspaceInviteRequestRole.ADMIN:
            return admin()
        if self is WorkspaceInviteRequestRole.READ_ONLY:
            return read_only()
