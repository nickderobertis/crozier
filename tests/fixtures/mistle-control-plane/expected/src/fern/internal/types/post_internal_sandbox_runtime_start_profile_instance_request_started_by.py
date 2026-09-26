

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_internal_sandbox_runtime_start_profile_instance_request_started_by_kind import (
    PostInternalSandboxRuntimeStartProfileInstanceRequestStartedByKind,
)


class PostInternalSandboxRuntimeStartProfileInstanceRequestStartedBy(UniversalBaseModel):
    kind: PostInternalSandboxRuntimeStartProfileInstanceRequestStartedByKind
    id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
