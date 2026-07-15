

import typing

from ..core.api_error import ApiError
from ..types.known_exception_info import KnownExceptionInfo


class BadRequestError(ApiError):
    def __init__(self, body: KnownExceptionInfo, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=400, headers=headers, body=body)
