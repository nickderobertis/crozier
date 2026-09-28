

import typing

from ..core.api_error import ApiError
from ..types.users_post_error409 import UsersPostError409


class ConflictError(ApiError):
    def __init__(self, body: UsersPostError409, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=409, headers=headers, body=body)
