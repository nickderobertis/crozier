

import typing

from ..core.api_error import ApiError
from ..types.approval_error import ApprovalError


class TooManyRequestsError(ApiError):
    def __init__(self, body: ApprovalError, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=429, headers=headers, body=body)
