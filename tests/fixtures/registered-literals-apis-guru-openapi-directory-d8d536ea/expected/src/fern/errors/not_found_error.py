

import typing

from ..core.api_error import ApiError
from ..types.exception import Exception


class NotFoundError(ApiError):
    def __init__(self, body: typing.Optional[Exception], headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=404, headers=headers, body=body)
