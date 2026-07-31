

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UMemberJoinedRole(enum.StrEnum):
    OWNER = "owner"
    EDITOR = "editor"
    VIEWER = "viewer"

    def visit(
        self,
        owner: typing.Callable[[], T_Result],
        editor: typing.Callable[[], T_Result],
        viewer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UMemberJoinedRole.OWNER:
            return owner()
        if self is UMemberJoinedRole.EDITOR:
            return editor()
        if self is UMemberJoinedRole.VIEWER:
            return viewer()
