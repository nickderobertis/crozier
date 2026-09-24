

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserStatus(enum.StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"
    INVITED = "invited"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        invited: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserStatus.ACTIVE:
            return active()
        if self is UserStatus.DISABLED:
            return disabled()
        if self is UserStatus.INVITED:
            return invited()
