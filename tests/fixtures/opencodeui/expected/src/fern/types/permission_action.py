

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PermissionAction(enum.StrEnum):
    ALLOW = "allow"
    DENY = "deny"
    ASK = "ask"

    def visit(
        self,
        allow: typing.Callable[[], T_Result],
        deny: typing.Callable[[], T_Result],
        ask: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PermissionAction.ALLOW:
            return allow()
        if self is PermissionAction.DENY:
            return deny()
        if self is PermissionAction.ASK:
            return ask()
