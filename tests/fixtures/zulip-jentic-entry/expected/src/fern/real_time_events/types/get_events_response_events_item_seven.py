

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_seven_op import GetEventsResponseEventsItemSevenOp
from .get_events_response_events_item_seven_type import GetEventsResponseEventsItemSevenType


class GetEventsResponseEventsItemSeven(UniversalBaseModel):
    """
    Event sent to other users when users have been unsubscribed
    from channels. Sent to all users if the channel is public or to only
    the existing subscribers if the channel is private.

    **Changes**: Prior to Zulip 8.0 (feature level 220), this event was
    incorrectly not sent to guest users when subscribers to web-public
    channels and subscribed public channels changed.

    In Zulip 4.0 (feature level 35), the singular `user_id` and
    `stream_id` integers included in this event were replaced
    with plural `user_ids` and `stream_ids` integer arrays.

    In Zulip 3.0 (feature level 19), the `stream_id` field was
    added to identify the channel the user unsubscribed from,
    replacing the `name` field.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSevenType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSevenOp] = None
    stream_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The IDs of the channels from which the users have been
    unsubscribed from.
    
    When a user is deactivated, the server will send this event
    removing the user's subscriptions before the `realm_user` event
    for the user's deactivation.
    
    **Changes**: Before Zulip 12.0 (feature level 428), this event
    was incorrectly not sent when deactivating a user subscribed to
    archived channels. Clients supporting older server versions and
    maintaining peer subscriber data need to remove all channel
    subscriptions for a user when processing the `realm_user` event
    with `op="remove"`.
    
    **Changes**: Before Zulip 10.0 (feature level 377), this event
    was not sent on user deactivation.
    
    **Changes**: New in Zulip 4.0 (feature level 35), replacing
    the `stream_id` integer.
    """

    user_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The IDs of the users who have been unsubscribed.
    
    **Changes**: New in Zulip 4.0 (feature level 35), replacing
    the `user_id` integer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
