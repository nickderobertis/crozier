

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SendChatMessageRequestImportance(enum.StrEnum):
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"

    def visit(
        self,
        normal: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        urgent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SendChatMessageRequestImportance.NORMAL:
            return normal()
        if self is SendChatMessageRequestImportance.HIGH:
            return high()
        if self is SendChatMessageRequestImportance.URGENT:
            return urgent()
