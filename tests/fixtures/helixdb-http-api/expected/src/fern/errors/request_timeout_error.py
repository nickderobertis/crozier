

import typing

from ..core.api_error import ApiError
from ..types.query_error import QueryError


class RequestTimeoutError(ApiError):
    def __init__(self, body: QueryError, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=408, headers=headers, body=body)
