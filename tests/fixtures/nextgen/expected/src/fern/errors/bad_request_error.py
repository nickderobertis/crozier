

import typing

from ..core.api_error import ApiError
from ..types.bad_request1 import BadRequest1


class BadRequestError(ApiError):
    def __init__(self, body: BadRequest1, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=400, headers=headers, body=body)
