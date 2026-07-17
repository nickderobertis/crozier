

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod(enum.StrEnum):
    """
    The method used to denoise the asset correlation matrix
    """

    EIGENVALUES_CLIPPING = "eigenvaluesClipping"

    def visit(self, eigenvalues_clipping: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod.EIGENVALUES_CLIPPING:
            return eigenvalues_clipping()
