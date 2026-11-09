

import typing

from ..core.api_error import ApiError
from ..types.not_implemented_error_body import NotImplementedErrorBody


class NotImplementedError(ApiError):
    def __init__(self, body: NotImplementedErrorBody, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=501, headers=headers, body=body)
