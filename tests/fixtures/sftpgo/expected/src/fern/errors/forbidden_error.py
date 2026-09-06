

import typing

from ..core.api_error import ApiError
from ..types.api_response import ApiResponse


class ForbiddenError(ApiError):
    def __init__(self, body: ApiResponse, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=403, headers=headers, body=body)
