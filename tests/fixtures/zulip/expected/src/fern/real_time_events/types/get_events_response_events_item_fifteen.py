

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.basic_channel import BasicChannel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_fifteen_op import GetEventsResponseEventsItemFifteenOp
from .get_events_response_events_item_fifteen_type import GetEventsResponseEventsItemFifteenType


class GetEventsResponseEventsItemFifteen(UniversalBaseModel):
    """
    Event sent when a new channel is created to users who can see
    the new channel exists (for private channels, only subscribers and
    organization administrators will receive this event).

    This event is also sent when a user gains access to a channel they
    previously [could not access](/help/channel-permissions), such as
    when their [role](/help/user-roles) changes, a
    private channel is made public, or a guest user is subscribed
    to a public (or private) channel.

    This event is also sent when a channel is unarchived but only
    to clients that did not declare the `archived_channels` [client
    capability][client-capabilities].

    Note that organization administrators who are not subscribed will
    not be able to see content on the channel; just that it exists.

    **Changes**: Prior to Zulip 11.0 (feature level 378), this
    event was sent to all the users who could see the channel when it
    was unarchived.

    Prior to Zulip 8.0 (feature level 220), this event was incorrectly
    not sent to guest users a web-public channel was created.

    Prior to Zulip 8.0 (feature level 205), this event was not sent
    when a user gained access to a channel due to their role changing.

    Prior to Zulip 8.0 (feature level 192), this event was not sent
    when guest users gained access to a public channel by being
    subscribed.

    Prior to Zulip 6.0 (feature level 134), this event was not sent
    when a private channel was made public.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFifteenType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemFifteenOp] = None
    streams: typing.Optional[typing.List[BasicChannel]] = pydantic.Field(default=None)
    """
    Array of objects, each containing
    details about the newly added channel(s).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
