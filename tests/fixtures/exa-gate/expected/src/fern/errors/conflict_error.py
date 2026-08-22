

import typing

from ..core.api_error import ApiError
from ..types.proxy_error import ProxyError


class ConflictError(ApiError):
    def __init__(self, body: ProxyError, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=409, headers=headers, body=body)
