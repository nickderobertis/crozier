

import typing

IdentityVerificationStatus = typing.Union[
    typing.Literal["active", "success", "failed", "expired", "canceled", "pending_review"], typing.Any
]
