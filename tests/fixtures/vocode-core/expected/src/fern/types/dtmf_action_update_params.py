

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dtmf_action_update_params_action_trigger import DtmfActionUpdateParamsActionTrigger
from .dtmf_action_update_params_config import DtmfActionUpdateParamsConfig


class DtmfActionUpdateParams(UniversalBaseModel):
    config: typing.Optional[DtmfActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[DtmfActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
