

import typing

V2WorkspaceFileTableImportStatus = typing.Union[
    typing.Literal["uploading", "processing", "completed", "failed", "canceled", "expired"], typing.Any
]
