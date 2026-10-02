

import typing

PostWebhooksRegistrationsRequestTopic = typing.Union[
    typing.Literal[
        "listings/update",
        "listings/publish",
        "listings/bumps-ran-out",
        "orders/create",
        "orders/update",
        "payments/create",
        "payments/update",
        "app/uninstalled",
    ],
    typing.Any,
]
