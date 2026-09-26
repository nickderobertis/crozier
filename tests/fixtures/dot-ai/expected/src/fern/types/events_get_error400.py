

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .events_get_error400error import EventsGetError400Error
from .events_get_error400meta import EventsGetError400Meta


class EventsGetError400(UniversalBaseModel):
    success: bool
    error: EventsGetError400Error
    meta: typing.Optional[EventsGetError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
