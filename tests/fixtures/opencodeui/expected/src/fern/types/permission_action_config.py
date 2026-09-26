

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PermissionActionConfig(enum.StrEnum):
    ASK = "ask"
    ALLOW = "allow"
    DENY = "deny"

    def visit(
        self,
        ask: typing.Callable[[], T_Result],
        allow: typing.Callable[[], T_Result],
        deny: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PermissionActionConfig.ASK:
            return ask()
        if self is PermissionActionConfig.ALLOW:
            return allow()
        if self is PermissionActionConfig.DENY:
            return deny()
