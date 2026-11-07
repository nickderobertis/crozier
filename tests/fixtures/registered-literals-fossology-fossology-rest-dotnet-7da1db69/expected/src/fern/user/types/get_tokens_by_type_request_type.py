

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTokensByTypeRequestType(enum.StrEnum):
    ACTIVE = "active"
    EXPIRED = "expired"

    def visit(self, active: typing.Callable[[], T_Result], expired: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTokensByTypeRequestType.ACTIVE:
            return active()
        if self is GetTokensByTypeRequestType.EXPIRED:
            return expired()
