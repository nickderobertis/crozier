

import typing

from ..core.api_error import ApiError
from ..types.bad_request_response import BadRequestResponse


class BadRequestError(ApiError):
    def __init__(self, body: BadRequestResponse, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=400, headers=headers, body=body)
