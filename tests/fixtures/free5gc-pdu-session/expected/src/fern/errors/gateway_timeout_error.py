

import typing

from ..core.api_error import ApiError
from ..types.sm_context_create_error import SmContextCreateError


class GatewayTimeoutError(ApiError):
    def __init__(self, body: SmContextCreateError, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=504, headers=headers, body=body)
