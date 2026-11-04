

import typing

DependencyEdgeToType = typing.Union[
    typing.Literal[
        "data_source", "asset", "widget", "layout", "playlist", "campaign", "schedule", "screen_group", "screen"
    ],
    typing.Any,
]
