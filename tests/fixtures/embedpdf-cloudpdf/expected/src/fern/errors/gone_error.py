

import typing

from ..core.api_error import ApiError
from ..types.shares_exchange410response import SharesExchange410Response


class GoneError(ApiError):
    def __init__(self, body: SharesExchange410Response, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=410, headers=headers, body=body)
