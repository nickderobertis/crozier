

import typing

RackTypeValue = typing.Union[
    typing.Literal[
        "2-post-frame",
        "4-post-frame",
        "4-post-cabinet",
        "wall-frame",
        "wall-frame-vertical",
        "wall-cabinet",
        "wall-cabinet-vertical",
    ],
    typing.Any,
]
