

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .events_get_error500error import EventsGetError500Error
from .events_get_error500meta import EventsGetError500Meta


class EventsGetError500(UniversalBaseModel):
    success: bool
    error: EventsGetError500Error
    meta: typing.Optional[EventsGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
