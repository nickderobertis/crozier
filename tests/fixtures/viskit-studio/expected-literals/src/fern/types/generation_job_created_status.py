

import typing

GenerationJobCreatedStatus = typing.Union[
    typing.Literal[
        "planned", "queued", "running", "stopping", "stopped", "succeeded", "failed", "partial", "interrupted"
    ],
    typing.Any,
]
