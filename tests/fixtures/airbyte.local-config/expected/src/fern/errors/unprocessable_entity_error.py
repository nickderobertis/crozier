

import typing

from ..core.api_error import ApiError
from ..types.invalid_input_exception_info import InvalidInputExceptionInfo


class UnprocessableEntityError(ApiError):
    def __init__(self, body: InvalidInputExceptionInfo, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=422, headers=headers, body=body)
