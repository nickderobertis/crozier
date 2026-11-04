

import typing

ActActionResponseStatus = typing.Union[
    typing.Literal[
        "completed",
        "running",
        "awaiting_user",
        "approval_required",
        "authentication_required",
        "connection_required",
        "payment_required",
        "verification_required",
        "insufficient_authority",
        "provider_unavailable",
        "stopped",
    ],
    typing.Any,
]
