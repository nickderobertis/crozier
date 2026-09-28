

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationFour(enum.StrEnum):
    CURVE = "curve"

    def visit(self, curve: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationFour.CURVE:
            return curve()
