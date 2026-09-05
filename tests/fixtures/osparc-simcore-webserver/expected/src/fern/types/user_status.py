

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserStatus(enum.StrEnum):
    CONFIRMATION_PENDING = "CONFIRMATION_PENDING"
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    BANNED = "BANNED"
    DELETED = "DELETED"

    def visit(
        self,
        confirmation_pending: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        banned: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserStatus.CONFIRMATION_PENDING:
            return confirmation_pending()
        if self is UserStatus.ACTIVE:
            return active()
        if self is UserStatus.EXPIRED:
            return expired()
        if self is UserStatus.BANNED:
            return banned()
        if self is UserStatus.DELETED:
            return deleted()
