

import typing

from ..core.api_error import ApiError
from ..types.error_payment_required import ErrorPaymentRequired


class PaymentRequiredError(ApiError):
    def __init__(self, body: ErrorPaymentRequired, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=402, headers=headers, body=body)
