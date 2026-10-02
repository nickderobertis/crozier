

import typing

JobConfigType = typing.Union[
    typing.Literal[
        "check_connection_source",
        "check_connection_destination",
        "discover_schema",
        "get_spec",
        "sync",
        "reset_connection",
    ],
    typing.Any,
]
