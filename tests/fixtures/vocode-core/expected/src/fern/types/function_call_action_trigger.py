

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_call_action_trigger_config import FunctionCallActionTriggerConfig
from .function_call_action_trigger_type import FunctionCallActionTriggerType


class FunctionCallActionTrigger(UniversalBaseModel):
    type: FunctionCallActionTriggerType
    config: typing.Optional[FunctionCallActionTriggerConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
