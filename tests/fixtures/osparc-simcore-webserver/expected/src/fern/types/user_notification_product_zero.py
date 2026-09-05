

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserNotificationProductZero(enum.StrEnum):
    UNDEFINED = "UNDEFINED"

    def visit(self, undefined: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserNotificationProductZero.UNDEFINED:
            return undefined()
