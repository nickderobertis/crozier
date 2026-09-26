

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.email_address_visibility import EmailAddressVisibility
from .register_queue_response_user_settings_emojiset_choices_item import (
    RegisterQueueResponseUserSettingsEmojisetChoicesItem,
)


class RegisterQueueResponseUserSettings(UniversalBaseModel):
    """
    Present if `user_settings` is present in `fetch_event_types`.

    A dictionary containing the user's personal settings.

    **Changes**: In Zulip 12.0 (feature level 439), removed deprecated,
    duplicate copies of many of these user settings from the top-level object.
    Previously, clients that did not include the `user_settings_object`
    [client capability][client-capabilities] and included `update_display_settings`
    or `update_global_notifications` in `fetch_event_types` would receive those
    user settings that predated feature level 89 in the top-level response.

    In Zulip 10.0 (feature level 364), removed the `dense_mode` setting as we
    now have `web_font_size_px` and `web_line_height_percent` settings for
    more control.

    New in Zulip 5.0 (feature level 89). Previously, user settings appeared
    in the top-level object; see the `user_settings_object`
    [client capability][client-capabilities] for backwards-compatibility.

    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    twenty_four_hour_time: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether time should be [displayed in 24-hour notation](/help/change-the-time-format).
    
    A `null` value indicates that the client should use the default time
    format for the user's locale.
    
    **Changes**: Prior to Zulip 11.0 (feature level 408), `null`
    was not a valid value for this setting. Note that it was not possible
    to actually set the time format to `null` at this feature level.
    """

    web_mark_read_on_scroll_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Whether or not to mark messages as read when the user scrolls through their
    feed.
    
    - 1 - Always
    - 2 - Only in conversation views
    - 3 - Never
    
    **Changes**: New in Zulip 7.0 (feature level 175). Previously, there was no
    way for the user to configure this behavior on the web, and the Zulip web and
    desktop apps behaved like the "Always" setting when marking messages as read.
    """

    web_channel_default_view: typing.Optional[int] = pydantic.Field(default=None)
    """
    Web/desktop app setting controlling the default navigation
    behavior when clicking on a channel link.
    
    - 1 - Top topic in the channel
    - 2 - Channel feed
    - 3 - List of topics
    - 4 - Top unread topic in channel
    
    **Changes**: The "Top unread topic in channel" is new in Zulip 11.0
    (feature level 401).
    
    The "List of topics" option is new in Zulip 11.0 (feature level 383).
    
    New in Zulip 9.0 (feature level 269). Previously, this
    was not configurable, and every user had the "Channel feed" behavior.
    """

    starred_message_counts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether clients should display the [number of starred
    messages](/help/star-a-message#display-the-number-of-starred-messages).
    """

    receives_typing_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user is configured to receive typing notifications from
    other users. The server will only deliver typing notifications events
    to users who for whom this is enabled.
    
    **Changes**: New in Zulip 9.0 (feature level 253). Previously, there were
    only options to disable sending typing notifications.
    """

    web_suggest_update_timezone: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user should be shown an alert, offering to update their
    [profile time zone](/help/change-your-timezone), when the time displayed
    for the profile time zone differs from the current time displayed by the
    time zone configured on their device.
    
    **Changes**: New in Zulip 10.0 (feature level 329).
    """

    fluid_layout_width: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to use the [maximum available screen width](/help/enable-full-width-display)
    for the web app's center panel (message feed, recent conversations) on wide screens.
    """

    high_contrast_mode: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This setting is reserved for use to control variations in Zulip's design
    to help visually impaired users.
    """

    web_font_size_px: typing.Optional[int] = pydantic.Field(default=None)
    """
    User-configured primary `font-size` for the web application, in pixels.
    
    **Changes**: New in Zulip 9.0 (feature level 245). Previously, font size was
    only adjustable via browser zoom. Note that this setting was not fully
    implemented at this feature level.
    """

    web_line_height_percent: typing.Optional[int] = pydantic.Field(default=None)
    """
    User-configured primary `line-height` for the web application, in percent, so a
    value of 120 represents a `line-height` of 1.2.
    
    **Changes**: New in Zulip 9.0 (feature level 245). Previously, line height was
    not user-configurable. Note that this setting was not fully implemented at this
    feature level.
    """

    color_scheme: typing.Optional[int] = pydantic.Field(default=None)
    """
    Controls which [color theme](/help/dark-theme) to use.
    
    - 1 - Automatic
    - 2 - Dark theme
    - 3 - Light theme
    
    Automatic detection is implementing using the standard `prefers-color-scheme`
    media query.
    """

    translate_emoticons: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to [translate emoticons to emoji](/help/configure-emoticon-translations)
    in messages the user sends.
    """

    display_emoji_reaction_users: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to display the names of reacting users on a message.
    
    When enabled, clients should display the names of reacting
    users, rather than a count, for messages with few total
    reactions. The ideal cutoff may depend on the space
    available for displaying reactions; the official web
    application displays names when 3 or fewer total reactions
    are present with this setting enabled.
    
    **Changes**: New in Zulip 6.0 (feature level 125).
    """

    default_language: typing.Optional[str] = pydantic.Field(default=None)
    """
    What [default language](/help/change-your-language) to use for the account.
    
    This controls both the Zulip UI as well as email notifications sent to the user.
    
    The value needs to be a standard language code that the Zulip server has
    translation data for; for example, `"en"` for English or `"de"` for German.
    """

    web_home_view: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [home view](/help/configure-home-view) used when opening a new
    Zulip web app window or hitting the `Esc` keyboard shortcut repeatedly.
    
    - "recent" - Recent conversations view
    - "inbox" - Inbox view
    - "all_messages" - Combined feed view
    
    **Changes**: Before Zulip 12.0 (feature level 454), the Recent
    view had `"recent_topics"` as its string encoding.
    
    New in Zulip 8.0 (feature level 219). Previously, this was
    called `default_view`, which was new in Zulip 4.0 (feature level 42).
    """

    web_escape_navigates_to_home_view: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the escape key navigates to the
    [configured home view](/help/configure-home-view).
    
    **Changes**: New in Zulip 8.0 (feature level 219). Previously, this
    was called `escape_navigates_to_default_view`, which was new in Zulip
    5.0 (feature level 107).
    """

    left_side_userlist: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the users list on left sidebar in narrow windows.
    
    This feature is not heavily used and is likely to be reworked.
    """

    emojiset: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's configured [emoji set](/help/emoji-and-emoticons#use-emoticons),
    used to display emoji to the user everywhere they appear in the UI.
    
    - "google" - Google modern
    - "twitter" - Twitter
    - "text" - Plain text
    """

    demote_inactive_streams: typing.Optional[int] = pydantic.Field(default=None)
    """
    Whether to [hide inactive channels](/help/manage-inactive-channels) in the left sidebar.
    
    - 1 - Automatic
    - 2 - Always
    - 3 - Never
    """

    user_list_style: typing.Optional[int] = pydantic.Field(default=None)
    """
    The style selected by the user for the right sidebar user list.
    
    - 1 - Compact
    - 2 - With status
    - 3 - With avatar and status
    
    **Changes**: New in Zulip 6.0 (feature level 141).
    """

    web_animate_image_previews: typing.Optional[str] = pydantic.Field(default=None)
    """
    Controls how animated images should be played in the message feed in the web/desktop application.
    
    - "always" - Always play the animated images in the message feed.
    - "on_hover" - Play the animated images on hover over them in the message feed.
    - "never" - Never play animated images in the message feed.
    
    **Changes**: New in Zulip 9.0 (feature level 275).
    """

    web_stream_unreads_count_display_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Configuration for which channels should be displayed with a numeric unread count in the left sidebar.
    Channels that do not have an unread count will have a simple dot indicator for whether there are any
    unread messages.
    
    - 1 - All channels
    - 2 - Unmuted channels and topics
    - 3 - No channels
    
    **Changes**: New in Zulip 8.0 (feature level 210).
    """

    hide_ai_features: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Controls whether user wants AI features like topic summarization to
    be hidden in all Zulip clients.
    
    **Changes**: New in Zulip 10.0 (feature level 350).
    """

    web_inbox_show_channel_folders: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines whether [channel folders](/help/channel-folders)
    are used to organize how conversations with unread messages
    are displayed in the web/desktop application's Inbox view.
    
    **Changes**: New in Zulip 12.0 (feature level 431).
    """

    web_left_sidebar_show_channel_folders: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines whether [channel folders](/help/channel-folders)
    are used to organize how channels are displayed in the
    web/desktop application's left sidebar.
    
    **Changes**: New in Zulip 11.0 (feature level 411).
    """

    web_left_sidebar_unreads_count_summary: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines whether the web/desktop application's left sidebar displays
    the unread message count summary.
    
    **Changes**: New in Zulip 11.0 (feature level 398).
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IANA identifier of the user's [profile time zone](/help/change-your-timezone),
    which is used primarily to display the user's local time to other users.
    """

    enter_sends: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user setting for [sending on pressing Enter](/help/configure-send-message-keys)
    in the compose box is enabled.
    """

    enable_drafts_synchronization: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean parameter to control whether synchronizing drafts is enabled for
    the user. When synchronization is disabled, all drafts stored in the server
    will be automatically deleted from the server.
    
    This does not do anything (like sending events) to delete local copies of
    drafts stored in clients.
    """

    enable_stream_desktop_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable visual desktop notifications for channel messages.
    """

    enable_stream_email_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable email notifications for channel messages.
    """

    enable_stream_push_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable mobile notifications for channel messages.
    """

    enable_stream_audible_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable audible desktop notifications for channel messages.
    """

    notification_sound: typing.Optional[str] = pydantic.Field(default=None)
    """
    Notification sound name.
    """

    enable_desktop_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable visual desktop notifications for direct messages and @-mentions.
    """

    enable_sounds: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable audible desktop notifications for direct messages and
    @-mentions.
    """

    enable_followed_topic_desktop_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable visual desktop notifications for messages sent to followed topics.
    
    **Changes**: New in Zulip 8.0 (feature level 189).
    """

    enable_followed_topic_email_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable email notifications for messages sent to followed topics.
    
    **Changes**: New in Zulip 8.0 (feature level 189).
    """

    enable_followed_topic_push_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable push notifications for messages sent to followed topics.
    
    **Changes**: New in Zulip 8.0 (feature level 189).
    """

    enable_followed_topic_audible_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable audible desktop notifications for messages sent to followed topics.
    
    **Changes**: New in Zulip 8.0 (feature level 189).
    """

    email_notifications_batching_period_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    The duration (in seconds) for which the server should wait to batch
    email notifications before sending them.
    """

    enable_offline_email_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable email notifications for direct messages and @-mentions received
    when the user is offline.
    """

    enable_offline_push_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable mobile notification for direct messages and @-mentions received
    when the user is offline.
    """

    enable_online_push_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable mobile notification for direct messages and @-mentions received
    when the user is online.
    """

    enable_digest_emails: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable digest emails when the user is away.
    """

    enable_marketing_emails: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable marketing emails. Has no function outside Zulip Cloud.
    """

    enable_login_emails: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable email notifications for new logins to account.
    """

    message_content_in_email_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include the message's content in email notifications for new messages.
    """

    pm_content_in_desktop_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include content of direct messages in desktop notifications.
    """

    wildcard_mentions_notify: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether wildcard mentions (E.g. @**all**) should send notifications
    like a personal mention.
    """

    enable_followed_topic_wildcard_mentions_notify: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether wildcard mentions (e.g., @**all**) in messages sent to followed topics
    should send notifications like a personal mention.
    
    **Changes**: New in Zulip 8.0 (feature level 189).
    """

    desktop_icon_count_display: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unread count badge (appears in desktop sidebar and browser tab)
    
    - 1 - All unread messages
    - 2 - DMs, mentions, and followed topics
    - 3 - DMs and mentions
    - 4 - None
    
    **Changes**: In Zulip 8.0 (feature level 227), added `DMs, mentions,
    and followed topics` option, renumbering the options to insert it in
    order.
    """

    realm_name_in_email_notifications_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Whether to [include organization name in subject of message notification
    emails](/help/email-notifications#include-organization-name-in-subject-line).
    
    - 1 - Automatic
    - 2 - Always
    - 3 - Never
    
    **Changes**: New in Zulip 7.0 (feature level 168), replacing the
    previous `realm_name_in_notifications` boolean;
    `true` corresponded to `Always`, and `false` to `Never`.
    """

    automatically_follow_topics_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Which [topics to follow automatically](/help/mute-a-topic).
    
    - 1 - Topics the user participates in
    - 2 - Topics the user sends a message to
    - 3 - Topics the user starts
    - 4 - Never
    
    **Changes**: New in Zulip 8.0 (feature level 214).
    """

    automatically_unmute_topics_in_muted_streams_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Which [topics to unmute automatically in muted channels](/help/mute-a-topic).
    
    - 1 - Topics the user participates in
    - 2 - Topics the user sends a message to
    - 3 - Topics the user starts
    - 4 - Never
    
    **Changes**: New in Zulip 8.0 (feature level 214).
    """

    automatically_follow_topics_where_mentioned: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the server will automatically mark the user as following
    topics where the user is mentioned.
    
    **Changes**: New in Zulip 8.0 (feature level 235).
    """

    resolved_topic_notice_auto_read_policy: typing.Optional[str] = pydantic.Field(default=None)
    """
    Controls whether the resolved-topic notices are marked as read.
    
    - "always" - Always mark resolved-topic notices as read.
    - "except_followed" - Mark resolved-topic notices as read in topics not followed by the user.
    - "never" - Never mark resolved-topic notices as read.
    
    **Changes**: New in Zulip 11.0 (feature level 385).
    """

    presence_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Display the presence status to other users when online.
    """

    available_notification_sounds: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Array containing the names of the notification sound options
    supported by this Zulip server. Only relevant to support UI
    for configuring notification sounds.
    """

    emojiset_choices: typing.Optional[typing.List[RegisterQueueResponseUserSettingsEmojisetChoicesItem]] = (
        pydantic.Field(default=None)
    )
    """
    Array of dictionaries where each dictionary describes an emoji set
    supported by this version of the Zulip server.
    
    Only relevant to clients with configuration UI for choosing an emoji set;
    the currently selected emoji set is available in the `emojiset` key.
    
    See [PATCH /settings](/api/update-settings) for details on
    the meaning of this setting.
    """

    send_private_typing_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user has chosen to send [typing
    notifications](/help/typing-notifications)
    when composing direct messages. The client should send typing
    notifications for direct messages if and only if this setting is enabled.
    
    **Changes**: New in Zulip 5.0 (feature level 105).
    """

    send_stream_typing_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user has chosen to send [typing
    notifications](/help/typing-notifications)
    when composing channel messages. The client should send typing
    notifications for channel messages if and only if this setting is enabled.
    
    **Changes**: New in Zulip 5.0 (feature level 105).
    """

    send_read_receipts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether other users are allowed to see whether you've
    read messages.
    
    **Changes**: New in Zulip 5.0 (feature level 105).
    """

    allow_private_data_export: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether organization administrators are allowed to
    export your private data.
    
    **Changes**: New in Zulip 10.0 (feature level 293).
    """

    email_address_visibility: typing.Optional[EmailAddressVisibility] = None
    web_navigate_to_sent_message: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Web/desktop app setting for whether the user's view should
    automatically go to the conversation where they sent a message.
    
    **Changes**: New in Zulip 9.0 (feature level 268). Previously,
    this behavior was not configurable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
