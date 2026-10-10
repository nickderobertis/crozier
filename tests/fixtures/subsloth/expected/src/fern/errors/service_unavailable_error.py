

import typing

from ..core.api_error import ApiError
from ..types.error_response import ErrorResponse


class ServiceUnavailableError(ApiError):
    def __init__(self, body: ErrorResponse, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=503, headers=headers, body=body)
