

import typing

from ..core.api_error import ApiError
from ..types.v2error import V2Error


class UnauthorizedError(ApiError):
    def __init__(self, body: V2Error, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=401, headers=headers, body=body)
