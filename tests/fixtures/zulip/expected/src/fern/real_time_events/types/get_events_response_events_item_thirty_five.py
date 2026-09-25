

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_thirty_five_type import GetEventsResponseEventsItemThirtyFiveType


class GetEventsResponseEventsItemThirtyFive(UniversalBaseModel):
    """
    Heartbeat events are sent by the server to avoid
    longpolling connections being affected by networks that
    kill idle HTTP connections.

    Clients do not need to do anything to process these
    events, beyond the common `last_event_id` accounting.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemThirtyFiveType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
