

import typing

AttemptFailureOrigin = typing.Union[
    typing.Literal[
        "source", "destination", "replication", "persistence", "normalization", "dbt", "airbyte_platform", "unknown"
    ],
    typing.Any,
]
