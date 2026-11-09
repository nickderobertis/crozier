

import typing

from ..core.api_error import ApiError
from ..types.info import Info


class PreconditionFailedError(ApiError):
    def __init__(self, body: Info, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=412, headers=headers, body=body)
