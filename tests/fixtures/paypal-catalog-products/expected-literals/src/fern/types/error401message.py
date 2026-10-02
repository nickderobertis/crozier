

import typing

Error401Message = typing.Union[
    typing.Literal["Authentication failed due to missing authorization header, or invalid authentication credentials."],
    typing.Any,
]
