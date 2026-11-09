

import typing

PublishJobStatus = typing.Union[
    typing.Literal["QUEUED", "SCHEDULED", "IN_PROGRESS", "DISPATCHED", "COMPLETED", "FAILED"], typing.Any
]
