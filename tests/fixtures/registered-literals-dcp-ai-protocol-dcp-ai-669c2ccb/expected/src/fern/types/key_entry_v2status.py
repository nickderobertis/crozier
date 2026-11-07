

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KeyEntryV2Status(enum.StrEnum):
    ACTIVE = "active"
    REVOKED = "revoked"
    EXPIRED = "expired"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        revoked: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is KeyEntryV2Status.ACTIVE:
            return active()
        if self is KeyEntryV2Status.REVOKED:
            return revoked()
        if self is KeyEntryV2Status.EXPIRED:
            return expired()
