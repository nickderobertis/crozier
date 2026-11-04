

import typing

from ..core.api_error import ApiError
from ..types.error_envelope import ErrorEnvelope


class RangeNotSatisfiableError(ApiError):
    def __init__(self, body: ErrorEnvelope, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=416, headers=headers, body=body)
