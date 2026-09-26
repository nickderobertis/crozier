

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_agent_runtimes_item_capabilities_associated_resource_delivery import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilitiesAssociatedResourceDelivery,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_agent_runtimes_item_capabilities_conversation_delivery import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilitiesConversationDelivery,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilities(UniversalBaseModel):
    associated_resource_delivery: typing_extensions.Annotated[
        typing.Optional[
            PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilitiesAssociatedResourceDelivery
        ],
        FieldMetadata(alias="associatedResourceDelivery"),
        pydantic.Field(alias="associatedResourceDelivery"),
    ] = None
    conversation_delivery: typing_extensions.Annotated[
        typing.Optional[
            PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilitiesConversationDelivery
        ],
        FieldMetadata(alias="conversationDelivery"),
        pydantic.Field(alias="conversationDelivery"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
