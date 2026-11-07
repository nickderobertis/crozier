

import typing

QueryableType = typing.Union[
    typing.Literal["string", "uri", "number", "integer", "date", "dateTime", "boolean", "geometry"], typing.Any
]
