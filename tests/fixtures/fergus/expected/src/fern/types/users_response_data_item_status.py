

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UsersResponseDataItemStatus(enum.StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"
    INVITED = "invited"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        invited: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UsersResponseDataItemStatus.ACTIVE:
            return active()
        if self is UsersResponseDataItemStatus.DISABLED:
            return disabled()
        if self is UsersResponseDataItemStatus.INVITED:
            return invited()
