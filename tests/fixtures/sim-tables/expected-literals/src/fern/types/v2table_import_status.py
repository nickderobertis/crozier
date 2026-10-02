

import typing

V2TableImportStatus = typing.Union[
    typing.Literal["uploading", "processing", "completed", "failed", "canceled", "expired"], typing.Any
]
