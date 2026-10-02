

import typing

SshAuthentications = typing.Union[
    typing.Literal[
        "publickey", "password", "keyboard-interactive", "publickey+password", "publickey+keyboard-interactive"
    ],
    typing.Any,
]
