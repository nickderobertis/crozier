

import typing

from ..core.api_error import ApiError
from ..types.shares_exchange422response import SharesExchange422Response


class UnprocessableEntityError(ApiError):
    def __init__(self, body: SharesExchange422Response, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=422, headers=headers, body=body)
