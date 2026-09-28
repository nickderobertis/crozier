

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationZero(enum.StrEnum):
    LINEAR = "linear"

    def visit(self, linear: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationZero.LINEAR:
            return linear()
