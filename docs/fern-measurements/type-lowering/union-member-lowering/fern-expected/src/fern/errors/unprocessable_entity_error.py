

import typing

from ..core.api_error import ApiError
from ..types.session_problem import SessionProblem


class UnprocessableEntityError(ApiError):
    def __init__(self, body: SessionProblem, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=422, headers=headers, body=body)
