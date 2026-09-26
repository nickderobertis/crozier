

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_endpoints_item_transport_type import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemTransportType,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemTransport(
    UniversalBaseModel
):
    type: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemTransportType
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
