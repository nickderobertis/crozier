

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .events_get_response_data import EventsGetResponseData
from .events_get_response_meta import EventsGetResponseMeta


class EventsGetResponse(UniversalBaseModel):
    success: bool
    data: EventsGetResponseData
    meta: typing.Optional[EventsGetResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
