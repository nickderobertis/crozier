

import typing

from ..core.api_error import ApiError
from ..types.http_error import HttpError


class BadRequestError(ApiError):
    def __init__(self, body: HttpError, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=400, headers=headers, body=body)
