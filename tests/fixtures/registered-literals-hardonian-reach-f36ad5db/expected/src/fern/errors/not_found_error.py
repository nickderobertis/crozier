

import typing

from ..core.api_error import ApiError
from ..types.reach_error import ReachError


class NotFoundError(ApiError):
    def __init__(self, body: ReachError, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=404, headers=headers, body=body)
