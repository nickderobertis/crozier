

import typing

from ..core.api_error import ApiError
from ..types.error_response import ErrorResponse


class ServerError(ApiError):
    def __init__(
        self,
        body: ErrorResponse,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        status_code: typing.Optional[int] = None,
    ):
        super().__init__(status_code=status_code if status_code is not None else 500, headers=headers, body=body)
