

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationChannelResponseStatus(enum.StrEnum):
    ENABLED = "enabled"
    DISABLED = "disabled"

    def visit(self, enabled: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotificationChannelResponseStatus.ENABLED:
            return enabled()
        if self is NotificationChannelResponseStatus.DISABLED:
            return disabled()
