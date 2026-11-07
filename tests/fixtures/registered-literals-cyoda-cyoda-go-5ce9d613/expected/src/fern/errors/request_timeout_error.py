

import typing

from ..core.api_error import ApiError
from ..types.problem_detail_dto import ProblemDetailDto


class RequestTimeoutError(ApiError):
    def __init__(self, body: ProblemDetailDto, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=408, headers=headers, body=body)
