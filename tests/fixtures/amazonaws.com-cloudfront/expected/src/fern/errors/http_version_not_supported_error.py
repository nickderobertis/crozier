

import typing

from ..core.api_error import ApiError


class HttpVersionNotSupportedError(ApiError):
    def __init__(self, body: typing.Any, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=505, headers=headers, body=body)
