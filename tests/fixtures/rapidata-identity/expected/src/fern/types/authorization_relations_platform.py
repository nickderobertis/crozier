

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthorizationRelationsPlatform(enum.StrEnum):
    """
    Relations on the singleton `platform` object. The model is hierarchical: `admin`
    folds into `viewer`.
    """

    ADMIN = "Admin"
    VIEWER = "Viewer"

    def visit(self, admin: typing.Callable[[], T_Result], viewer: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthorizationRelationsPlatform.ADMIN:
            return admin()
        if self is AuthorizationRelationsPlatform.VIEWER:
            return viewer()
