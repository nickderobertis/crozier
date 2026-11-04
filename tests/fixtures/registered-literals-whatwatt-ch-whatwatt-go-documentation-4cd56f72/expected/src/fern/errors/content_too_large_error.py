

import typing

from ..core.api_error import ApiError
from ..types.content_too_large_error_body import ContentTooLargeErrorBody


class ContentTooLargeError(ApiError):
    def __init__(self, body: ContentTooLargeErrorBody, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=413, headers=headers, body=body)
