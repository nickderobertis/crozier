

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
from .folder_id import FolderId
from .topics_policy import TopicsPolicy


class BasicChannelBase(UniversalBaseModel):
    """
    Object containing basic details about the channel.
    """

    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique ID of the channel.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the channel.
    """

    is_archived: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating whether the channel is [archived](/help/archive-a-channel).
    
    **Changes**: New in Zulip 10.0 (feature level 315).
    Previously, this endpoint never returned archived channels.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The short description of the channel in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format,
    intended to be used to prepopulate UI for editing a channel's
    description.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
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

    rendered_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The short description of the channel rendered as HTML, intended to
    be used when displaying the channel description in a UI.
    
    One should use the standard Zulip rendered_markdown CSS when
    displaying this content so that emoji, LaTeX, and other syntax
    work correctly. And any client-side security logic for
    user-generated message content should be applied when displaying
    this HTML as though it were the body of a Zulip message.
    """

    is_web_public: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the channel has been configured to allow unauthenticated
    access to its message history from the web.
    
    **Changes**: New in Zulip 2.1.0.
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

    history_public_to_subscribers: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the history of the channel is public to its subscribers.
    
    Currently always true for public channels (i.e. `"invite_only": false` implies
    `"history_public_to_subscribers": true`), but clients should not make that
    assumption, as we may change that behavior in the future.
    """

    topics_policy: typing.Optional[TopicsPolicy] = None
    first_message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the first message in the channel.
    
    Intended to help clients determine whether they need to display
    UI like the "show all topics" widget that would suggest the channel
    has older history that can be accessed.
    
    Is `null` for channels with no message history.
    
    **Changes**: New in Zulip 2.1.0.
    """

    folder_id: typing.Optional[FolderId] = None
    is_recently_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the channel has recent message activity. Clients should use this to implement
    [hide inactive channels](/help/manage-inactive-channels) if
    `demote_inactive_streams` is enabled.
    
    **Changes**: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
    demote_inactive_streams from local message history, resulting in a choppy loading
    experience.
    """

    is_announcement_only: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the given channel is announcement only or not.
    
    **Changes**: Deprecated in Zulip 3.0 (feature level 1). Clients
    should use `stream_post_policy` instead.
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
