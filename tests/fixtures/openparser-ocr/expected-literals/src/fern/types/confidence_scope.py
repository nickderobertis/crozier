

import typing

ConfidenceScope = typing.Union[
    typing.Literal["detection", "recognition", "classification", "geometry", "answer", "quality"], typing.Any
]
