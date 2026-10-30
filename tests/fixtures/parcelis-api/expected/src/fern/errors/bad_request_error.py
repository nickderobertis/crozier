

import typing

from ..core.api_error import ApiError
from ..types.error_bad_request import ErrorBadRequest


class BadRequestError(ApiError):
    def __init__(self, body: ErrorBadRequest, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=400, headers=headers, body=body)
