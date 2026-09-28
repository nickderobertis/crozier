

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionPartTintTintModeOne(enum.StrEnum):
    SCREEN = "screen"

    def visit(self, screen: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionPartTintTintModeOne.SCREEN:
            return screen()
