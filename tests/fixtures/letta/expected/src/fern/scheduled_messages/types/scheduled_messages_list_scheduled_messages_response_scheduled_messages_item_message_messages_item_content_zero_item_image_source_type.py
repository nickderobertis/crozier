

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemImageSourceType(
    enum.StrEnum
):
    BASE64 = "base64"

    def visit(self, base64: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemImageSourceType.BASE64
        ):
            return base64()
