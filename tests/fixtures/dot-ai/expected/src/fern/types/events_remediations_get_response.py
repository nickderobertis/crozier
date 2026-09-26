

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .events_remediations_get_response_data import EventsRemediationsGetResponseData
from .events_remediations_get_response_event import EventsRemediationsGetResponseEvent


class EventsRemediationsGetResponse(UniversalBaseModel):
    """
    SSE event for remediation session changes (Content-Type: text/event-stream)
    """

    event: EventsRemediationsGetResponseEvent = pydantic.Field()
    """
    SSE event type
    """

    data: EventsRemediationsGetResponseData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
