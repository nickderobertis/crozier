

import typing

from ..core.api_error import ApiError
from ..types.error_response_dto import ErrorResponseDto


class UnauthorizedError(ApiError):
    def __init__(self, body: ErrorResponseDto, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=401, headers=headers, body=body)
