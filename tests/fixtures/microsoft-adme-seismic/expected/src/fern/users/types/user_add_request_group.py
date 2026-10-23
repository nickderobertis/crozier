

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UserAddRequestGroup(enum.StrEnum):
    """
    Role to be assigned to the user.
    """

    VIEWER = "viewer"
    EDITOR = "editor"
    ADMIN = "admin"

    def visit(
        self,
        viewer: typing.Callable[[], T_Result],
        editor: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserAddRequestGroup.VIEWER:
            return viewer()
        if self is UserAddRequestGroup.EDITOR:
            return editor()
        if self is UserAddRequestGroup.ADMIN:
            return admin()
