

import typing

from ..core.api_error import ApiError
from ..types.error_internal import ErrorInternal


class InternalServerError(ApiError):
    def __init__(self, body: ErrorInternal, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=500, headers=headers, body=body)
