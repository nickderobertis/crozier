

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric(enum.StrEnum):
    """
    The distance metric to use to compute the informativeness of the asset correlation matrix
    """

    EUCLIDEAN = "euclidean"
    CORRELATION_MATRIX = "correlationMatrix"
    BURES = "bures"

    def visit(
        self,
        euclidean: typing.Callable[[], T_Result],
        correlation_matrix: typing.Callable[[], T_Result],
        bures: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric.EUCLIDEAN:
            return euclidean()
        if self is PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric.CORRELATION_MATRIX:
            return correlation_matrix()
        if self is PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric.BURES:
            return bures()
