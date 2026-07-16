

import typing

from ..core.api_error import ApiError
from ..types.ob_error_response1 import ObErrorResponse1


class ForbiddenError(ApiError):
    def __init__(self, body: ObErrorResponse1, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=403, headers=headers, body=body)
