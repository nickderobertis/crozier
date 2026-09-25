

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RolesRolesItemPermissionsItemEffect(enum.StrEnum):
    ALLOW = "allow"
    DENY = "deny"

    def visit(self, allow: typing.Callable[[], T_Result], deny: typing.Callable[[], T_Result]) -> T_Result:
        if self is RolesRolesItemPermissionsItemEffect.ALLOW:
            return allow()
        if self is RolesRolesItemPermissionsItemEffect.DENY:
            return deny()
