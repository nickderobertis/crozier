

import typing

VaultEventType = typing.Union[
    typing.Literal[
        "*",
        "vault.connection.created",
        "vault.connection.updated",
        "vault.connection.disabled",
        "vault.connection.deleted",
        "vault.connection.callable",
        "vault.connection.token_refresh.failed",
    ],
    typing.Any,
]
