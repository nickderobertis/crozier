

import typing

EventConditionsFsEventsItem = typing.Union[
    typing.Literal[
        "upload",
        "download",
        "delete",
        "rename",
        "mkdir",
        "rmdir",
        "copy",
        "ssh_cmd",
        "pre-upload",
        "pre-download",
        "pre-delete",
        "first-upload",
        "first-download",
    ],
    typing.Any,
]
