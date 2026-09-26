

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .register_queue_response_unread_msgs_huddles_item import RegisterQueueResponseUnreadMsgsHuddlesItem
from .register_queue_response_unread_msgs_pms_item import RegisterQueueResponseUnreadMsgsPmsItem
from .register_queue_response_unread_msgs_streams_item import RegisterQueueResponseUnreadMsgsStreamsItem


class RegisterQueueResponseUnreadMsgs(UniversalBaseModel):
    """
    Present if `message` and `update_message_flags` are both present in
    `event_types`.

    A set of data structures describing the conversations containing
    the 50000 most recent unread messages the user has received. This will usually
    contain every unread message the user has received, but clients should support
    users with even more unread messages (and not hardcode the number 50000).
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of unread messages to display. This includes one-on-one and group
    direct messages, as well as channel messages that are not [muted](/help/mute-a-topic).
    
    **Changes**: Before Zulip 8.0 (feature level 213), the unmute and follow
    topic features were not handled correctly in calculating this field.
    """

    pms: typing.Optional[typing.List[RegisterQueueResponseUnreadMsgsPmsItem]] = pydantic.Field(default=None)
    """
    An array of objects where each object contains details of unread
    one-on-one direct messages with a specific user.
    
    Note that it is possible for a message that the current user sent
    to the specified user to be marked as unread and thus appear here.
    """

    streams: typing.Optional[typing.List[RegisterQueueResponseUnreadMsgsStreamsItem]] = pydantic.Field(default=None)
    """
    An array of dictionaries where each dictionary contains details of all
    unread messages of a single subscribed channel. This includes muted channels
    and muted topics, even though those messages are excluded from `count`.
    
    **Changes**: Prior to Zulip 5.0 (feature level 90), these objects
    included a `sender_ids` property, which listed the set of IDs of
    users who had sent the unread messages.
    """

    huddles: typing.Optional[typing.List[RegisterQueueResponseUnreadMsgsHuddlesItem]] = pydantic.Field(default=None)
    """
    An array of objects where each object contains details of unread
    group direct messages with a specific group of users.
    """

    mentions: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array containing the IDs of all unread messages in which the user was
    mentioned directly, and unread [non-muted](/help/mute-a-topic) messages
    in which the user was mentioned through a wildcard.
    
    **Changes**: Before Zulip 8.0 (feature level 213), the unmute and follow
    topic features were not handled correctly in calculating this field.
    """

    old_unreads_missing: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this data set was truncated because the user has too many
    unread messages. When truncation occurs, only the most recent
    `MAX_UNREAD_MESSAGES` (currently 50000) messages will be considered
    when forming this response. When `true`, we recommend that clients
    display a warning, as they are likely to produce erroneous results
    until reloaded with the user having fewer than `MAX_UNREAD_MESSAGES`
    unread messages.
    
    **Changes**: New in Zulip 4.0 (feature level 44).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
