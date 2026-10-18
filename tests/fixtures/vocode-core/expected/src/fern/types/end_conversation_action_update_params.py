

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .end_conversation_action_update_params_action_trigger import EndConversationActionUpdateParamsActionTrigger
from .end_conversation_action_update_params_config import EndConversationActionUpdateParamsConfig


class EndConversationActionUpdateParams(UniversalBaseModel):
    config: typing.Optional[EndConversationActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[EndConversationActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
