

import typing

KnownUnionsDataType = typing.Union[
    typing.Literal["boolean", "date", "datetime", "geometry", "integer", "number", "string", "time", "unknown"],
    typing.Any,
]
