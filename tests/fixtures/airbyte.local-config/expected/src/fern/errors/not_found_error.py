

import typing

from ..core.api_error import ApiError
from ..types.not_found_known_exception_info import NotFoundKnownExceptionInfo


class NotFoundError(ApiError):
    def __init__(self, body: NotFoundKnownExceptionInfo, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=404, headers=headers, body=body)
