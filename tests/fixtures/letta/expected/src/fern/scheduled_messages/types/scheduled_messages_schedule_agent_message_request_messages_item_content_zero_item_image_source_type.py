

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSourceType(enum.StrEnum):
    BASE64 = "base64"

    def visit(self, base64: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSourceType.BASE64:
            return base64()
