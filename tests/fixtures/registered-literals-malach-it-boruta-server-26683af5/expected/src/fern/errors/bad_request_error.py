

import typing

from ..core.api_error import ApiError
from ..types.o_auth_error import OAuthError


class BadRequestError(ApiError):
    def __init__(self, body: OAuthError, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=400, headers=headers, body=body)
