

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_six_op import GetEventsResponseEventsItemSixOp
from .get_events_response_events_item_six_type import GetEventsResponseEventsItemSixType


class GetEventsResponseEventsItemSix(UniversalBaseModel):
    """
    Event sent when another user subscribes to a channel, or their
    subscription is newly visible to the current user.

    When a user subscribes to a channel, the current user will receive this
    event only if they [have permission to see the channel's subscriber
    list](/help/channel-permissions). When the current user gains permission
    to see a given channel's subscriber list, they will receive this event
    for the existing subscriptions to the channel.

    **Changes**: Prior to Zulip 8.0 (feature level 220), this event was
    incorrectly not sent to guest users when subscribers to web-public
    channels and subscribed public channels changed.

    Prior to Zulip 8.0 (feature level 205), this event was not sent when
    a user gained access to a channel due to their [role
    changing](/help/user-roles).

    Prior to Zulip 6.0 (feature level 134), this event was not sent when a
    private channel was made public.

    In Zulip 4.0 (feature level 35), the singular `user_id` and `stream_id`
    integers included in this event were replaced with plural `user_ids` and
    `stream_ids` integer arrays.

    In Zulip 3.0 (feature level 19), the `stream_id` field was added to
    identify the channel the user subscribed to, replacing the `name` field.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSixType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSixOp] = None
    stream_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The IDs of channels that have new or updated subscriber data.
    
    **Changes**: New in Zulip 4.0 (feature level 35), replacing
    the `stream_id` integer.
    """

    user_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The IDs of the users who are newly visible as subscribed to
    the specified channels.
    
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
