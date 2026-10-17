

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .empty_action_config import EmptyActionConfig
from .set_hold_action_action_trigger import SetHoldActionActionTrigger


class SetHoldAction(UniversalBaseModel):
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
