

import typing

from ..core.api_error import ApiError
from ..types.bad_request_exception import BadRequestException


class BadRequestError(ApiError):
    def __init__(self, body: BadRequestException, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=400, headers=headers, body=body)
