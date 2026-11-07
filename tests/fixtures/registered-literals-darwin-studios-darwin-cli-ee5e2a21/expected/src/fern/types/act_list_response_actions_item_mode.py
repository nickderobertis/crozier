

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActListResponseActionsItemMode(enum.StrEnum):
    BUY = "buy"
    SELL = "sell"
    CHAT = "chat"
    AUTO = "auto"

    def visit(
        self,
        buy: typing.Callable[[], T_Result],
        sell: typing.Callable[[], T_Result],
        chat: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActListResponseActionsItemMode.BUY:
            return buy()
        if self is ActListResponseActionsItemMode.SELL:
            return sell()
        if self is ActListResponseActionsItemMode.CHAT:
            return chat()
        if self is ActListResponseActionsItemMode.AUTO:
            return auto()
