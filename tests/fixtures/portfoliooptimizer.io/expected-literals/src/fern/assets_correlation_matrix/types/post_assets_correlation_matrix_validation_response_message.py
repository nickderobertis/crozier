

import typing

PostAssetsCorrelationMatrixValidationResponseMessage = typing.Union[
    typing.Literal[
        "valid correlation matrix",
        "invalid correlation matrix - non symmetric matrix",
        "invalid correlation matrix - non positive diagonal elements",
        "invalid correlation matrix - non positive semi-definite matrix",
    ],
    typing.Any,
]
