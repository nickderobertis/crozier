

import typing

from ..core.api_error import ApiError


class ClientRequestError(ApiError):
    def __init__(
        self,
        body: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        status_code: typing.Optional[int] = None,
    ):
        super().__init__(status_code=status_code if status_code is not None else 400, headers=headers, body=body)
