

import typing

from ..core.api_error import ApiError
from ..types.ia_no_disponible_response import IaNoDisponibleResponse


class ServiceUnavailableError(ApiError):
    def __init__(self, body: IaNoDisponibleResponse, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=503, headers=headers, body=body)
