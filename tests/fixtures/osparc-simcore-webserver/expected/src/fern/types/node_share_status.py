

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeShareStatus(enum.StrEnum):
    OPENING = "OPENING"
    OPENED = "OPENED"
    CLOSING = "CLOSING"

    def visit(
        self,
        opening: typing.Callable[[], T_Result],
        opened: typing.Callable[[], T_Result],
        closing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NodeShareStatus.OPENING:
            return opening()
        if self is NodeShareStatus.OPENED:
            return opened()
        if self is NodeShareStatus.CLOSING:
            return closing()
