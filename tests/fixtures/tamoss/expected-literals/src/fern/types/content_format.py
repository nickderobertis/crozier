

import typing

ContentFormat = typing.Union[
    typing.Literal[
        "urn:x-nmos:format:video",
        "urn:x-tam:format:image",
        "urn:x-nmos:format:audio",
        "urn:x-nmos:format:data",
        "urn:x-nmos:format:multi",
    ],
    typing.Any,
]
