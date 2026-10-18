

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_to_conference_action_update_params_action_trigger import AddToConferenceActionUpdateParamsActionTrigger
from .add_to_conference_action_update_params_config import AddToConferenceActionUpdateParamsConfig


class AddToConferenceActionUpdateParams(UniversalBaseModel):
    config: typing.Optional[AddToConferenceActionUpdateParamsConfig] = None
    action_trigger: typing.Optional[AddToConferenceActionUpdateParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
