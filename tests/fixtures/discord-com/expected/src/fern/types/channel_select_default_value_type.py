

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelSelectDefaultValueType(enum.StrEnum):
    CHANNEL = "channel"

    def visit(self, channel: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelSelectDefaultValueType.CHANNEL:
            return channel()
