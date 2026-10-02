

import typing

PostAssetsCovarianceMatrixValidationResponseMessage = typing.Union[
    typing.Literal[
        "valid covariance matrix",
        "invalid covariance matrix - non symmetric matrix",
        "invalid covariance matrix - non positive diagonal elements",
        "invalid covariance matrix - non positive semi-definite matrix",
    ],
    typing.Any,
]
