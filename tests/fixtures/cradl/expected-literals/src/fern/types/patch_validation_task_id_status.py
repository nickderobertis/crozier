

import typing

PatchValidationTaskIdStatus = typing.Union[
    typing.Literal["ready", "in-progress", "succeeded", "failed", "cancelled"], typing.Any
]
