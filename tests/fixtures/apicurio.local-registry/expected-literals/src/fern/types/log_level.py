

import typing

LogLevel = typing.Union[
    typing.Literal["DEBUG", "TRACE", "WARN", "ERROR", "SEVERE", "WARNING", "INFO", "CONFIG", "FINE", "FINER", "FINEST"],
    typing.Any,
]
