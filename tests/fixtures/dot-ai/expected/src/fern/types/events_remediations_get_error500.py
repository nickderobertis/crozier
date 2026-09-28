

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .events_remediations_get_error500error import EventsRemediationsGetError500Error
from .events_remediations_get_error500meta import EventsRemediationsGetError500Meta


class EventsRemediationsGetError500(UniversalBaseModel):
    success: bool
    error: EventsRemediationsGetError500Error
    meta: typing.Optional[EventsRemediationsGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
