

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelStatus(enum.StrEnum):
    OPENING = "Opening"
    OPENED = "Opened"
    CLOSING = "Closing"

    def visit(
        self,
        opening: typing.Callable[[], T_Result],
        opened: typing.Callable[[], T_Result],
        closing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelStatus.OPENING:
            return opening()
        if self is ChannelStatus.OPENED:
            return opened()
        if self is ChannelStatus.CLOSING:
            return closing()
