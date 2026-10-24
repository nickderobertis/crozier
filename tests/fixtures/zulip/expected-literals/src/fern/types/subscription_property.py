

import typing

SubscriptionProperty = typing.Union[
    typing.Literal[
        "color",
        "is_muted",
        "in_home_view",
        "pin_to_top",
        "desktop_notifications",
        "audible_notifications",
        "push_notifications",
        "email_notifications",
        "wildcard_mentions_notify",
    ],
    typing.Any,
]
