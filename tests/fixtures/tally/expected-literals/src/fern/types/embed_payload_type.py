

import typing

EmbedPayloadType = typing.Union[
    typing.Literal["rich", "video", "photo", "link", "pdf", "gist", "image/*", "audio/*"], typing.Any
]
