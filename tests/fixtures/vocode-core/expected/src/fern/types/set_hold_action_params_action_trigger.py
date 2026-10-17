

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_call_action_trigger_config import FunctionCallActionTriggerConfig
from .phrase_based_action_trigger_config import PhraseBasedActionTriggerConfig


class SetHoldActionParamsActionTrigger_ActionTriggerFunctionCall(UniversalBaseModel):
    type: typing.Literal["action_trigger_function_call"] = "action_trigger_function_call"
    config: typing.Optional[FunctionCallActionTriggerConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SetHoldActionParamsActionTrigger_ActionTriggerPhraseBased(UniversalBaseModel):
    type: typing.Literal["action_trigger_phrase_based"] = "action_trigger_phrase_based"
    config: PhraseBasedActionTriggerConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SetHoldActionParamsActionTrigger = typing_extensions.Annotated[
    typing.Union[
        SetHoldActionParamsActionTrigger_ActionTriggerFunctionCall,
        SetHoldActionParamsActionTrigger_ActionTriggerPhraseBased,
    ],
    pydantic.Field(discriminator="type"),
]
