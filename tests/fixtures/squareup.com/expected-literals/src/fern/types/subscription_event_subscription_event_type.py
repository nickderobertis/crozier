

import typing

SubscriptionEventSubscriptionEventType = typing.Union[
    typing.Literal[
        "START_SUBSCRIPTION", "PLAN_CHANGE", "STOP_SUBSCRIPTION", "DEACTIVATE_SUBSCRIPTION", "RESUME_SUBSCRIPTION"
    ],
    typing.Any,
]
