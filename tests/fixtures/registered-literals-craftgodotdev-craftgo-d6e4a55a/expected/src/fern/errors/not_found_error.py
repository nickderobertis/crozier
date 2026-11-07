

import typing

from ..core.api_error import ApiError
from ..types.order_not_found_err import OrderNotFoundErr


class NotFoundError(ApiError):
    def __init__(self, body: OrderNotFoundErr, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=404, headers=headers, body=body)
