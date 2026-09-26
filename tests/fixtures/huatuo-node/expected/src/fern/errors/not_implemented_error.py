

import typing

from ..core.api_error import ApiError
from ..types.apis_v1components_error_response import ApisV1ComponentsErrorResponse


class NotImplementedError(ApiError):
    def __init__(self, body: ApisV1ComponentsErrorResponse, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=501, headers=headers, body=body)
