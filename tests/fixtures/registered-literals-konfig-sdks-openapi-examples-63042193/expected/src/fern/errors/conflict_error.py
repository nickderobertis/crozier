

import typing

from ..core.api_error import ApiError
from ..types.context_create_restriction409response import ContextCreateRestriction409Response


class ConflictError(ApiError):
    def __init__(
        self, body: ContextCreateRestriction409Response, headers: typing.Optional[typing.Dict[str, str]] = None
    ):
        super().__init__(status_code=409, headers=headers, body=body)
