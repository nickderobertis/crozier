

import typing

ValidationInputRequestValidationType = typing.Union[
    typing.Literal[
        "ValidateAddress",
        "ValidateDataDestinationDetails",
        "ValidateSubscriptionIsAllowedToCreateJob",
        "ValidatePreferences",
        "ValidateCreateOrderLimit",
        "ValidateSkuAvailability",
    ],
    typing.Any,
]
