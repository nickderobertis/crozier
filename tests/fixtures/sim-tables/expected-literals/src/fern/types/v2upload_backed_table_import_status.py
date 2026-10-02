

import typing

V2UploadBackedTableImportStatus = typing.Union[
    typing.Literal["uploading", "processing", "completed", "failed", "canceled", "expired"], typing.Any
]
