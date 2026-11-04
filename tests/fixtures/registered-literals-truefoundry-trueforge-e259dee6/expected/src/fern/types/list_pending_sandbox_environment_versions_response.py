

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pending_sandbox_environment_version import PendingSandboxEnvironmentVersion


class ListPendingSandboxEnvironmentVersionsResponse(UniversalBaseModel):
    data: typing.List[PendingSandboxEnvironmentVersion]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
