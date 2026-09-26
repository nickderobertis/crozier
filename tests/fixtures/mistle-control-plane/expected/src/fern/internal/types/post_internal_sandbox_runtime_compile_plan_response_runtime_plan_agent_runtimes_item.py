

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_agent_runtimes_item_capabilities import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilities,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_agent_runtimes_item_pty_launch import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunch,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItem(UniversalBaseModel):
    runtime_id: typing_extensions.Annotated[str, FieldMetadata(alias="runtimeId"), pydantic.Field(alias="runtimeId")]
    runtime_key: typing_extensions.Annotated[str, FieldMetadata(alias="runtimeKey"), pydantic.Field(alias="runtimeKey")]
    client_id: typing_extensions.Annotated[str, FieldMetadata(alias="clientId"), pydantic.Field(alias="clientId")]
    endpoint_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="endpointKey"), pydantic.Field(alias="endpointKey")
    ]
    pty_launch: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunch,
        FieldMetadata(alias="ptyLaunch"),
        pydantic.Field(alias="ptyLaunch"),
    ]
    capabilities: typing.Optional[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilities
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
