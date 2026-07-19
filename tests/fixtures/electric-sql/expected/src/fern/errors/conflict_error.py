

import typing

from ..core.api_error import ApiError
from ..types.conflict_error_body_item import ConflictErrorBodyItem


class ConflictError(ApiError):
    def __init__(
        self, body: typing.List[ConflictErrorBodyItem], headers: typing.Optional[typing.Dict[str, str]] = None
    ):
        super().__init__(status_code=409, headers=headers, body=body)
