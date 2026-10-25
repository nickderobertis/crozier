

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RoomStatusStatus(enum.StrEnum):
    OPEN = "open"
    FINALIZED = "finalized"

    def visit(self, open: typing.Callable[[], T_Result], finalized: typing.Callable[[], T_Result]) -> T_Result:
        if self is RoomStatusStatus.OPEN:
            return open()
        if self is RoomStatusStatus.FINALIZED:
            return finalized()
