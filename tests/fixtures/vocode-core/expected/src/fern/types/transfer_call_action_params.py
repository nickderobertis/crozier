

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_call_action_params_action_trigger import TransferCallActionParamsActionTrigger
from .transfer_call_config import TransferCallConfig


class TransferCallActionParams(UniversalBaseModel):
    config: TransferCallConfig
    action_trigger: typing.Optional[TransferCallActionParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
