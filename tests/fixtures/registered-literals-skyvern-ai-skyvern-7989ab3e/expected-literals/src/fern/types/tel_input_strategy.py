

import typing

TelInputStrategy = typing.Union[
    typing.Literal[
        "legacy_sequential", "formatted_sequential", "sequential_national", "atomic_national", "atomic_e164"
    ],
    typing.Any,
]
