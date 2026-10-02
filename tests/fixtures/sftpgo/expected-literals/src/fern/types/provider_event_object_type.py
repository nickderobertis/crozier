

import typing

ProviderEventObjectType = typing.Union[
    typing.Literal["user", "folder", "group", "admin", "api_key", "share", "event_action", "event_rule", "role"],
    typing.Any,
]
