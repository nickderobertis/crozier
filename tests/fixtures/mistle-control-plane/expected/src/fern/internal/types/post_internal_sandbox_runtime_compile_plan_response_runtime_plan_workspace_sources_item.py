

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_workspace_sources_item_resource_kind import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanWorkspaceSourcesItemResourceKind,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_workspace_sources_item_source_kind import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanWorkspaceSourcesItemSourceKind,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanWorkspaceSourcesItem(UniversalBaseModel):
    source_kind: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanWorkspaceSourcesItemSourceKind,
        FieldMetadata(alias="sourceKind"),
        pydantic.Field(alias="sourceKind"),
    ]
    resource_kind: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanWorkspaceSourcesItemResourceKind,
        FieldMetadata(alias="resourceKind"),
        pydantic.Field(alias="resourceKind"),
    ]
    path: str
    origin_url: typing_extensions.Annotated[str, FieldMetadata(alias="originUrl"), pydantic.Field(alias="originUrl")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
