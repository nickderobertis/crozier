

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopologyOne(enum.StrEnum):
    ALPHA_CONTOUR = "alpha-contour"

    def visit(self, alpha_contour: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopologyOne.ALPHA_CONTOUR:
            return alpha_contour()
