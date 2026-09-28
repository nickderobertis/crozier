

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .events_get_error503error import EventsGetError503Error
from .events_get_error503meta import EventsGetError503Meta


class EventsGetError503(UniversalBaseModel):
    success: bool
    error: EventsGetError503Error
    meta: typing.Optional[EventsGetError503Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
