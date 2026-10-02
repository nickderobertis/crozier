

import typing

GenerationJobStopResponseStatus = typing.Union[
    typing.Literal[
        "planned", "queued", "running", "stopping", "stopped", "succeeded", "failed", "partial", "interrupted"
    ],
    typing.Any,
]
