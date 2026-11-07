

import typing

from ..core.api_error import ApiError
from ..types.maintenance_window_err import MaintenanceWindowErr


class ServiceUnavailableError(ApiError):
    def __init__(self, body: MaintenanceWindowErr, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=503, headers=headers, body=body)
