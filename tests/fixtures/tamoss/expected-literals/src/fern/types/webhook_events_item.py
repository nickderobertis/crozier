

import typing

WebhookEventsItem = typing.Union[
    typing.Literal[
        "flows/created",
        "flows/updated",
        "flows/deleted",
        "flows/segments_added",
        "flows/segments_deleted",
        "sources/created",
        "sources/updated",
        "sources/deleted",
    ],
    typing.Any,
]
