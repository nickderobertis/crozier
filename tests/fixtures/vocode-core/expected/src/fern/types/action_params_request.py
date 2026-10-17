

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_to_conference_action_params_action_trigger import AddToConferenceActionParamsActionTrigger
from .add_to_conference_config import AddToConferenceConfig
from .empty_action_config import EmptyActionConfig
from .end_conversation_action_params_action_trigger import EndConversationActionParamsActionTrigger
from .external_action_config import ExternalActionConfig
from .function_call_action_trigger import FunctionCallActionTrigger
from .set_hold_action_params_action_trigger import SetHoldActionParamsActionTrigger
from .transfer_call_action_params_action_trigger import TransferCallActionParamsActionTrigger
from .transfer_call_config import TransferCallConfig


class ActionParamsRequest_ActionAddToConference(UniversalBaseModel):
    type: typing.Literal["action_add_to_conference"] = "action_add_to_conference"
    config: AddToConferenceConfig
    action_trigger: typing.Optional[AddToConferenceActionParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionParamsRequest_ActionDtmf(UniversalBaseModel):
    type: typing.Literal["action_dtmf"] = "action_dtmf"
    config: typing.Optional[EmptyActionConfig] = None
    action_trigger: typing.Optional[FunctionCallActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionParamsRequest_ActionEndConversation(UniversalBaseModel):
    type: typing.Literal["action_end_conversation"] = "action_end_conversation"
    config: typing.Optional[EmptyActionConfig] = None
    action_trigger: typing.Optional[EndConversationActionParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionParamsRequest_ActionExternal(UniversalBaseModel):
    type: typing.Literal["action_external"] = "action_external"
    config: ExternalActionConfig
    action_trigger: typing.Optional[FunctionCallActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionParamsRequest_ActionSetHold(UniversalBaseModel):
    type: typing.Literal["action_set_hold"] = "action_set_hold"
    config: typing.Optional[EmptyActionConfig] = None
    action_trigger: typing.Optional[SetHoldActionParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionParamsRequest_ActionTransferCall(UniversalBaseModel):
    type: typing.Literal["action_transfer_call"] = "action_transfer_call"
    config: TransferCallConfig
    action_trigger: typing.Optional[TransferCallActionParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ActionParamsRequest = typing_extensions.Annotated[
    typing.Union[
        ActionParamsRequest_ActionAddToConference,
        ActionParamsRequest_ActionDtmf,
        ActionParamsRequest_ActionEndConversation,
        ActionParamsRequest_ActionExternal,
        ActionParamsRequest_ActionSetHold,
        ActionParamsRequest_ActionTransferCall,
    ],
    pydantic.Field(discriminator="type"),
]
