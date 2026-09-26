

import typing

from ..core.api_error import ApiError
from ..types.api_error_response import ApiErrorResponse


class ServiceUnavailableError(ApiError):
    def __init__(self, body: ApiErrorResponse, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=503, headers=headers, body=body)
