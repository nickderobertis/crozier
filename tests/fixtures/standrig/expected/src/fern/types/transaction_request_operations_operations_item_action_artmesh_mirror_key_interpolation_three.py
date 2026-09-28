

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationThree(enum.StrEnum):
    ARC = "arc"

    def visit(self, arc: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationThree.ARC:
            return arc()
