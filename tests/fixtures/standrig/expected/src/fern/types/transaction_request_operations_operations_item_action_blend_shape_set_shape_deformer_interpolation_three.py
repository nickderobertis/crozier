

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationThree(enum.StrEnum):
    ARC = "arc"

    def visit(self, arc: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationThree.ARC:
            return arc()
