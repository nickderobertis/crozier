

import typing

from ..core.api_error import ApiError
from ..types.http_error_out import HttpErrorOut


class UnauthorizedError(ApiError):
    def __init__(self, body: HttpErrorOut, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=401, headers=headers, body=body)
