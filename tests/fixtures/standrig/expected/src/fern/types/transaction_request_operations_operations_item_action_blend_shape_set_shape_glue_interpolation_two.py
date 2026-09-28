

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationTwo(enum.StrEnum):
    SMOOTHSTEP = "smoothstep"

    def visit(self, smoothstep: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationTwo.SMOOTHSTEP:
            return smoothstep()
