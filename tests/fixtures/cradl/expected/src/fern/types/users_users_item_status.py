

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UsersUsersItemStatus(enum.StrEnum):
    INACTIVE = "inactive"
    ACTIVE = "active"
    INVITE_PENDING = "invite_pending"

    def visit(
        self,
        inactive: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        invite_pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UsersUsersItemStatus.INACTIVE:
            return inactive()
        if self is UsersUsersItemStatus.ACTIVE:
            return active()
        if self is UsersUsersItemStatus.INVITE_PENDING:
            return invite_pending()
