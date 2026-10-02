

import typing

Action = typing.Union[
    typing.Literal[
        "DROP", "FORWARD_DECAPSULATED", "FORWARD_AS_IS", "PASSTHROUGH", "DUPLICATED_DECAPSULATED", "DUPLICATE_AS_IS"
    ],
    typing.Any,
]
