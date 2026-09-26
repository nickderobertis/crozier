

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GameRecordSeat(enum.StrEnum):
    B = "b"
    W = "w"

    def visit(self, b: typing.Callable[[], T_Result], w: typing.Callable[[], T_Result]) -> T_Result:
        if self is GameRecordSeat.B:
            return b()
        if self is GameRecordSeat.W:
            return w()
