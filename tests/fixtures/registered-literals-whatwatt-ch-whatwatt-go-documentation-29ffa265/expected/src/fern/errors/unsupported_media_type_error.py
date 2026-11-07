

import typing

from ..core.api_error import ApiError
from ..types.unsupported_media_type_error_body import UnsupportedMediaTypeErrorBody


class UnsupportedMediaTypeError(ApiError):
    def __init__(self, body: UnsupportedMediaTypeErrorBody, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=415, headers=headers, body=body)
