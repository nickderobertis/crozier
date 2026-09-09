

import typing

from ..core.api_error import ApiError
from ..types.error500 import Error500


class InternalServerError(ApiError):
    def __init__(self, body: Error500, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=500, headers=headers, body=body)
