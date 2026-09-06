

import typing

from ..core.api_error import ApiError
from ..types.validation_error_response import ValidationErrorResponse


class BadRequestError(ApiError):
    def __init__(self, body: ValidationErrorResponse, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=400, headers=headers, body=body)
