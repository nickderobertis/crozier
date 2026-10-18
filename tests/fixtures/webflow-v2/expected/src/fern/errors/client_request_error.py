

import typing

from ..core.api_error import ApiError
from ..types.client_request_error_body import ClientRequestErrorBody


class ClientRequestError(ApiError):
    def __init__(
        self,
        body: ClientRequestErrorBody,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        status_code: typing.Optional[int] = None,
    ):
        super().__init__(status_code=status_code if status_code is not None else 400, headers=headers, body=body)
