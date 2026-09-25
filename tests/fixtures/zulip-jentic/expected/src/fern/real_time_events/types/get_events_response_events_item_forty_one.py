

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_forty_one_op import GetEventsResponseEventsItemFortyOneOp
from .get_events_response_events_item_forty_one_operation import GetEventsResponseEventsItemFortyOneOperation
from .get_events_response_events_item_forty_one_type import GetEventsResponseEventsItemFortyOneType


class GetEventsResponseEventsItemFortyOne(UniversalBaseModel):
    """
    Event sent to a user when [message flags][message-flags] are added
    to messages.

    This can reflect a direct user action, or can be the indirect
    consequence of another action. Whatever the cause, if there's a change
    in the set of message flags that the user has for a message, then an
    `update_message_flags` event will be sent with the change. Note
    that this applies when the user already had access to the message, and
    continues to have access to it. When a message newly appears or
    disappears, a [`message`][message-event] or
    [`delete_message`][message-delete] event is sent instead.

    Some examples of actions that trigger an `update_message_flags`
    event:

    - The `"starred"` flag is added when the user chooses to [star a
      message](/help/star-a-message).
    - The `"read"` flag is added when the user marks messages as read by
      scrolling through them, or uses [Mark all messages as read][all-read]
      on a conversation.
    - The `"read"` flag is added when the user [mutes](/help/mute-a-user) a
      message's sender.
    - The `"read"` flag is added after the user unsubscribes from a channel,
      or messages are moved to a not-subscribed channel, provided the user
      can still access the messages at all. Note a
      [`delete_message`][message-delete] event is sent in the case where the
      user can no longer access the messages.

    In some cases, a change in message flags that's caused by another change
    may happen a short while after the original change, rather than
    simultaneously. For example, when messages that were unread are moved to
    a channel where the user is not subscribed, the resulting change in
    message flags (and the corresponding `update_message_flags` event with
    flag `"read"`) may happen later than the message move itself. The delay
    in that example is typically at most a few hundred milliseconds and can
    in rare cases be minutes or longer.

    [message-flags]: /api/update-message-flags#available-flags
    [message-event]: /api/get-events#message
    [message-delete]: /api/get-events#delete_message
    [all-read]: /help/marking-messages-as-read#mark-messages-in-multiple-topics-and-channels-as-read
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFortyOneType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemFortyOneOp] = None
    operation: typing.Optional[GetEventsResponseEventsItemFortyOneOperation] = pydantic.Field(default=None)
    """
    Old name for the `op` field in this event type.
    
    **Deprecated** in Zulip 4.0 (feature level 32), and
    replaced by the `op` field.
    """

    flag: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [flag][message-flags] that was added.
    """

    messages: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array containing the IDs of all messages to which
    the flag was added.
    """

    all_: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="all"),
        pydantic.Field(
            alias="all",
            description='Whether the specified flag was added to all messages.\nThis field is only relevant for the `"read"` flag, and\nwill be `false` for all other flags.\n\nWhen `true` for the `"read"` flag, then the `messages`\narray will be empty.',
        ),
    ] = None
    """
    Whether the specified flag was added to all messages.
    This field is only relevant for the `"read"` flag, and
    will be `false` for all other flags.
    
    When `true` for the `"read"` flag, then the `messages`
    array will be empty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
