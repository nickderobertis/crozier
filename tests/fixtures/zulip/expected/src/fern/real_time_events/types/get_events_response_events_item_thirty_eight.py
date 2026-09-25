

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_thirty_eight_message_type import GetEventsResponseEventsItemThirtyEightMessageType
from .get_events_response_events_item_thirty_eight_op import GetEventsResponseEventsItemThirtyEightOp
from .get_events_response_events_item_thirty_eight_recipients_item import (
    GetEventsResponseEventsItemThirtyEightRecipientsItem,
)
from .get_events_response_events_item_thirty_eight_sender import GetEventsResponseEventsItemThirtyEightSender
from .get_events_response_events_item_thirty_eight_type import GetEventsResponseEventsItemThirtyEightType


class GetEventsResponseEventsItemThirtyEight(UniversalBaseModel):
    """
    Event sent when a user starts typing a message.

    Sent to all clients for users who would receive the
    message being typed, with the additional rule that typing
    notifications for channel messages are only sent to clients
    that included `stream_typing_notifications` in their
    [client capabilities][client-capabilities] when registering
    the event queue.

    See [POST /typing](/api/set-typing-status) endpoint for more details.

    **Changes**: Typing notifications for channel messages are new in
    Zulip 4.0 (feature level 58).

    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemThirtyEightType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemThirtyEightOp] = None
    message_type: typing.Optional[GetEventsResponseEventsItemThirtyEightMessageType] = pydantic.Field(default=None)
    """
    Type of message being composed. Must be `"stream"` or `"direct"`.
    
    **Changes**: In Zulip 8.0 (feature level 215), replaced the
    value `"private"` with `"direct"`.
    
    New in Zulip 4.0 (feature level 58). Previously, all typing
    notifications were implicitly direct messages.
    """

    sender: typing.Optional[GetEventsResponseEventsItemThirtyEightSender] = pydantic.Field(default=None)
    """
    Object describing the user who is typing the message.
    """

    recipients: typing.Optional[typing.List[GetEventsResponseEventsItemThirtyEightRecipientsItem]] = pydantic.Field(
        default=None
    )
    """
    Only present if `message_type` is `"direct"`.
    
    Array of dictionaries describing the set of users who would be
    recipients of the message being typed. Each dictionary contains
    details about one of the recipients. The sending user is guaranteed
    to appear among the recipients.
    """

    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Only present if `message_type` is `"stream"`.
    
    The unique ID of the channel to which message is being typed.
    
    **Changes**: New in Zulip 4.0 (feature level 58). Previously,
    typing notifications were only for direct messages.
    """

    topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if `message_type` is `"stream"`.
    
    Topic within the channel where the message is being typed.
    
    For clients that don't support the `empty_topic_name` [client capability][client-capabilities],
    if the actual topic name is empty string, this field's value will instead
    be the value of `realm_empty_topic_display_name` found in the
    [`POST /register`](/api/register-queue) response.
    
    **Changes**: Before 10.0 (feature level 334), `empty_topic_name`
    client capability didn't exist and empty string as the topic name for
    channel messages wasn't allowed.
    
    New in Zulip 4.0 (feature level 58). Previously, typing notifications
    were only for direct messages.
    
    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
