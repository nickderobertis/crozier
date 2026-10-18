

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_to_conference_action_update_params_action_trigger import AddToConferenceActionUpdateParamsActionTrigger
from .add_to_conference_action_update_params_config import AddToConferenceActionUpdateParamsConfig
from .dtmf_action_update_params_action_trigger import DtmfActionUpdateParamsActionTrigger
from .dtmf_action_update_params_config import DtmfActionUpdateParamsConfig
from .end_conversation_action_update_params_action_trigger import EndConversationActionUpdateParamsActionTrigger
from .end_conversation_action_update_params_config import EndConversationActionUpdateParamsConfig
from .external_action_update_params_action_trigger import ExternalActionUpdateParamsActionTrigger
from .external_action_update_params_config import ExternalActionUpdateParamsConfig
from .set_hold_action_update_params_action_trigger import SetHoldActionUpdateParamsActionTrigger
from .set_hold_action_update_params_config import SetHoldActionUpdateParamsConfig
from .transfer_call_action_update_params_action_trigger import TransferCallActionUpdateParamsActionTrigger
from .transfer_call_action_update_params_config import TransferCallActionUpdateParamsConfig


class ActionUpdateParamsRequest_ActionAddToConference(UniversalBaseModel):
    type: typing.Literal["action_add_to_conference"] = "action_add_to_conference"
    config: typing.Optional[AddToConferenceActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[AddToConferenceActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionUpdateParamsRequest_ActionDtmf(UniversalBaseModel):
    type: typing.Literal["action_dtmf"] = "action_dtmf"
    config: typing.Optional[DtmfActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[DtmfActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionUpdateParamsRequest_ActionEndConversation(UniversalBaseModel):
    type: typing.Literal["action_end_conversation"] = "action_end_conversation"
    config: typing.Optional[EndConversationActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[EndConversationActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionUpdateParamsRequest_ActionExternal(UniversalBaseModel):
    type: typing.Literal["action_external"] = "action_external"
    config: typing.Optional[ExternalActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[ExternalActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionUpdateParamsRequest_ActionSetHold(UniversalBaseModel):
    type: typing.Literal["action_set_hold"] = "action_set_hold"
    config: typing.Optional[SetHoldActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[SetHoldActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionUpdateParamsRequest_ActionTransferCall(UniversalBaseModel):
    type: typing.Literal["action_transfer_call"] = "action_transfer_call"
    config: typing.Optional[TransferCallActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[TransferCallActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ActionUpdateParamsRequest = typing_extensions.Annotated[
    typing.Union[
        ActionUpdateParamsRequest_ActionAddToConference,
        ActionUpdateParamsRequest_ActionDtmf,
        ActionUpdateParamsRequest_ActionEndConversation,
        ActionUpdateParamsRequest_ActionExternal,
        ActionUpdateParamsRequest_ActionSetHold,
        ActionUpdateParamsRequest_ActionTransferCall,
    ],
    pydantic.Field(discriminator="type"),
]
