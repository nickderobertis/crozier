

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthorizationRelationsBidder(enum.StrEnum):
    """
    Relations on the singleton `bidder` object that carries global RTB access. Grants are
    direct here and, unlike Organization, are never folded in from platform staff.
    """

    ADMIN = "Admin"
    EDITOR = "Editor"
    VIEWER = "Viewer"

    def visit(
        self,
        admin: typing.Callable[[], T_Result],
        editor: typing.Callable[[], T_Result],
        viewer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthorizationRelationsBidder.ADMIN:
            return admin()
        if self is AuthorizationRelationsBidder.EDITOR:
            return editor()
        if self is AuthorizationRelationsBidder.VIEWER:
            return viewer()
