

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrgRole(enum.StrEnum):
    OWNER = "Owner"
    ADMIN = "Admin"
    EDITOR = "Editor"
    VIEWER = "Viewer"

    def visit(
        self,
        owner: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        editor: typing.Callable[[], T_Result],
        viewer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrgRole.OWNER:
            return owner()
        if self is OrgRole.ADMIN:
            return admin()
        if self is OrgRole.EDITOR:
            return editor()
        if self is OrgRole.VIEWER:
            return viewer()
