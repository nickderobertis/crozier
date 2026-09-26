

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_endpoints_item_connection_mode import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemConnectionMode,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_endpoints_item_transport import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemTransport,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItem(UniversalBaseModel):
    endpoint_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="endpointKey"), pydantic.Field(alias="endpointKey")
    ]
    process_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="processKey"), pydantic.Field(alias="processKey")
    ] = None
    transport: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemTransport
    connection_mode: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemConnectionMode,
        FieldMetadata(alias="connectionMode"),
        pydantic.Field(alias="connectionMode"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
