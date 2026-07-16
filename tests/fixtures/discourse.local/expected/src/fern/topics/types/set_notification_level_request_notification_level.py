

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SetNotificationLevelRequestNotificationLevel(enum.StrEnum):
    ZERO = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"

    def visit(
        self,
        zero: typing.Callable[[], T_Result],
        one: typing.Callable[[], T_Result],
        two: typing.Callable[[], T_Result],
        three: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SetNotificationLevelRequestNotificationLevel.ZERO:
            return zero()
        if self is SetNotificationLevelRequestNotificationLevel.ONE:
            return one()
        if self is SetNotificationLevelRequestNotificationLevel.TWO:
            return two()
        if self is SetNotificationLevelRequestNotificationLevel.THREE:
            return three()
