

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_call_action_update_params_action_trigger import TransferCallActionUpdateParamsActionTrigger
from .transfer_call_action_update_params_config import TransferCallActionUpdateParamsConfig


class TransferCallActionUpdateParams(UniversalBaseModel):
    config: typing.Optional[TransferCallActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[TransferCallActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
