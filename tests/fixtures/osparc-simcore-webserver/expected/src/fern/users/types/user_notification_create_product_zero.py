

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UserNotificationCreateProductZero(enum.StrEnum):
    UNDEFINED = "UNDEFINED"

    def visit(self, undefined: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserNotificationCreateProductZero.UNDEFINED:
            return undefined()
