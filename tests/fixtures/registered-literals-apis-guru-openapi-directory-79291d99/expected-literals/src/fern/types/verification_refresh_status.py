

import typing

VerificationRefreshStatus = typing.Union[
    typing.Literal[
        "VERIFICATION_REFRESH_STATUS_USER_PRESENCE_REQUIRED",
        "VERIFICATION_REFRESH_SUCCESSFUL",
        "VERIFICATION_REFRESH_NOT_FOUND",
    ],
    typing.Any,
]
