

import typing

RunObjectLastErrorCode = typing.Union[
    typing.Literal["server_error", "rate_limit_exceeded", "invalid_prompt"], typing.Any
]
