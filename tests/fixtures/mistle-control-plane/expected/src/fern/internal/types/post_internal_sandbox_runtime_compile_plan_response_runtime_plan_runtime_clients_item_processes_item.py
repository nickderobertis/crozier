

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_processes_item_command import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemCommand,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_processes_item_readiness import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadiness,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_processes_item_stop import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemStop,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItem(UniversalBaseModel):
    process_key: typing_extensions.Annotated[str, FieldMetadata(alias="processKey"), pydantic.Field(alias="processKey")]
    command: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemCommand
    readiness: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadiness
    stop: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemStop

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
