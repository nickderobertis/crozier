

import typing

from ..core.api_error import ApiError
from ..types.range_not_satisfiable_error_body import RangeNotSatisfiableErrorBody


class RangeNotSatisfiableError(ApiError):
    def __init__(self, body: RangeNotSatisfiableErrorBody, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=416, headers=headers, body=body)
