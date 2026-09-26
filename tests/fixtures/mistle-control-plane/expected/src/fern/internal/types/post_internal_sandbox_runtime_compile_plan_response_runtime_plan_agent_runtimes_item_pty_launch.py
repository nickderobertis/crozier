

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_agent_runtimes_item_pty_launch_new_launch import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchNewLaunch,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_agent_runtimes_item_pty_launch_resume_launch import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchResumeLaunch,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunch(UniversalBaseModel):
    runtime_id: typing_extensions.Annotated[str, FieldMetadata(alias="runtimeId"), pydantic.Field(alias="runtimeId")]
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    new_launch: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchNewLaunch,
        FieldMetadata(alias="newLaunch"),
        pydantic.Field(alias="newLaunch"),
    ]
    resume_launch: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchResumeLaunch,
        FieldMetadata(alias="resumeLaunch"),
        pydantic.Field(alias="resumeLaunch"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
