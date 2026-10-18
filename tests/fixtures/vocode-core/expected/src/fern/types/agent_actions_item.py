

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_to_conference_action_action_trigger import AddToConferenceActionActionTrigger
from .add_to_conference_config import AddToConferenceConfig
from .empty_action_config import EmptyActionConfig
from .end_conversation_action_action_trigger import EndConversationActionActionTrigger
from .external_action_config import ExternalActionConfig
from .function_call_action_trigger import FunctionCallActionTrigger
from .set_hold_action_action_trigger import SetHoldActionActionTrigger
from .transfer_call_action_action_trigger import TransferCallActionActionTrigger
from .transfer_call_config import TransferCallConfig


class AgentActionsItem_ActionAddToConference(UniversalBaseModel):
    type: typing.Literal["action_add_to_conference"] = "action_add_to_conference"
    id: str
    user_id: str
    config: AddToConferenceConfig
    action_trigger: typing.Optional[AddToConferenceActionActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentActionsItem_ActionDtmf(UniversalBaseModel):
    type: typing.Literal["action_dtmf"] = "action_dtmf"
    id: str
    user_id: str
    config: typing.Optional[EmptyActionConfig] = None
    action_trigger: typing.Optional[FunctionCallActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentActionsItem_ActionEndConversation(UniversalBaseModel):
    type: typing.Literal["action_end_conversation"] = "action_end_conversation"
    id: str
    user_id: str
    config: typing.Optional[EmptyActionConfig] = None
    action_trigger: typing.Optional[EndConversationActionActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentActionsItem_ActionExternal(UniversalBaseModel):
    type: typing.Literal["action_external"] = "action_external"
    id: str
    user_id: str
    config: ExternalActionConfig
    action_trigger: typing.Optional[FunctionCallActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentActionsItem_ActionSetHold(UniversalBaseModel):
    type: typing.Literal["action_set_hold"] = "action_set_hold"
    id: str
    user_id: str
    config: typing.Optional[EmptyActionConfig] = None
    action_trigger: typing.Optional[SetHoldActionActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentActionsItem_ActionTransferCall(UniversalBaseModel):
    type: typing.Literal["action_transfer_call"] = "action_transfer_call"
    id: str
    user_id: str
    config: TransferCallConfig
    action_trigger: typing.Optional[TransferCallActionActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AgentActionsItem = typing_extensions.Annotated[
    typing.Union[
        AgentActionsItem_ActionAddToConference,
        AgentActionsItem_ActionDtmf,
        AgentActionsItem_ActionEndConversation,
        AgentActionsItem_ActionExternal,
        AgentActionsItem_ActionSetHold,
        AgentActionsItem_ActionTransferCall,
    ],
    pydantic.Field(discriminator="type"),
]
