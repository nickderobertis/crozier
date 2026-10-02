

import typing

OauthScope = typing.Union[
    typing.Literal[
        "authorized_user:read",
        "assets:read",
        "assets:write",
        "cms:read",
        "cms:write",
        "comments:read",
        "comments:write",
        "custom_code:read",
        "custom_code:write",
        "ecommerce:read",
        "ecommerce:write",
        "forms:read",
        "forms:write",
        "pages:read",
        "pages:write",
        "components:read",
        "components:write",
        "sites:read",
        "sites:write",
        "users:read",
        "site_activity:read",
        "users:write",
        "workspace:read",
        "workspace:write",
        "site_config:read",
        "site_config:write",
    ],
    typing.Any,
]
