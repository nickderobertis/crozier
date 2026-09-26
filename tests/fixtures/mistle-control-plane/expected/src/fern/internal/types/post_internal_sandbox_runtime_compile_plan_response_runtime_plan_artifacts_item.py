

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_artifacts_item_lifecycle import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycle,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItem(UniversalBaseModel):
    artifact_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="artifactKey"), pydantic.Field(alias="artifactKey")
    ]
    name: str
    description: typing.Optional[str] = None
    env: typing.Optional[typing.Dict[str, str]] = None
    lifecycle: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycle

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
