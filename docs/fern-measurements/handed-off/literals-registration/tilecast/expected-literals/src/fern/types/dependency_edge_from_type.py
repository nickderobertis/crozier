

import typing

DependencyEdgeFromType = typing.Union[
    typing.Literal[
        "data_source", "asset", "widget", "layout", "playlist", "campaign", "schedule", "screen_group", "screen"
    ],
    typing.Any,
]
