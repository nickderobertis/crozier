

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .external_action_config import ExternalActionConfig
from .function_call_action_trigger import FunctionCallActionTrigger


class ExternalActionParams(UniversalBaseModel):
    config: ExternalActionConfig
    action_trigger: typing.Optional[FunctionCallActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
