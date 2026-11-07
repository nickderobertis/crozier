

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VaultConnectionListConnectionsItemStatus(enum.StrEnum):
    ACTIVE = "active"
    UNAVAILABLE = "unavailable"
    REVOKED = "revoked"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
        revoked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VaultConnectionListConnectionsItemStatus.ACTIVE:
            return active()
        if self is VaultConnectionListConnectionsItemStatus.UNAVAILABLE:
            return unavailable()
        if self is VaultConnectionListConnectionsItemStatus.REVOKED:
            return revoked()
