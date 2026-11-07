

import typing

from ..core.api_error import ApiError
from ..types.context_get_restrictions429response import ContextGetRestrictions429Response


class TooManyRequestsError(ApiError):
    def __init__(self, body: ContextGetRestrictions429Response, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=429, headers=headers, body=body)
