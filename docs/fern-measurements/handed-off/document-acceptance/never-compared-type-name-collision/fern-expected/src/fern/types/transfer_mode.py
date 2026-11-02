

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferMode(enum.StrEnum):
    HAND = "HAND"
    DROP = "DROP"
    LOCKER = "LOCKER"
    RETURN = "RETURN"

    def visit(
        self,
        hand: typing.Callable[[], T_Result],
        drop: typing.Callable[[], T_Result],
        locker: typing.Callable[[], T_Result],
        return_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferMode.HAND:
            return hand()
        if self is TransferMode.DROP:
            return drop()
        if self is TransferMode.LOCKER:
            return locker()
        if self is TransferMode.RETURN:
            return return_()
