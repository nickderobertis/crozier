

import typing

OauthScope = typing.Union[
    typing.Literal[
        "basic",
        "conversations_read",
        "conversations_write",
        "groups_read",
        "groups_write",
        "profile_read",
        "profile_write",
    ],
    typing.Any,
]
