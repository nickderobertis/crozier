

import typing

FsEventAction = typing.Union[
    typing.Literal[
        "download", "upload", "first-upload", "first-download", "delete", "rename", "mkdir", "rmdir", "ssh_cmd"
    ],
    typing.Any,
]
