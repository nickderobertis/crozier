

import typing

VaultItemListItemsItemKind = typing.Union[
    typing.Literal[
        "oauth_token",
        "api_key",
        "client_credentials",
        "password",
        "totp_seed",
        "ssh_private_key",
        "certificate",
        "provider_secret",
    ],
    typing.Any,
]
