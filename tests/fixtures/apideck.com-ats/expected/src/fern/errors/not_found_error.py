

import typing

from ..core.api_error import ApiError
from ..types.not_found_response import NotFoundResponse


class NotFoundError(ApiError):
    def __init__(self, body: NotFoundResponse, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=404, headers=headers, body=body)
