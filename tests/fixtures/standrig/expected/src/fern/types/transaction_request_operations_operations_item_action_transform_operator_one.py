

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionTransformOperatorOne(enum.StrEnum):
    SET = "set"

    def visit(self, set_: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionTransformOperatorOne.SET:
            return set_()
