

import typing

ImageImportOperationStatus = typing.Union[
    typing.Literal["pending", "queued", "processing", "complete", "failed", "expired"], typing.Any
]
