

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .can_administer_channel_group import CanAdministerChannelGroup
from .can_create_topic_group import CanCreateTopicGroup
from .can_delete_any_message_group import CanDeleteAnyMessageGroup
from .can_delete_own_message_group import CanDeleteOwnMessageGroup
from .can_move_messages_out_of_channel_group import CanMoveMessagesOutOfChannelGroup
from .can_move_messages_within_channel_group import CanMoveMessagesWithinChannelGroup
from .can_remove_subscribers_group import CanRemoveSubscribersGroup
from .can_resolve_topics_group import CanResolveTopicsGroup
from .can_send_message_group import CanSendMessageGroup
from .can_subscribe_group import CanSubscribeGroup
from .channel_can_add_subscribers_group import ChannelCanAddSubscribersGroup
from .default_push_notifications import DefaultPushNotifications
from .folder_id import FolderId
from .topics_policy import TopicsPolicy


class Subscription(UniversalBaseModel):
    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique ID of a channel.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of a channel.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [description](/help/change-the-channel-description) of the channel in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format,
    intended to be used to prepopulate UI for editing a channel's
    description.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    
    See also `rendered_description`.
    """

    rendered_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [description](/help/change-the-channel-description) of the channel rendered as HTML, intended to
    be used when displaying the channel description in a UI.
    
    One should use the standard Zulip rendered_markdown CSS when
    displaying this content so that emoji, LaTeX, and other syntax
    work correctly. And any client-side security logic for
    user-generated message content should be applied when displaying
    this HTML as though it were the body of a Zulip message.
    
    See also `description`.
    """

    date_created: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for when the channel was created, in UTC seconds.
    
    **Changes**: New in Zulip 4.0 (feature level 30).
    """

    creator_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who created this channel.
    
    A `null` value means the channel has no recorded creator, which is often
    because the channel is very old, was created during realm creation or
    because it was created via a data import tool or [management command][management-commands].
    
    **Changes**: New in Zulip 9.0 (feature level 254).
    
    [management-commands]: https://zulip.readthedocs.io/en/latest/production/management-commands.html
    """

    invite_only: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Specifies whether the channel is private or not.
    Only people who have been invited can access a private channel.
    """

    subscribers: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    A list of user IDs of users who are also subscribed
    to a given channel. Included only if `include_subscribers` is `true`.
    """

    partial_subscribers: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    If [`include_subscribers="partial"`](/api/get-subscriptions#parameter-include_subscribers)
    was requested, the server may, at its discretion, send a
    `partial_subscribers` list rather than a `subscribers` list
    for channels with a large number of subscribers.
    
    The `partial_subscribers` list contains an arbitrary
    subset of the channel's subscribers that is guaranteed
    to include all bot user subscribers as well as all
    users who have been active in the last 14 days, but
    otherwise can be chosen arbitrarily by the server.
    
    **Changes**: New in Zulip 11.0 (feature level 412).
    """

    desktop_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether desktop notifications
    are enabled for the given channel.
    
    A `null` value means the value of this setting
    should be inherited from the user-level default
    setting, `enable_stream_desktop_notifications`, for
    this channel.
    """

    email_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether email notifications
    are enabled for the given channel.
    
    A `null` value means the value of this setting
    should be inherited from the user-level default
    setting, `enable_stream_email_notifications`, for
    this channel.
    """

    wildcard_mentions_notify: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether wildcard mentions
    trigger notifications as though they were personal
    mentions in this channel.
    
    A `null` value means the value of this setting
    should be inherited from the user-level default
    setting, wildcard_mentions_notify, for
    this channel.
    """

    push_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether push notifications
    are enabled for the given channel.
    
    A `null` value means the value of this setting
    should be inherited from the user-level default
    setting, `enable_stream_push_notifications`, for
    this channel.
    """

    audible_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether audible notifications
    are enabled for the given channel.
    
    A `null` value means the value of this setting
    should be inherited from the user-level default
    setting, `enable_stream_audible_notifications`, for
    this channel.
    """

    pin_to_top: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the given channel has been pinned
    to the top.
    """

    is_muted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user has muted the channel. Muted channels do
    not count towards your total unread count and do not show
    up in the `Combined feed` view (previously known as `All messages`).
    
    **Changes**: Prior to Zulip 2.1.0, this feature was
    represented by the more confusingly named `in_home_view` (with the
    opposite value, `in_home_view=!is_muted`).
    """

    in_home_view: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Legacy property for if the given channel is muted, with inverted meaning.
    
    **Changes**: Deprecated in Zulip 2.1.0. Clients should use `is_muted`
    where available.
    """

    is_announcement_only: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether only organization administrators can post to the channel.
    
    **Changes**: Deprecated in Zulip 3.0 (feature level 1). Clients
    should use `stream_post_policy` instead.
    """

    is_web_public: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the channel has been configured to allow unauthenticated
    access to its message history from the web.
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's personal color for the channel.
    """

    stream_post_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    A deprecated representation of a superset of the users who
    have permission to post messages to the channel available
    for backwards-compatibility. Clients should use
    `can_send_message_group` instead.
    
    It is an enum with the following possible values, corresponding
    to roles/system groups:
    
    - 1 = Any user can post.
    - 2 = Only administrators can post.
    - 3 = Only [full members][calc-full-member] can post.
    - 4 = Only moderators can post.
    
    **Changes**: Deprecated in Zulip 10.0 (feature level 333) and
    replaced by `can_send_message_group`, which supports finer
    resolution of configurations, resulting in this property being
    inaccurate following that transition.
    
    New in Zulip 3.0 (feature level 1), replacing the previous
    `is_announcement_only` boolean.
    
    [calc-full-member]: /api/roles-and-permissions#determining-if-a-user-is-a-full-member
    """

    message_retention_days: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of days that messages sent to this channel will be stored
    before being automatically deleted by the [message retention
    policy](/help/message-retention-policy). There are two special values:
    
    - `null`, the default, means the channel will inherit the organization
      level setting.
    - `-1` encodes retaining messages in this channel forever.
    
    **Changes**: New in Zulip 3.0 (feature level 17).
    """

    default_push_notifications: typing.Optional[DefaultPushNotifications] = None
    history_public_to_subscribers: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the history of the channel is public to its subscribers.
    
    Currently always true for public channels (i.e. `"invite_only": false` implies
    `"history_public_to_subscribers": true`), but clients should not make that
    assumption, as we may change that behavior in the future.
    """

    first_message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the first message in the channel.
    
    Intended to help clients determine whether they need to display
    UI like the "show all topics" widget that would suggest the channel
    has older history that can be accessed.
    
    Is `null` for channels with no message history.
    """

    folder_id: typing.Optional[FolderId] = None
    topics_policy: typing.Optional[TopicsPolicy] = None
    is_recently_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the channel has recent message activity. Clients should use this to implement
    [hiding inactive channels](/help/manage-inactive-channels).
    
    **Changes**: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
    demote_inactive_streams from local message history, resulting in a choppy loading
    experience.
    """

    stream_weekly_traffic: typing.Optional[int] = pydantic.Field(default=None)
    """
    The average number of messages sent to the channel per week, as
    estimated based on recent weeks, rounded to the nearest integer.
    
    If `null`, the channel was recently created and there is
    insufficient data to estimate the average traffic.
    """

    can_add_subscribers_group: typing.Optional[ChannelCanAddSubscribersGroup] = None
    can_remove_subscribers_group: typing.Optional[CanRemoveSubscribersGroup] = None
    can_administer_channel_group: typing.Optional[CanAdministerChannelGroup] = None
    can_delete_any_message_group: typing.Optional[CanDeleteAnyMessageGroup] = None
    can_delete_own_message_group: typing.Optional[CanDeleteOwnMessageGroup] = None
    can_move_messages_out_of_channel_group: typing.Optional[CanMoveMessagesOutOfChannelGroup] = None
    can_move_messages_within_channel_group: typing.Optional[CanMoveMessagesWithinChannelGroup] = None
    can_send_message_group: typing.Optional[CanSendMessageGroup] = None
    can_subscribe_group: typing.Optional[CanSubscribeGroup] = None
    can_resolve_topics_group: typing.Optional[CanResolveTopicsGroup] = None
    can_create_topic_group: typing.Optional[CanCreateTopicGroup] = None
    is_archived: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating whether the channel is [archived](/help/archive-a-channel).
    
    **Changes**: New in Zulip 10.0 (feature level 315).
    Previously, subscriptions only included active
    channels. Note that some endpoints will never return archived
    channels unless the client declares explicit support for
    them via the `archived_channels` client capability.
    """

    subscriber_count: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total number of non-deactivated users (including bots) who
    are subscribed to the channel. Clients are responsible for updating
    this value using `peer_add` and `peer_remove` events.
    
    The server's internals cannot guarantee this value is correctly
    synced with `peer_add` and `peer_remove` events for the channel. As
    a result, if a (rare) race occurs between a change in the channel's
    subscribers and fetching this value, it is possible for a client
    that is correctly following the events protocol to end up with a
    permanently off-by-one error in the channel's subscriber count.
    
    Clients are recommended to fetch full subscriber data for a channel
    in contexts where it is important to avoid this risk. The official
    web application, for example, uses this field primarily while
    waiting to fetch a given channel's full subscriber list from the
    server.
    
    **Changes**: New in Zulip 11.0 (feature level 394).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
