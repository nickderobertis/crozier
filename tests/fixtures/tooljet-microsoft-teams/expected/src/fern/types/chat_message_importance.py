

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatMessageImportance(enum.StrEnum):
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"

    def visit(
        self,
        normal: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        urgent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatMessageImportance.NORMAL:
            return normal()
        if self is ChatMessageImportance.HIGH:
            return high()
        if self is ChatMessageImportance.URGENT:
            return urgent()
