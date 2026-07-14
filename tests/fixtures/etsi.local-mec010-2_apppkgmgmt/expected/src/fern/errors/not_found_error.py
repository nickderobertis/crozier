

import typing

from ..core.api_error import ApiError
from ..types.problem_details import ProblemDetails


class NotFoundError(ApiError):
    def __init__(self, body: ProblemDetails, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=404, headers=headers, body=body)
