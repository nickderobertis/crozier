

import typing

EndpointsErrorCategory = typing.Union[
    typing.Literal["API_ERROR", "AUTHENTICATION_ERROR", "INVALID_REQUEST_ERROR"], typing.Any
]
