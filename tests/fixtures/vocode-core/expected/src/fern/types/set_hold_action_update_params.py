

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .set_hold_action_update_params_action_trigger import SetHoldActionUpdateParamsActionTrigger
from .set_hold_action_update_params_config import SetHoldActionUpdateParamsConfig


class SetHoldActionUpdateParams(UniversalBaseModel):
    config: typing.Optional[SetHoldActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[SetHoldActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
