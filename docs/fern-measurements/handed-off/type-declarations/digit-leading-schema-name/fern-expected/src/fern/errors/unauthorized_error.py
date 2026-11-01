

import typing

from ..core.api_error import ApiError
from ..types.four_hundred_one_response import FourHundredOneResponse


class UnauthorizedError(ApiError):
    def __init__(self, body: FourHundredOneResponse, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=401, headers=headers, body=body)
