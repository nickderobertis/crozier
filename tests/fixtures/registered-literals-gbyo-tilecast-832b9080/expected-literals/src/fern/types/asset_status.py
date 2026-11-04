

import typing

AssetStatus = typing.Union[
    typing.Literal[
        "uploading", "uploaded", "queued", "inspecting", "processing", "ready", "failed", "deleting", "deleted"
    ],
    typing.Any,
]
