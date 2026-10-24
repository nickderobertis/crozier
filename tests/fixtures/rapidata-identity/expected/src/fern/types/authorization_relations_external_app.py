

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthorizationRelationsExternalApp(enum.StrEnum):
    """
    Relations on an `external_app` object — one object per third-party app that federates
    on the OIDC `groups` claim. The apps themselves are `ExternalAppId`. The ladder is hierarchical: `admin` folds into `viewer`.
    Grants are direct and, like `Bidder`, are never folded in from platform staff —
    holding platform admin must not confer administration of a separate system.
    """

    ADMIN = "Admin"
    VIEWER = "Viewer"

    def visit(self, admin: typing.Callable[[], T_Result], viewer: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthorizationRelationsExternalApp.ADMIN:
            return admin()
        if self is AuthorizationRelationsExternalApp.VIEWER:
            return viewer()
