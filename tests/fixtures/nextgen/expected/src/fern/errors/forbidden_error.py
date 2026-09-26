

import typing

from ..core.api_error import ApiError
from ..types.forbidden1 import Forbidden1


class ForbiddenError(ApiError):
    def __init__(self, body: Forbidden1, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=403, headers=headers, body=body)
