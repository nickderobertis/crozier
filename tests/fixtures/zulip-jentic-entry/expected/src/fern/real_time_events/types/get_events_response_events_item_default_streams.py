

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_default_streams_type import GetEventsResponseEventsItemDefaultStreamsType


class GetEventsResponseEventsItemDefaultStreams(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when the
    default channels in the organization are changed by an
    organization administrator.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemDefaultStreamsType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    default_streams: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    An array of IDs of all the [default channels](/help/set-default-streams-for-new-users)
    in the organization.
    
    **Changes**: Before Zulip 10.0 (feature level 330),
    we sent array of dictionaries where each dictionary
    contained details about a single default stream for
    the Zulip organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
