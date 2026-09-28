

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationThree(enum.StrEnum):
    ARC = "arc"

    def visit(self, arc: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationThree.ARC:
            return arc()
