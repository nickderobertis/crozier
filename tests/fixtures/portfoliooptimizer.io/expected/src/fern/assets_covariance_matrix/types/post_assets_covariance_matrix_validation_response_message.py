

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostAssetsCovarianceMatrixValidationResponseMessage(str, enum.Enum):
    """
    Indicates whether the matrix is a valid covariance matrix
    """

    VALID_COVARIANCE_MATRIX = "valid covariance matrix"
    INVALID_COVARIANCE_MATRIX_NON_SYMMETRIC_MATRIX = "invalid covariance matrix - non symmetric matrix"
    INVALID_COVARIANCE_MATRIX_NON_POSITIVE_DIAGONAL_ELEMENTS = (
        "invalid covariance matrix - non positive diagonal elements"
    )
    INVALID_COVARIANCE_MATRIX_NON_POSITIVE_SEMI_DEFINITE_MATRIX = (
        "invalid covariance matrix - non positive semi-definite matrix"
    )

    def visit(
        self,
        valid_covariance_matrix: typing.Callable[[], T_Result],
        invalid_covariance_matrix_non_symmetric_matrix: typing.Callable[[], T_Result],
        invalid_covariance_matrix_non_positive_diagonal_elements: typing.Callable[[], T_Result],
        invalid_covariance_matrix_non_positive_semi_definite_matrix: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostAssetsCovarianceMatrixValidationResponseMessage.VALID_COVARIANCE_MATRIX:
            return valid_covariance_matrix()
        if self is PostAssetsCovarianceMatrixValidationResponseMessage.INVALID_COVARIANCE_MATRIX_NON_SYMMETRIC_MATRIX:
            return invalid_covariance_matrix_non_symmetric_matrix()
        if (
            self
            is PostAssetsCovarianceMatrixValidationResponseMessage.INVALID_COVARIANCE_MATRIX_NON_POSITIVE_DIAGONAL_ELEMENTS
        ):
            return invalid_covariance_matrix_non_positive_diagonal_elements()
        if (
            self
            is PostAssetsCovarianceMatrixValidationResponseMessage.INVALID_COVARIANCE_MATRIX_NON_POSITIVE_SEMI_DEFINITE_MATRIX
        ):
            return invalid_covariance_matrix_non_positive_semi_definite_matrix()
