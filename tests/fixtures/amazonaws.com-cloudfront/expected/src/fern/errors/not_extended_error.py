

import typing

from ..core.api_error import ApiError
from ..types.invalid_ttl_order import InvalidTtlOrder


class NotExtendedError(ApiError):
    def __init__(self, body: InvalidTtlOrder, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=510, headers=headers, body=body)
