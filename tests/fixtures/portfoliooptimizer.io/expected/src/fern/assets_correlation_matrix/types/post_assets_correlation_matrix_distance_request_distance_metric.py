

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostAssetsCorrelationMatrixDistanceRequestDistanceMetric(str, enum.Enum):
    """
    The distance metric to use to compute the distance between the asset correlation matrix and the reference correlation matrix
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
        if self is PostAssetsCorrelationMatrixDistanceRequestDistanceMetric.EUCLIDEAN:
            return euclidean()
        if self is PostAssetsCorrelationMatrixDistanceRequestDistanceMetric.CORRELATION_MATRIX:
            return correlation_matrix()
        if self is PostAssetsCorrelationMatrixDistanceRequestDistanceMetric.BURES:
            return bures()
