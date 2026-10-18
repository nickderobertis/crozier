

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_to_conference_action_params_action_trigger import AddToConferenceActionParamsActionTrigger
from .add_to_conference_config import AddToConferenceConfig


class AddToConferenceActionParams(UniversalBaseModel):
    config: AddToConferenceConfig
    action_trigger: typing.Optional[AddToConferenceActionParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
