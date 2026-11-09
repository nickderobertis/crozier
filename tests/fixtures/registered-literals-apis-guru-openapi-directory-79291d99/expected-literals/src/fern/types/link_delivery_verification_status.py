

import typing

LinkDeliveryVerificationStatus = typing.Union[
    typing.Literal[
        "automatically_verified",
        "pending_automatic_verification",
        "pending_manual_verification",
        "manually_verified",
        "verification_expired",
        "verification_failed",
    ],
    typing.Any,
]
