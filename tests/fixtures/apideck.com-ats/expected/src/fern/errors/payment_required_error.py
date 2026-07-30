

import typing

from ..core.api_error import ApiError
from ..types.payment_required_response import PaymentRequiredResponse


class PaymentRequiredError(ApiError):
    def __init__(self, body: PaymentRequiredResponse, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=402, headers=headers, body=body)
