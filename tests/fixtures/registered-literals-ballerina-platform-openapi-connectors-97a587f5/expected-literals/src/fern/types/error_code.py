

import typing

ErrorCode = typing.Union[
    typing.Literal[
        "conflict",
        "invalidPayload",
        "forbidden",
        "notFound",
        "unexpectedEntityState",
        "itemDoesAlreadyExist",
        "serviceUnavailable",
        "internalFailure",
        "quotaExceeded",
        "jsonlValidationFailed",
        "fileImportFailed",
    ],
    typing.Any,
]
