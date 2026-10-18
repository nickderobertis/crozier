

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SigningKeysResponseOutputKeysItemStatus(enum.StrEnum):
    IN_USE = "in_use"
    PREVIOUSLY_USED = "previously_used"
    REVOKED = "revoked"
    STANDBY = "standby"

    def visit(
        self,
        in_use: typing.Callable[[], T_Result],
        previously_used: typing.Callable[[], T_Result],
        revoked: typing.Callable[[], T_Result],
        standby: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SigningKeysResponseOutputKeysItemStatus.IN_USE:
            return in_use()
        if self is SigningKeysResponseOutputKeysItemStatus.PREVIOUSLY_USED:
            return previously_used()
        if self is SigningKeysResponseOutputKeysItemStatus.REVOKED:
            return revoked()
        if self is SigningKeysResponseOutputKeysItemStatus.STANDBY:
            return standby()
