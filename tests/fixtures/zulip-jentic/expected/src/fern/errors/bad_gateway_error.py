

import typing

from ..core.api_error import ApiError
from ..types.bad_gateway_error_body import BadGatewayErrorBody


class BadGatewayError(ApiError):
    def __init__(self, body: BadGatewayErrorBody, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=502, headers=headers, body=body)
