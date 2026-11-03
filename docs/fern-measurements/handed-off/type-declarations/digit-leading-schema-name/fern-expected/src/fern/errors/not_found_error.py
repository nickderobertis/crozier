

import typing

from ..core.api_error import ApiError
from ..types.four_hundred_four_not_found import FourHundredFourNotFound


class NotFoundError(ApiError):
    def __init__(self, body: FourHundredFourNotFound, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=404, headers=headers, body=body)
