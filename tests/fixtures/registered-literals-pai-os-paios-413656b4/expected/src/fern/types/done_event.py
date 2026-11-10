

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .done_event_data import DoneEventData
from .done_event_event import DoneEventEvent


class DoneEvent(UniversalBaseModel):
    """
    Occurs when a stream ends.
    """

    event: DoneEventEvent
    data: DoneEventData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
