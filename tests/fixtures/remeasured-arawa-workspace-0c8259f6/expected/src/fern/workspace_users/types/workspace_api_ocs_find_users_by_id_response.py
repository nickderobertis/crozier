

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workspace_api_ocs_find_users_by_id_response_ocs import WorkspaceApiOcsFindUsersByIdResponseOcs


class WorkspaceApiOcsFindUsersByIdResponse(UniversalBaseModel):
    ocs: WorkspaceApiOcsFindUsersByIdResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
