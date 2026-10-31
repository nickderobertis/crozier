

import typing

from ..core.api_error import ApiError
from ..types.validation_errors import ValidationErrors


class UnprocessableEntityError(ApiError):
    def __init__(self, body: ValidationErrors, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=422, headers=headers, body=body)
