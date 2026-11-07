

import typing

ConfigCompatibilityLevel = typing.Union[
    typing.Literal[
        "BACKWARD", "BACKWARD_TRANSITIVE", "FORWARD", "FORWARD_TRANSITIVE", "FULL", "FULL_TRANSITIVE", "NONE"
    ],
    typing.Any,
]
