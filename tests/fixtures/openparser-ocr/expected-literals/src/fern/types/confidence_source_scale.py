

import typing

ConfidenceSourceScale = typing.Union[
    typing.Literal["zero_to_one", "zero_to_hundred", "log_probability", "unknown"], typing.Any
]
