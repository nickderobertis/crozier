

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_to_conference_action_action_trigger import AddToConferenceActionActionTrigger
from .add_to_conference_config import AddToConferenceConfig


class AddToConferenceAction(UniversalBaseModel):
    id: str
    user_id: str
    config: AddToConferenceConfig
    action_trigger: typing.Optional[AddToConferenceActionActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
