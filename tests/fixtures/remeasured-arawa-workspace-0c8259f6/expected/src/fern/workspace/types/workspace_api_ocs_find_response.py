

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workspace_api_ocs_find_response_ocs import WorkspaceApiOcsFindResponseOcs


class WorkspaceApiOcsFindResponse(UniversalBaseModel):
    ocs: WorkspaceApiOcsFindResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
