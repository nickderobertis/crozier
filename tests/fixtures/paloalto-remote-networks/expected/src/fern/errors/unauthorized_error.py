

import typing

from ..core.api_error import ApiError
from ..types.generic_error import GenericError


class UnauthorizedError(ApiError):
    def __init__(self, body: GenericError, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=401, headers=headers, body=body)
