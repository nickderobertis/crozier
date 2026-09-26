

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.messages_event import MessagesEvent
from .get_events_response_events_item_local_message_id_type import GetEventsResponseEventsItemLocalMessageIdType


class GetEventsResponseEventsItemLocalMessageId(UniversalBaseModel):
    """
    Event type for messages.

    **Changes**: In Zulip 3.1 (feature level 26), the
    `sender_short_name` field was removed from message
    objects.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemLocalMessageIdType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    message: typing.Optional[MessagesEvent] = None
    flags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The user's [message flags][message-flags] for the message.
    
    Clients should inspect the flags field rather than assuming that
    new messages are unread; [muted users](/api/mute-user), messages
    sent by the current user, and more subtle scenarios can result
    in a new message that the server has already marked as read for
    the user.
    
    **Changes**: In Zulip 8.0 (feature level 224), the `wildcard_mentioned`
    flag was deprecated in favor of the `stream_wildcard_mentioned` and
    `topic_wildcard_mentioned` flags. The `wildcard_mentioned` flag exists
    for backwards compatibility with older clients and equals
    `stream_wildcard_mentioned || topic_wildcard_mentioned`. Clients
    supporting older server versions should treat this field as a previous
    name for the `stream_wildcard_mentioned` flag as topic wildcard mentions
    were not available prior to this feature level.
    
    [message-flags]: /api/update-message-flags#available-flags
    """

    local_message_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    For clients supporting
    [local echo](https://zulip.readthedocs.io/en/latest/subsystems/sending-messages.html#local-echo).
    Only present if [`local_id`](/api/send-message#parameter-local_id) and
    [`queue_id`](/api/send-message#parameter-queue_id) were passed by the
    client when the message was sent to the server.
    
    The same unique string-format identifier chosen by the client to identify
    the locally echoed message (which was the value passed as the `local_id`
    parameter). This lets the client know unambiguously that it should
    replace the locally echoed message, rather than adding this new message
    (which would be correct if the user had sent the new message from another
    device).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
