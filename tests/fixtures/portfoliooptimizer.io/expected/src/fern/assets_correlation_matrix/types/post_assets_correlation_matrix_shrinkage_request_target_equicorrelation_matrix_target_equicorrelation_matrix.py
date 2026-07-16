

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrixTargetEquicorrelationMatrix(str, enum.Enum):
    """
    The shrinkage target correlation matrix
    """

    MINIMUM_EQUICORRELATION_MATRIX = "minimumEquicorrelationMatrix"
    ZERO_EQUICORRELATION_MATRIX = "zeroEquicorrelationMatrix"
    MAXIMUM_EQUICORRELATION_MATRIX = "maximumEquicorrelationMatrix"

    def visit(
        self,
        minimum_equicorrelation_matrix: typing.Callable[[], T_Result],
        zero_equicorrelation_matrix: typing.Callable[[], T_Result],
        maximum_equicorrelation_matrix: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrixTargetEquicorrelationMatrix.MINIMUM_EQUICORRELATION_MATRIX
        ):
            return minimum_equicorrelation_matrix()
        if (
            self
            is PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrixTargetEquicorrelationMatrix.ZERO_EQUICORRELATION_MATRIX
        ):
            return zero_equicorrelation_matrix()
        if (
            self
            is PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrixTargetEquicorrelationMatrix.MAXIMUM_EQUICORRELATION_MATRIX
        ):
            return maximum_equicorrelation_matrix()
