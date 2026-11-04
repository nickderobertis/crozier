

import typing

BillingVerificationErrorCode = typing.Union[
    typing.Literal[
        "renewal_verification_pending", "renewal_verification_failed", "entitlement_verification_unavailable"
    ],
    typing.Any,
]
