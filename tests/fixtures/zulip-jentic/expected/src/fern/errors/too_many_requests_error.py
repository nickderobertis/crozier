

import typing

from ..core.api_error import ApiError
from ..types.rate_limited_error import RateLimitedError


class TooManyRequestsError(ApiError):
    def __init__(self, body: RateLimitedError, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=429, headers=headers, body=body)
