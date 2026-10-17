

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NetworkRestrictionsV2ResponseOutputEntitlement(enum.StrEnum):
    DISALLOWED = "disallowed"
    ALLOWED = "allowed"

    def visit(self, disallowed: typing.Callable[[], T_Result], allowed: typing.Callable[[], T_Result]) -> T_Result:
        if self is NetworkRestrictionsV2ResponseOutputEntitlement.DISALLOWED:
            return disallowed()
        if self is NetworkRestrictionsV2ResponseOutputEntitlement.ALLOWED:
            return allowed()
