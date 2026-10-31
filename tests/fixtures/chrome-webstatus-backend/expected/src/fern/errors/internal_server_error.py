

import typing

from ..core.api_error import ApiError
from ..types.basic_error_model import BasicErrorModel


class InternalServerError(ApiError):
    def __init__(self, body: BasicErrorModel, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=500, headers=headers, body=body)
