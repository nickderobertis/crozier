

import typing

OauthScope = typing.Union[
    typing.Literal[
        "analytics:read",
        "analytics:write",
        "analytics_config:read",
        "analytics_config:write",
        "auth:read",
        "auth:write",
        "database:read",
        "database:write",
        "domains:read",
        "domains:write",
        "edge_functions:read",
        "edge_functions:write",
        "environment:read",
        "environment:write",
        "organizations:read",
        "organizations:write",
        "projects:read",
        "projects:write",
        "rest:read",
        "rest:write",
        "secrets:read",
        "secrets:write",
        "storage:read",
        "storage:write",
    ],
    typing.Any,
]
