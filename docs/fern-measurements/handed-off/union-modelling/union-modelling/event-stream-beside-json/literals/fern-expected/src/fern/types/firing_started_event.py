

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .firing import Firing
from .firing_started_event_type import FiringStartedEventType


class FiringStartedEvent(UniversalBaseModel):
    type: FiringStartedEventType = pydantic.Field()
    """
    Always `firing.started`.
    """

    firing: Firing

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
