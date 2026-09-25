

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.emoji_reaction import EmojiReaction
from .get_message_response_message_display_recipient import GetMessageResponseMessageDisplayRecipient
from .get_message_response_message_edit_history_item import GetMessageResponseMessageEditHistoryItem
from .get_message_response_message_submessages_item import GetMessageResponseMessageSubmessagesItem
from .get_message_response_message_topic_links_item import GetMessageResponseMessageTopicLinksItem


class GetMessageResponseMessage(UniversalBaseModel):
    """
    An object containing details of the message.

    **Changes**: New in Zulip 5.0 (feature level 120).
    """

    avatar_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the message sender's avatar. Can be `null` only if
    the current user has access to the sender's real email address
    and `client_gravatar` was `true`.
    
    If `null`, then the sender has not uploaded an avatar in Zulip,
    and the client can compute the gravatar URL by hashing the
    sender's email address, which corresponds in this case to their
    real email address.
    
    **Changes**: Before Zulip 7.0 (feature level 163), access to a
    user's real email address was a realm-level setting. As of this
    feature level, `email_address_visibility` is a user setting.
    """

    client: typing.Optional[str] = pydantic.Field(default=None)
    """
    A Zulip "client" string, describing what Zulip client
    sent the message.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content/body of the message.
    When `apply_markdown` is set, it will be in HTML format.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    """

    content_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The HTTP `content_type` for the message content. This
    will be `text/html` or `text/x-markdown`, depending on
    whether `apply_markdown` was set.
    
    See the help center article on [message formatting](/help/format-your-message-using-markdown) for details on Zulip-flavored Markdown.
    """

    display_recipient: typing.Optional[GetMessageResponseMessageDisplayRecipient] = pydantic.Field(default=None)
    """
    Data on the recipient of the message. Will be one of the following:
    """

    edit_history: typing.Optional[typing.List[GetMessageResponseMessageEditHistoryItem]] = pydantic.Field(default=None)
    """
    An array of objects, with each object documenting the
    changes in a previous edit made to the message,
    ordered chronologically from most recent to least recent
    edit.
    
    Not present if the message has never been edited or moved,
    or if [viewing message edit history][edit-history-access]
    is not allowed in the organization.
    
    Every object will contain `user_id` and `timestamp`.
    
    The other fields are optional, and will be present or not
    depending on whether the channel, topic, and/or message
    content were modified in the edit event. For example, if
    only the topic was edited, only `prev_topic` and `topic`
    will be present in addition to `user_id` and `timestamp`.
    
    [edit-history-access]: /help/restrict-message-edit-history-access
    
    **Changes**: In Zulip 10.0 (feature level 284), removed the
    `prev_rendered_content_version` field as it is an internal
    server implementation detail not used by any client.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique message ID. Messages should always be
    displayed sorted by ID.
    """

    is_me_message: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the message is a [/me status message][status-messages]
    
    [status-messages]: /help/format-your-message-using-markdown#status-messages
    """

    last_edit_timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for when the message's content was last edited, in
    UTC seconds.
    
    Not present if the message's content has never been edited.
    
    Clients should use this field, rather than parsing the `edit_history`
    array, to display an indicator that the message has been edited.
    
    **Changes**: Prior to Zulip 10.0 (feature level 365), this was the
    time when the message was last edited or moved.
    """

    last_moved_timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for when the message was last moved to a different
    channel or topic, in UTC seconds.
    
    Not present if the message has never been moved, or if the only topic
    moves for the message are [resolving or unresolving](/help/resolve-a-topic)
    the message's topic.
    
    Clients should use this field, rather than parsing the `edit_history`
    array, to display an indicator that the message has been moved.
    
    **Changes**: New in Zulip 10.0 (feature level 365). Previously,
    parsing the `edit_history` array was required in order to correctly
    display moved message indicators.
    """

    reactions: typing.Optional[typing.List[EmojiReaction]] = pydantic.Field(default=None)
    """
    Data on any [reactions](/help/emoji-reactions) to the message,
    ordered chronologically from oldest to newest reaction.
    
    **Changes**: In Zulip 10.0 (feature level 328), the deprecated `user`
    object was removed from the data for each reaction. It contained the
    following information about the user who added the reaction: `id`,
    `email`, `full_name` and `is_mirror_dummy`.
    """

    recipient_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    A unique ID for the set of users receiving the
    message (either a channel or group of users). Useful primarily
    for hashing.
    
    **Changes**: In Zulip 12.0 (feature level 482),
    `recipient_id` in 1:1 direct messages changed to a new
    value; it still has the semantics of "the 1:1 conversation
    with a specific user," but the raw value changed due to
    internal changes.
    
    Before Zulip 10.0 (feature level 327), `recipient_id`
    was the same across all incoming 1:1 direct messages. Now, each
    incoming message uniquely shares a `recipient_id` with outgoing
    messages in the same conversation.
    """

    sender_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Zulip API email address of the message's sender.
    """

    sender_full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full name of the message's sender.
    """

    sender_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The user ID of the message's sender.
    """

    sender_realm_str: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string identifier for the realm the sender is in. Unique only within
    the context of a given Zulip server.
    
    E.g. on `example.zulip.com`, this will be `example`.
    """

    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Only present for channel messages; the ID of the channel.
    """

    subject: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `topic` of the message. Currently always `""` for direct messages,
    though this could change if Zulip adds support for topics in direct
    message conversations.
    
    The field name is a legacy holdover from when topics were
    called "subjects" and will eventually change.
    
    For clients that don't support the `empty_topic_name` [client capability][client-capabilities],
    the empty string value is replaced with the value of `realm_empty_topic_display_name`
    found in the [POST /register](/api/register-queue) response, for channel messages.
    
    **Changes**: Before Zulip 10.0 (feature level 334), `empty_topic_name`
    client capability didn't exist and empty string as the topic name for
    channel messages wasn't allowed.
    
    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    submessages: typing.Optional[typing.List[GetMessageResponseMessageSubmessagesItem]] = pydantic.Field(default=None)
    """
    Data used for certain experimental Zulip integrations.
    """

    timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for when the message was sent,
    in UTC seconds.
    """

    topic_links: typing.Optional[typing.List[GetMessageResponseMessageTopicLinksItem]] = pydantic.Field(default=None)
    """
    Data on any links to be included in the `topic`
    line (these are generated by [custom linkification
    filters](/help/add-a-custom-linkifier) that match content in the
    message's topic.)
    
    **Changes**: This field contained a list of urls before
    Zulip 4.0 (feature level 46).
    
    New in Zulip 3.0 (feature level 1). Previously, this field was called
    `subject_links`; clients are recommended to rename `subject_links` to `topic_links`
    if present for compatibility with older Zulip servers.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the message: `"stream"` or `"private"`.
    """

    flags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The user's [message flags][message-flags] for the message.
    
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
