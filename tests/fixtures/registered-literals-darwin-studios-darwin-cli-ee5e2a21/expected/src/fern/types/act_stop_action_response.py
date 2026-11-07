

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .act_action_response_available_actions_item import ActActionResponseAvailableActionsItem
from .act_action_response_feedback_request import ActActionResponseFeedbackRequest
from .act_action_response_interaction import ActActionResponseInteraction
from .act_action_response_lifecycle import ActActionResponseLifecycle
from .act_action_response_policy_state import ActActionResponsePolicyState
from .act_action_response_status import ActActionResponseStatus
from .act_stop_action_response_type import ActStopActionResponseType
from .action_outcome import ActionOutcome


class ActStopActionResponse(UniversalBaseModel):
    type: ActStopActionResponseType
    action_id: typing_extensions.Annotated[str, FieldMetadata(alias="actionId"), pydantic.Field(alias="actionId")]
    target_ai_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetAiId"), pydantic.Field(alias="targetAiId")
    ] = None
    capability_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="capabilityId"), pydantic.Field(alias="capabilityId")
    ] = None
    capability_revision: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="capabilityRevision"), pydantic.Field(alias="capabilityRevision")
    ] = None
    revision: int
    lifecycle: ActActionResponseLifecycle
    outcome: typing.Optional[ActionOutcome] = None
    status: ActActionResponseStatus
    result: typing.Dict[str, typing.Any]
    action_required: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="actionRequired"), pydantic.Field(alias="actionRequired")
    ] = None
    available_actions: typing_extensions.Annotated[
        typing.List[ActActionResponseAvailableActionsItem],
        FieldMetadata(alias="availableActions"),
        pydantic.Field(alias="availableActions"),
    ]
    interaction: typing.Optional[ActActionResponseInteraction] = None
    feedback_request: typing_extensions.Annotated[
        typing.Optional[ActActionResponseFeedbackRequest],
        FieldMetadata(alias="feedbackRequest"),
        pydantic.Field(alias="feedbackRequest"),
    ] = None
    policy_state: typing_extensions.Annotated[
        typing.Optional[ActActionResponsePolicyState],
        FieldMetadata(alias="policyState"),
        pydantic.Field(alias="policyState"),
    ] = None
    web_link: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="webLink"), pydantic.Field(alias="webLink")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
