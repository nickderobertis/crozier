

import typing

from ..core.api_error import ApiError
from ..types.n1n2message_transfer_error import N1N2MessageTransferError


class GatewayTimeoutError(ApiError):
    def __init__(self, body: N1N2MessageTransferError, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=504, headers=headers, body=body)
