

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workspace_api_ocs_create_response_ocs import WorkspaceApiOcsCreateResponseOcs


class WorkspaceApiOcsCreateResponse(UniversalBaseModel):
    ocs: WorkspaceApiOcsCreateResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
