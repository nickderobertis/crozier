

import typing

FileStorageEventType = typing.Union[
    typing.Literal["*", "file-storage.file.created", "file-storage.file.updated", "file-storage.file.deleted"],
    typing.Any,
]
