

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchRoleIdPermissionsItemEffect(enum.StrEnum):
    ALLOW = "allow"
    DENY = "deny"

    def visit(self, allow: typing.Callable[[], T_Result], deny: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchRoleIdPermissionsItemEffect.ALLOW:
            return allow()
        if self is PatchRoleIdPermissionsItemEffect.DENY:
            return deny()
