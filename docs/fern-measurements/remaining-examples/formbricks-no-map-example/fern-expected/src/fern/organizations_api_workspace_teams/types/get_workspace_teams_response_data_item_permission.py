

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWorkspaceTeamsResponseDataItemPermission(enum.StrEnum):
    """
    Level of access granted to the Workspace
    """

    READ = "read"
    READ_WRITE = "readWrite"
    MANAGE = "manage"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        read_write: typing.Callable[[], T_Result],
        manage: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWorkspaceTeamsResponseDataItemPermission.READ:
            return read()
        if self is GetWorkspaceTeamsResponseDataItemPermission.READ_WRITE:
            return read_write()
        if self is GetWorkspaceTeamsResponseDataItemPermission.MANAGE:
            return manage()
