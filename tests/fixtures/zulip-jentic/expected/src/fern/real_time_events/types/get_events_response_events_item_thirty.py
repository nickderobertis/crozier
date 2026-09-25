

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_thirty_message_type import GetEventsResponseEventsItemThirtyMessageType
from .get_events_response_events_item_thirty_type import GetEventsResponseEventsItemThirtyType


class GetEventsResponseEventsItemThirty(UniversalBaseModel):
    """
    Event sent when a message has been deleted.

    Sent to all users who currently are subscribed to the messages'
    recipient. May also be sent to additional users who had access to
    the deleted message, including, in particular, an administrator user
    deleting messages in a channel that they are not subscribed to, but
    have content access to. Clients can thus reliably remove the
    messages from whatever view the administrator was using to delete
    them.

    Clients will receive an event of this type for message deletions
    that the client itself initiated if and only if the user previously
    had access to the deleted messages. (Some moderation actions, such
    as deleting all messages sent by a user, allow deleting DMs or
    private channel messages that the acting user cannot themselves
    access. The user will not receive deletion events for such
    inaccessible messages).

    This event is also sent when the user loses access to a message,
    such as when it is [moved to a channel][message-move-channel] that
    the user does not [have permission to access][channel-access].

    **Changes**: Before Zulip 12.0 (feature level 457), an
    administrator who initiated the deletion of messages that they did
    not have permission to access could theoretically receive this event
    for inaccessible messages. However, no Zulip feature actually
    generated events of that type.

    Prior to Zulip 12.0 (feature level 452) messages deleted via a
    message retention policy incorrectly failed to generate
    `delete_message` events.

    Before Zulip 9.0 (feature level 274), this event was only sent to
    subscribers of the message's recipient.

    Before Zulip 5.0 (feature level 77), events
    for direct messages contained additional `sender_id` and
    `recipient_id` fields.

    [message-move-channel]: /help/move-content-to-another-channel
    [channel-access]: /help/channel-permissions
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemThirtyType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    message_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Only present for clients that support the `bulk_message_deletion`
    [client capability][client-capabilities].
    
    A sorted list containing the IDs of the newly deleted messages.
    
    **Changes**: Before Zulip 11.0 (feature level 393), this list was
    not guaranteed to be sorted.
    
    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Only present for clients that do not support the `bulk_message_deletion`
    [client capability][client-capabilities].
    
    The ID of the newly deleted message.
    
    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    message_type: typing.Optional[GetEventsResponseEventsItemThirtyMessageType] = pydantic.Field(default=None)
    """
    The type of message. Either `"stream"` or `"private"`.
    """

    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Only present if `message_type` is `"stream"`.
    
    The ID of the channel to which the message was sent.
    """

    topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if `message_type` is `"stream"`.
    
    The topic to which the message was sent.
    
    For clients that don't support the `empty_topic_name` [client capability][client-capabilities],
    if the actual topic name was empty string, this field's value will instead
    be the value of `realm_empty_topic_display_name` found in the
    [`POST /register`](/api/register-queue) response.
    
    **Changes**: Before 10.0 (feature level 334), `empty_topic_name`
    client capability didn't exist and empty string as the topic name for
    channel messages wasn't allowed.
    
    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
