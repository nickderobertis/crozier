

import typing

from ..core.api_error import ApiError
from ..types.error_throttled import ErrorThrottled


class TooManyRequestsError(ApiError):
    def __init__(self, body: ErrorThrottled, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=429, headers=headers, body=body)
