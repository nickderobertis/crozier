

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_agent_runtimes_item_pty_launch_new_launch_args_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchNewLaunchArgsItem,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchNewLaunch(UniversalBaseModel):
    pty_session_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="ptySessionId"), pydantic.Field(alias="ptySessionId")
    ]
    cols: int
    rows: int
    cwd: typing.Optional[str] = None
    command: str
    args: typing.List[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemPtyLaunchNewLaunchArgsItem
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
