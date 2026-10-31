

import typing

from ..core.api_error import ApiError
from ..types.error_unauthorized import ErrorUnauthorized


class UnauthorizedError(ApiError):
    def __init__(self, body: ErrorUnauthorized, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=401, headers=headers, body=body)
