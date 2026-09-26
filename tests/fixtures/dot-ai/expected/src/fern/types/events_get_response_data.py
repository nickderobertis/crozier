

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .events_get_response_data_events_item import EventsGetResponseDataEventsItem


class EventsGetResponseData(UniversalBaseModel):
    events: typing.List[EventsGetResponseDataEventsItem] = pydantic.Field()
    """
    List of events
    """

    count: float = pydantic.Field()
    """
    Number of events returned
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
