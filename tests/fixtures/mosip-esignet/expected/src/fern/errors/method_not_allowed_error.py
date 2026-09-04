

import typing

from ..core.api_error import ApiError
from ..types.method_not_allowed_error_body import MethodNotAllowedErrorBody


class MethodNotAllowedError(ApiError):
    def __init__(self, body: MethodNotAllowedErrorBody, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=405, headers=headers, body=body)
