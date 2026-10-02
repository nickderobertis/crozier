

import typing

GetRecordHandlerProgressRequestErrorCode = typing.Union[
    typing.Literal[
        "NotUpdatable",
        "InvalidRequest",
        "AccessDenied",
        "InvalidCredentials",
        "AlreadyExists",
        "NotFound",
        "ResourceConflict",
        "Throttling",
        "ServiceLimitExceeded",
        "NotStabilized",
        "GeneralServiceException",
        "ServiceInternalError",
        "NetworkFailure",
        "InternalFailure",
        "InvalidTypeConfiguration",
        "HandlerInternalFailure",
        "NonCompliant",
        "Unknown",
        "UnsupportedTarget",
    ],
    typing.Any,
]
