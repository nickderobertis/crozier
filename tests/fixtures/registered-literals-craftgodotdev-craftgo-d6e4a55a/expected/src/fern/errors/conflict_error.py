

import typing

from ..core.api_error import ApiError
from ..types.payment_failed_err import PaymentFailedErr


class ConflictError(ApiError):
    def __init__(self, body: PaymentFailedErr, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=409, headers=headers, body=body)
