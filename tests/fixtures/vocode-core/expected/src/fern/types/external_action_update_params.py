

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .external_action_update_params_action_trigger import ExternalActionUpdateParamsActionTrigger
from .external_action_update_params_config import ExternalActionUpdateParamsConfig


class ExternalActionUpdateParams(UniversalBaseModel):
    config: typing.Optional[ExternalActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[ExternalActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
