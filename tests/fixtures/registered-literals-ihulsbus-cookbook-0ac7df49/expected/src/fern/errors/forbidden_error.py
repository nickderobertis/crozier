

import typing

from ..core.api_error import ApiError


class ForbiddenError(ApiError):
    def __init__(self, body: str, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=403, headers=headers, body=body)
