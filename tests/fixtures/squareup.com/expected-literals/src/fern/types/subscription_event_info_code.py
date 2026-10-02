

import typing

SubscriptionEventInfoCode = typing.Union[
    typing.Literal[
        "LOCATION_NOT_ACTIVE",
        "LOCATION_CANNOT_ACCEPT_PAYMENT",
        "CUSTOMER_DELETED",
        "CUSTOMER_NO_EMAIL",
        "CUSTOMER_NO_NAME",
    ],
    typing.Any,
]
