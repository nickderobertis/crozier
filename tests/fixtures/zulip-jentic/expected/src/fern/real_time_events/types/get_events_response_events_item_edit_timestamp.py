

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_edit_timestamp_propagate_mode import (
    GetEventsResponseEventsItemEditTimestampPropagateMode,
)
from .get_events_response_events_item_edit_timestamp_topic_links_item import (
    GetEventsResponseEventsItemEditTimestampTopicLinksItem,
)
from .get_events_response_events_item_edit_timestamp_type import GetEventsResponseEventsItemEditTimestampType


class GetEventsResponseEventsItemEditTimestamp(UniversalBaseModel):
    """
    Event sent when a message's content, topic and/or
    channel has been edited or when a message's content
    has a rendering update, such as for an
    [inline URL preview][inline-url-previews].
    Sent to all users who had received the original
    message.

    [inline-url-previews]: https://zulip.readthedocs.io/en/latest/subsystems/sending-messages.html#inline-url-previews

    **Changes**: In Zulip 10.0 (feature level 284), removed the
    `prev_rendered_content_version` field as it is an internal
    server implementation detail not used by any client.
    """

    id: EventIdSchema
    type: GetEventsResponseEventsItemEditTimestampType = pydantic.Field()
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who sent the message.
    
    Will be `null` when event is for a rendering update of the original
    message, such as for an [inline URL preview][inline-url-previews].
    
    **Changes**: Prior to Zulip 5.0 (feature level 114), this field was
    omitted for [inline URL preview][inline-url-previews] updates.
    """

    rendering_only: bool = pydantic.Field()
    """
    Whether the event only updates the rendered content of the message.
    
    This field should be used by clients to determine if the event
    only provides a rendering update to the message content,
    such as for an [inline URL preview][inline-url-previews].
    When `true`, the event does not reflect a user-generated edit
    and does not modify the message history.
    
    **Changes**: New in Zulip 5.0 (feature level 114). Clients can
    correctly identify these rendering update events prior to this
    feature level by checking whether the `user_id` field was omitted.
    """

    message_id: int = pydantic.Field()
    """
    The ID of the message which was edited or updated.
    
    This field should be used to apply content edits to the client's
    cached message history, or to apply rendered content updates.
    
    If the channel or topic was changed, the set of moved messages is
    encoded in the separate `message_ids` field, which is guaranteed
    to include `message_id`.
    """

    message_ids: typing.List[int] = pydantic.Field()
    """
    A sorted list of IDs of messages to which any channel or topic
    changes encoded in this event should be applied.
    
    This list always includes `message_id`, even when there are no
    channel or topic changes to apply.
    
    These messages are guaranteed to have all been previously sent
    to channel `stream_id` with topic `orig_subject`, and have been
    moved to `new_stream_id` with topic `subject` (if those fields
    are present in the event).
    
    Clients processing these events should update all cached message
    history associated with the moved messages (including adjusting
    `unread_msgs` data structures, where the client may not have the
    message itself in its history) to reflect the new channel and
    topic.
    
    Content changes should be applied only to the single message
    indicated by `message_id`.
    
    **Changes**: Before Zulip 11.0 (feature level 393), this list
    was not guaranteed to be sorted.
    """

    flags: typing.List[str] = pydantic.Field()
    """
    The user's personal [message flags][message-flags] for the
    message with ID `message_id` following the edit.
    
    A client application should compare these to the original flags
    to identify cases where a mention or alert word was added by the
    edit.
    
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

    edit_timestamp: int = pydantic.Field()
    """
    The UNIX timestamp when this message edit operation was processed by
    the server, in UTC seconds.
    
    **Changes**: Prior to Zulip 5.0 (feature level 114), this field
    was omitted for [inline URL preview][inline-url-previews] updates.
    """

    stream_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if the message was edited and originally sent to a channel.
    
    The name of the channel that the message was sent to. Clients
    are recommended to use the `stream_id` field instead.
    """

    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Only present if the message was edited and originally sent to a channel.
    
    The pre-edit channel for all of the messages with IDs in
    `message_ids`.
    
    **Changes**: As of Zulip 5.0 (feature level 112), this field
    is present for all edits to a channel message. Previously, it
    was not present when only the content of the channel message was
    edited.
    """

    new_stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Only present if message(s) were moved to a different channel.
    
    The post-edit channel for all of the messages with IDs in
    `message_ids`.
    """

    propagate_mode: typing.Optional[GetEventsResponseEventsItemEditTimestampPropagateMode] = pydantic.Field(
        default=None
    )
    """
    Only present if this event moved messages to a different
    topic and/or channel.
    
    The choice the editing user made about which messages should be
    affected by a channel/topic edit:
    
    - `"change_one"`: Just change the one indicated in `message_id`.
    - `"change_later"`: Change messages in the same topic that had
      been sent after this one.
    - `"change_all"`: Change all messages in that topic.
    
    This parameter should be used to decide whether to change
    navigation and compose box state in response to the edit. For
    example, if the user was previously in topic narrow, and the
    topic was edited with `"change_later"` or `"change_all"`, the Zulip
    web app will automatically navigate to the new topic narrow.
    Similarly, a message being composed to the old topic should
    have its recipient changed to the new topic.
    
    This navigation makes it much more convenient to move content
    between topics without disruption or messages continuing
    to be sent to the pre-edit topic by accident.
    """

    orig_subject: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if this event moved messages to a different
    topic and/or channel.
    
    The pre-edit topic for all of the messages with IDs in
    `message_ids`.
    
    For clients that don't support the `empty_topic_name` [client capability][client-capabilities],
    if the actual pre-edit topic name is empty string, this field's value will instead
    be the value of `realm_empty_topic_display_name` found in the
    [`POST /register`](/api/register-queue) response.
    
    **Changes**: Before 10.0 (feature level 334), `empty_topic_name`
    client capability didn't exist and empty string as the topic name for
    channel messages wasn't allowed.
    
    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    subject: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if this event moved messages to a different topic;
    this field will not be present when moving messages to the same
    topic name in a different channel.
    
    The post-edit topic for all of the messages with IDs in
    `message_ids`.
    
    For clients that don't support the `empty_topic_name` [client capability][client-capabilities],
    if the actual post-edit topic name is empty string, this field's value will instead
    be the value of `realm_empty_topic_display_name` found in the
    [`POST /register`](/api/register-queue) response.
    
    **Changes**: Before 10.0 (feature level 334), `empty_topic_name`
    client capability didn't exist and empty string as the topic name for
    channel messages wasn't allowed.
    
    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    topic_links: typing.Optional[typing.List[GetEventsResponseEventsItemEditTimestampTopicLinksItem]] = pydantic.Field(
        default=None
    )
    """
    Only present if this event moved messages to a different topic;
    this field will not be present when moving messages to the same
    topic name in a different channel.
    
    Data on any links to be included in the `topic`
    line (these are generated by
    [custom linkification filter](/help/add-a-custom-linkifier)
    that match content in the message's topic.), corresponding
    to the post-edit topic.
    
    **Changes**: This field contained a list of urls before
    Zulip 4.0 (feature level 46).
    
    New in Zulip 3.0 (feature level 1). Previously, this field
    was called `subject_links`; clients are recommended to
    rename `subject_links` to `topic_links` if present for
    compatibility with older Zulip servers.
    """

    orig_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if this event changed the message content.
    
    The original content of the message with ID `message_id`
    immediately prior to this edit, in the original [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.
    """

    orig_rendered_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if this event changed the message content.
    
    The original content of the message with ID `message_id`
    immediately prior to this edit, rendered as HTML.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if this event changed the message content or
    updated the message content for an
    [inline URL preview][inline-url-previews].
    
    The new content of the message with ID `message_id`, in the
    original [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.
    """

    rendered_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if this event changed the message content or
    updated the message content for an
    [inline URL preview][inline-url-previews].
    
    The new content of the message with ID `message_id`,
    rendered in HTML.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    """

    is_me_message: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Only present if this event changed the message content.
    
    Whether the message with ID `message_id` is now a
    [/me status message][status-messages].
    
    [status-messages]: /help/format-your-message-using-markdown#status-messages
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
