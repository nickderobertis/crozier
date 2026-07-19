

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSourceType(enum.StrEnum):
    BASE64 = "base64"

    def visit(self, base64: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSourceType.BASE64
        ):
            return base64()
