

import typing

from ..core.api_error import ApiError
from ..types.http_response_body import HttpResponseBody


class BadRequestError(ApiError):
    def __init__(self, body: HttpResponseBody, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=400, headers=headers, body=body)
