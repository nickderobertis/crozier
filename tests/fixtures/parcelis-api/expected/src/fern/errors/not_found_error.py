

import typing

from ..core.api_error import ApiError
from ..types.error_not_found import ErrorNotFound


class NotFoundError(ApiError):
    def __init__(self, body: ErrorNotFound, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=404, headers=headers, body=body)
