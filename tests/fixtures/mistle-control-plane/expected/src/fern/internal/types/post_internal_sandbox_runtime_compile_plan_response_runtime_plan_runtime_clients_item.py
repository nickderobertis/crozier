

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_endpoints_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItem,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_processes_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItem,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_setup import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetup,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItem(UniversalBaseModel):
    client_id: typing_extensions.Annotated[str, FieldMetadata(alias="clientId"), pydantic.Field(alias="clientId")]
    setup: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetup
    processes: typing.List[PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItem]
    endpoints: typing.List[PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
