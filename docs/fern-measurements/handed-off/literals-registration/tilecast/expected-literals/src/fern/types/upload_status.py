

import typing

UploadStatus = typing.Union[
    typing.Literal["pending", "uploading", "finalizing", "finalized", "failed", "expired", "cancelled"], typing.Any
]
