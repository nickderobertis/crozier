

import typing

ValidationInputResponseValidationType = typing.Union[
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
