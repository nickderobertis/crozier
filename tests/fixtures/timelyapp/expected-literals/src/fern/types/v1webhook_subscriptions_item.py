

import typing

V1WebhookSubscriptionsItem = typing.Union[
    typing.Literal[
        "forecasts:created",
        "forecasts:updated",
        "forecasts:deleted",
        "hours:created",
        "hours:updated",
        "hours:deleted",
        "labels:created",
        "labels:updated",
        "labels:deleted",
        "projects:created",
        "projects:updated",
        "projects:deleted",
    ],
    typing.Any,
]
