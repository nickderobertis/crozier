

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_agent_runtimes_item_capabilities_conversation_delivery_create_conversation_retry_policy import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilitiesConversationDeliveryCreateConversationRetryPolicy,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilitiesConversationDelivery(
    UniversalBaseModel
):
    idempotency_fingerprint_runtime_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="idempotencyFingerprintRuntimeKey"),
        pydantic.Field(alias="idempotencyFingerprintRuntimeKey"),
    ]
    create_conversation_retry_policy: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilitiesConversationDeliveryCreateConversationRetryPolicy,
        FieldMetadata(alias="createConversationRetryPolicy"),
        pydantic.Field(alias="createConversationRetryPolicy"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
