

import typing

JobType = typing.Union[
    typing.Literal[
        "get_spec", "check_connection", "discover_schema", "sync", "reset_connection", "connection_updater", "replicate"
    ],
    typing.Any,
]
