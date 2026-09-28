

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionPartBlendModeModeOne(enum.StrEnum):
    NORMAL = "normal"

    def visit(self, normal: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionPartBlendModeModeOne.NORMAL:
            return normal()
