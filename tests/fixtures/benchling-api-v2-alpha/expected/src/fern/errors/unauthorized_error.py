

import typing

from ..core.api_error import ApiError
from ..types.o_auth_unauthorized_error import OAuthUnauthorizedError


class UnauthorizedError(ApiError):
    def __init__(self, body: OAuthUnauthorizedError, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=401, headers=headers, body=body)
