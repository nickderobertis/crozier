

import typing

from ..core.api_error import ApiError


class LoopDetectedError(ApiError):
    def __init__(self, body: typing.Any, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=508, headers=headers, body=body)
