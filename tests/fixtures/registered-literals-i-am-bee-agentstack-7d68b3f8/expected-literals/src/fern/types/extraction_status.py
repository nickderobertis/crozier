

import typing

ExtractionStatus = typing.Union[
    typing.Literal["pending", "in_progress", "completed", "failed", "cancelled"], typing.Any
]
