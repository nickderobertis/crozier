

import typing

IdentityVerificationStepStatus = typing.Union[
    typing.Literal[
        "success",
        "active",
        "failed",
        "waiting_for_prerequisite",
        "not_applicable",
        "skipped",
        "expired",
        "canceled",
        "pending_review",
        "manually_approved",
        "manually_rejected",
    ],
    typing.Any,
]
