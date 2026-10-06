

import typing

from ..core.api_error import ApiError
from ..types.error_result_user_is_not_post_creator import ErrorResultUserIsNotPostCreator


class ForbiddenError(ApiError):
    def __init__(self, body: ErrorResultUserIsNotPostCreator, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=403, headers=headers, body=body)
