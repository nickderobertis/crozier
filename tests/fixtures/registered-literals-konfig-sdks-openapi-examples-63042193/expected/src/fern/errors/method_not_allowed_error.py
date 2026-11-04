

import typing

from ..core.api_error import ApiError
from ..types.project_create_project_default_settings405response import ProjectCreateProjectDefaultSettings405Response


class MethodNotAllowedError(ApiError):
    def __init__(
        self,
        body: ProjectCreateProjectDefaultSettings405Response,
        headers: typing.Optional[typing.Dict[str, str]] = None,
    ):
        super().__init__(status_code=405, headers=headers, body=body)
