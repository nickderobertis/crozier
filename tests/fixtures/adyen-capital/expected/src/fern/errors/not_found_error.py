

import typing

from ..core.api_error import ApiError
from ..types.default_error_response_entity import DefaultErrorResponseEntity


class NotFoundError(ApiError):
    def __init__(self, body: DefaultErrorResponseEntity, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=404, headers=headers, body=body)
