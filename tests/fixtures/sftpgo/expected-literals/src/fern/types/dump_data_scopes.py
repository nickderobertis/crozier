

import typing

DumpDataScopes = typing.Union[
    typing.Literal[
        "users", "folders", "groups", "admins", "api_keys", "shares", "actions", "rules", "roles", "ip_lists", "configs"
    ],
    typing.Any,
]
