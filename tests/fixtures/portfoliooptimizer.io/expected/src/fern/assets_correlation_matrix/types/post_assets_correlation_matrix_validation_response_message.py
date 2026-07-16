

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostAssetsCorrelationMatrixValidationResponseMessage(str, enum.Enum):
    """
    Indicates whether the matrix is a valid correlation matrix
    """

    VALID_CORRELATION_MATRIX = "valid correlation matrix"
    INVALID_CORRELATION_MATRIX_NON_SYMMETRIC_MATRIX = "invalid correlation matrix - non symmetric matrix"
    INVALID_CORRELATION_MATRIX_NON_POSITIVE_DIAGONAL_ELEMENTS = (
        "invalid correlation matrix - non positive diagonal elements"
    )
    INVALID_CORRELATION_MATRIX_NON_POSITIVE_SEMI_DEFINITE_MATRIX = (
        "invalid correlation matrix - non positive semi-definite matrix"
    )

    def visit(
        self,
        valid_correlation_matrix: typing.Callable[[], T_Result],
        invalid_correlation_matrix_non_symmetric_matrix: typing.Callable[[], T_Result],
        invalid_correlation_matrix_non_positive_diagonal_elements: typing.Callable[[], T_Result],
        invalid_correlation_matrix_non_positive_semi_definite_matrix: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostAssetsCorrelationMatrixValidationResponseMessage.VALID_CORRELATION_MATRIX:
            return valid_correlation_matrix()
        if self is PostAssetsCorrelationMatrixValidationResponseMessage.INVALID_CORRELATION_MATRIX_NON_SYMMETRIC_MATRIX:
            return invalid_correlation_matrix_non_symmetric_matrix()
        if (
            self
            is PostAssetsCorrelationMatrixValidationResponseMessage.INVALID_CORRELATION_MATRIX_NON_POSITIVE_DIAGONAL_ELEMENTS
        ):
            return invalid_correlation_matrix_non_positive_diagonal_elements()
        if (
            self
            is PostAssetsCorrelationMatrixValidationResponseMessage.INVALID_CORRELATION_MATRIX_NON_POSITIVE_SEMI_DEFINITE_MATRIX
        ):
            return invalid_correlation_matrix_non_positive_semi_definite_matrix()
