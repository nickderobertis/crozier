

import typing

ProtocolErrorError = typing.Union[
    typing.Literal[
        "invalid_argument",
        "unknown_command",
        "unknown_error",
        "no_such_run",
        "no_such_subscription",
        "no_such_namespace",
        "no_such_interrupt",
        "no_such_checkpoint",
        "permission_denied",
        "not_supported",
    ],
    typing.Any,
]
