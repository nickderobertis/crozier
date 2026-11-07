

import typing

AsyncSearchStatusDtoSearchJobStatus = typing.Union[
    typing.Literal["RUNNING", "FAILED", "CANCELLED", "SUCCESSFUL", "NOT_FOUND"], typing.Any
]
