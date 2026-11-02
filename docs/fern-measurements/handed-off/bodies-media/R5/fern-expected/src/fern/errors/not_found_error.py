

import typing

from ..core.api_error import ApiError
from ..types.lock_fault import LockFault


class NotFoundError(ApiError):
    def __init__(self, body: typing.Optional[LockFault], headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=404, headers=headers, body=body)
