

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .act_list_response_actions_item_attention_state import ActListResponseActionsItemAttentionState
from .act_list_response_actions_item_available_actions_item import ActListResponseActionsItemAvailableActionsItem
from .act_list_response_actions_item_lifecycle import ActListResponseActionsItemLifecycle
from .act_list_response_actions_item_mode import ActListResponseActionsItemMode
from .action_outcome import ActionOutcome


class ActListResponseActionsItem(UniversalBaseModel):
    action_id: typing_extensions.Annotated[str, FieldMetadata(alias="actionId"), pydantic.Field(alias="actionId")]
    ai_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="aiId"), pydantic.Field(alias="aiId")
    ] = None
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
    lifecycle: ActListResponseActionsItemLifecycle
    outcome: typing.Optional[ActionOutcome] = None
    title: str
    intent: str
    mode: ActListResponseActionsItemMode
    lifecycle_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="lifecycleStatus"), pydantic.Field(alias="lifecycleStatus")
    ]
    attention_state: typing_extensions.Annotated[
        ActListResponseActionsItemAttentionState,
        FieldMetadata(alias="attentionState"),
        pydantic.Field(alias="attentionState"),
    ]
    capability_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="capabilityIds"), pydantic.Field(alias="capabilityIds")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    available_actions: typing_extensions.Annotated[
        typing.List[ActListResponseActionsItemAvailableActionsItem],
        FieldMetadata(alias="availableActions"),
        pydantic.Field(alias="availableActions"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
