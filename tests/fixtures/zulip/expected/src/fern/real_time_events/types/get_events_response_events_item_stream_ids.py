

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_stream_ids_op import GetEventsResponseEventsItemStreamIdsOp
from .get_events_response_events_item_stream_ids_streams_item import GetEventsResponseEventsItemStreamIdsStreamsItem
from .get_events_response_events_item_stream_ids_type import GetEventsResponseEventsItemStreamIdsType


class GetEventsResponseEventsItemStreamIds(UniversalBaseModel):
    """
    Event sent when a user loses access to a channel they previously
    [could access](/help/channel-permissions) because they are
    unsubscribed from a private channel or their [role](/help/user-roles)
    has changed.

    This event is also sent when a channel is archived but only
    to clients that did not declare the `archived_channels` [client
    capability][client-capabilities].

    **Changes**: Prior to Zulip 11.0 (feature level 378), this
    event was sent to all the users who could see the channel when it
    was archived.

    Prior to Zulip 8.0 (feature level 205), this event was not sent
    when a user lost access to a channel due to their role changing.

    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemStreamIdsType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemStreamIdsOp] = None
    streams: typing.Optional[typing.List[GetEventsResponseEventsItemStreamIdsStreamsItem]] = pydantic.Field(
        default=None
    )
    """
    Array of objects, each containing ID of the channel that was deleted.
    
    **Changes**: **Deprecated** in Zulip 10.0 (feature level 343)
    and will be removed in a future release. Previously, these
    objects additionally contained all the standard fields for a
    channel object.
    """

    stream_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array containing the IDs of the channels that were deleted.
    
    **Changes**: New in Zulip 10.0 (feature level 343). Previously,
    these IDs were available only via the legacy `streams` array.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
