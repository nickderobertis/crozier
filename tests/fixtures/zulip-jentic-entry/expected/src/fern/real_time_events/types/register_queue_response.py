

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.basic_channel import BasicChannel
from ...types.bot import Bot
from ...types.channel_folder import ChannelFolder
from ...types.custom_profile_field import CustomProfileField
from ...types.default_channel_group import DefaultChannelGroup
from ...types.draft import Draft
from ...types.navigation_view import NavigationView
from ...types.onboarding_step import OnboardingStep
from ...types.realm_authentication_method import RealmAuthenticationMethod
from ...types.realm_domain import RealmDomain
from ...types.realm_emoji import RealmEmoji
from ...types.realm_playground import RealmPlayground
from ...types.saved_snippet import SavedSnippet
from ...types.scheduled_message import ScheduledMessage
from ...types.subscription import Subscription
from ...types.user import User
from ...types.user_group import UserGroup
from .register_queue_response_cross_realm_bots_item import RegisterQueueResponseCrossRealmBotsItem
from .register_queue_response_custom_profile_field_types_value import RegisterQueueResponseCustomProfileFieldTypesValue
from .register_queue_response_devices_value import RegisterQueueResponseDevicesValue
from .register_queue_response_gif_rating_policy_options_value import RegisterQueueResponseGifRatingPolicyOptionsValue
from .register_queue_response_muted_topics_item_item import RegisterQueueResponseMutedTopicsItemItem
from .register_queue_response_muted_users_item import RegisterQueueResponseMutedUsersItem
from .register_queue_response_never_subscribed_item import RegisterQueueResponseNeverSubscribedItem
from .register_queue_response_presences_value import RegisterQueueResponsePresencesValue
from .register_queue_response_realm_available_video_chat_providers_value import (
    RegisterQueueResponseRealmAvailableVideoChatProvidersValue,
)
from .register_queue_response_realm_billing import RegisterQueueResponseRealmBilling
from .register_queue_response_realm_can_access_all_users_group import RegisterQueueResponseRealmCanAccessAllUsersGroup
from .register_queue_response_realm_can_add_custom_emoji_group import RegisterQueueResponseRealmCanAddCustomEmojiGroup
from .register_queue_response_realm_can_add_subscribers_group import RegisterQueueResponseRealmCanAddSubscribersGroup
from .register_queue_response_realm_can_create_bots_group import RegisterQueueResponseRealmCanCreateBotsGroup
from .register_queue_response_realm_can_create_groups import RegisterQueueResponseRealmCanCreateGroups
from .register_queue_response_realm_can_create_private_channel_group import (
    RegisterQueueResponseRealmCanCreatePrivateChannelGroup,
)
from .register_queue_response_realm_can_create_public_channel_group import (
    RegisterQueueResponseRealmCanCreatePublicChannelGroup,
)
from .register_queue_response_realm_can_create_web_public_channel_group import (
    RegisterQueueResponseRealmCanCreateWebPublicChannelGroup,
)
from .register_queue_response_realm_can_create_write_only_bots_group import (
    RegisterQueueResponseRealmCanCreateWriteOnlyBotsGroup,
)
from .register_queue_response_realm_can_delete_any_message_group import (
    RegisterQueueResponseRealmCanDeleteAnyMessageGroup,
)
from .register_queue_response_realm_can_delete_own_message_group import (
    RegisterQueueResponseRealmCanDeleteOwnMessageGroup,
)
from .register_queue_response_realm_can_invite_users_group import RegisterQueueResponseRealmCanInviteUsersGroup
from .register_queue_response_realm_can_manage_all_groups import RegisterQueueResponseRealmCanManageAllGroups
from .register_queue_response_realm_can_manage_billing_group import RegisterQueueResponseRealmCanManageBillingGroup
from .register_queue_response_realm_can_mention_many_users_group import (
    RegisterQueueResponseRealmCanMentionManyUsersGroup,
)
from .register_queue_response_realm_can_move_messages_between_channels_group import (
    RegisterQueueResponseRealmCanMoveMessagesBetweenChannelsGroup,
)
from .register_queue_response_realm_can_move_messages_between_topics_group import (
    RegisterQueueResponseRealmCanMoveMessagesBetweenTopicsGroup,
)
from .register_queue_response_realm_can_resolve_topics_group import RegisterQueueResponseRealmCanResolveTopicsGroup
from .register_queue_response_realm_can_set_delete_message_policy_group import (
    RegisterQueueResponseRealmCanSetDeleteMessagePolicyGroup,
)
from .register_queue_response_realm_can_set_topics_policy_group import RegisterQueueResponseRealmCanSetTopicsPolicyGroup
from .register_queue_response_realm_can_summarize_topics_group import RegisterQueueResponseRealmCanSummarizeTopicsGroup
from .register_queue_response_realm_create_multiuse_invite_group import (
    RegisterQueueResponseRealmCreateMultiuseInviteGroup,
)
from .register_queue_response_realm_default_external_accounts_value import (
    RegisterQueueResponseRealmDefaultExternalAccountsValue,
)
from .register_queue_response_realm_direct_message_initiator_group import (
    RegisterQueueResponseRealmDirectMessageInitiatorGroup,
)
from .register_queue_response_realm_direct_message_permission_group import (
    RegisterQueueResponseRealmDirectMessagePermissionGroup,
)
from .register_queue_response_realm_embedded_bots_item import RegisterQueueResponseRealmEmbeddedBotsItem
from .register_queue_response_realm_filters_item_item import RegisterQueueResponseRealmFiltersItemItem
from .register_queue_response_realm_incoming_webhook_bots_item import RegisterQueueResponseRealmIncomingWebhookBotsItem
from .register_queue_response_realm_linkifiers_item import RegisterQueueResponseRealmLinkifiersItem
from .register_queue_response_realm_topics_policy import RegisterQueueResponseRealmTopicsPolicy
from .register_queue_response_realm_user_settings_defaults import RegisterQueueResponseRealmUserSettingsDefaults
from .register_queue_response_realm_workplace_users_group import RegisterQueueResponseRealmWorkplaceUsersGroup
from .register_queue_response_recent_private_conversations_item import (
    RegisterQueueResponseRecentPrivateConversationsItem,
)
from .register_queue_response_server_report_message_types_item import RegisterQueueResponseServerReportMessageTypesItem
from .register_queue_response_server_supported_permission_settings import (
    RegisterQueueResponseServerSupportedPermissionSettings,
)
from .register_queue_response_server_thumbnail_formats_item import RegisterQueueResponseServerThumbnailFormatsItem
from .register_queue_response_unread_msgs import RegisterQueueResponseUnreadMsgs
from .register_queue_response_user_settings import RegisterQueueResponseUserSettings
from .register_queue_response_user_status_value import RegisterQueueResponseUserStatusValue
from .register_queue_response_user_topics_item import RegisterQueueResponseUserTopicsItem


class RegisterQueueResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    queue_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the queue that has been allocated for your client.
    
    Will be `null` only for unauthenticated access in realms that have
    enabled the [public access option](/help/public-access-option).
    """

    last_event_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The initial value of `last_event_id` to pass to `GET /api/v1/events`.
    """

    zulip_feature_level: typing.Optional[int] = pydantic.Field(default=None)
    """
    The server's current [Zulip feature level](/api/changelog).
    
    **Changes**: As of Zulip 3.0 (feature level 3), this is always present
    in the endpoint's response. Previously, it was only present if
    `event_types` included `zulip_version`.
    
    New in Zulip 3.0 (feature level 1).
    """

    zulip_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The server's version number. This is often a release version number,
    like `2.1.7`. But for a server running a [version from Git][git-release],
    it will be a Git reference to the commit, like `5.0-dev-1650-gc3fd37755f`.
    
    **Changes**: As of Zulip 3.0 (feature level 3), this is always present
    in the endpoint's response. Previously, it was only present if
    `event_types` included `zulip_version`.
    
    [git-release]: https://zulip.readthedocs.io/en/latest/overview/release-lifecycle.html#git-versions
    """

    zulip_merge_base: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `git merge-base` between `zulip_version` and official branches
    in the public
    [Zulip server and web app repository](https://github.com/zulip/zulip),
    in the same format as `zulip_version`. This will equal
    `zulip_version` if the server is not running a fork of the Zulip server.
    
    This will be `""` if the server does not know its `merge-base`.
    
    **Changes**: New in Zulip 5.0 (feature level 88).
    """

    alert_words: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Present if `alert_words` is present in `fetch_event_types`.
    
    An array of strings, each an [alert word](/help/dm-mention-alert-notifications#alert-words)
    that the current user has configured.
    """

    custom_profile_fields: typing.Optional[typing.List[CustomProfileField]] = pydantic.Field(default=None)
    """
    Present if `custom_profile_fields` is present in `fetch_event_types`.
    
    An array of dictionaries where each dictionary contains the
    details of a single custom profile field that is available to users
    in this Zulip organization. This must be combined with the custom profile
    field values on individual user objects to display users' profiles.
    """

    custom_profile_field_types: typing.Optional[typing.Dict[str, RegisterQueueResponseCustomProfileFieldTypesValue]] = (
        pydantic.Field(default=None)
    )
    """
    Present if `custom_profile_fields` is present in `fetch_event_types`.
    
    An array of objects; each object describes a type of custom profile field
    that could be configured on this Zulip server. Each custom profile type
    has an ID and the `type` property of a custom profile field is equal
    to one of these IDs.
    
    This attribute is only useful for clients containing UI for changing
    the set of configured custom profile fields in a Zulip organization.
    """

    realm_date_created: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The UNIX timestamp (UTC) for when the organization was
    created.
    
    **Changes**: New in Zulip 8.0 (feature level 203).
    """

    demo_organization_scheduled_deletion_date: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`,
    and the realm is a demo organization.
    
    The UNIX timestamp (UTC) when the demo organization will be
    automatically deleted. Clients should use this to display a
    prominent warning to the user that the organization will be
    deleted at the indicated time.
    
    **Changes**: New in Zulip 5.0 (feature level 94).
    """

    drafts: typing.Optional[typing.List[Draft]] = pydantic.Field(default=None)
    """
    An array containing draft objects for the user. These drafts are being
    stored on the backend for the purpose of syncing across devices. This
    array will be empty if `enable_drafts_synchronization` is set to `false`.
    """

    onboarding_steps: typing.Optional[typing.List[OnboardingStep]] = pydantic.Field(default=None)
    """
    Present if `onboarding_steps` is present in `fetch_event_types`.
    
    An array of dictionaries, where each dictionary contains details about
    a single onboarding step that should be shown to the user.
    
    We expect that only official Zulip clients will interact with this data.
    
    **Changes**: Before Zulip 8.0 (feature level 233), this array was named
    `hotspots`. Prior to this feature level, one-time notice onboarding
    steps were not supported, and the `type` field in these objects did not
    exist as all onboarding steps were implicitly hotspots.
    """

    navigation_tour_video_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `onboarding_steps` is present in `fetch_event_types`.
    
    URL of the navigation tour video to display to new users during
    onboarding. If `null`, the onboarding video experience is disabled.
    
    **Changes**: New in Zulip 10.0 (feature level 369).
    """

    max_message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `message` is present in `fetch_event_types`.
    
    The highest message ID among all messages the user has received as of the
    moment of this request.
    
    **Deprecated**: This field may be removed in future versions as it no
    longer has a clear purpose. Clients wishing to fetch the latest messages
    should pass `"anchor": "latest"` to `GET /messages`.
    """

    max_reminder_note_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum allowed length for a reminder note, in Unicode code points.
    
    **Changes**: New in Zulip 11.0 (feature level 415).
    """

    max_stream_name_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The maximum allowed length for a channel name, in Unicode code
    points. Clients should use this property rather than hardcoding
    field sizes.
    
    **Changes**: New in Zulip 4.0 (feature level 53). Previously,
    this required `stream` in `fetch_event_types`, was called
    `stream_name_max_length`, and always had a value of 60.
    """

    max_stream_description_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The maximum allowed length for a channel description, in Unicode
    code points. Clients should use this property rather than hardcoding
    field sizes.
    
    **Changes**: New in Zulip 4.0 (feature level 53). Previously,
    this required `stream` in `fetch_event_types`, was called
    `stream_description_max_length`, and always had a value of 1024.
    """

    max_channel_folder_name_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The maximum allowed length for a channel folder name, in Unicode
    code points. Clients should use this property rather than hardcoding
    field sizes.
    
    **Changes**: New in Zulip 11.0 (feature level 410). Clients should use
    60 as a fallback value on previous feature levels.
    """

    max_channel_folder_description_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The maximum allowed length for a channel folder description, in
    Unicode code points. Clients should use this property rather than
    hardcoding field sizes.
    
    **Changes**: New in Zulip 11.0 (feature level 410). Clients should use
    1024 as a fallback value on previous feature levels.
    """

    max_topic_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The maximum allowed length for a topic, in Unicode code points.
    Clients should use this property rather than hardcoding field
    sizes.
    
    **Changes**: New in Zulip 4.0 (feature level 53). Previously,
    this property always had a value of 60.
    """

    max_message_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The maximum allowed length for a message, in Unicode code points.
    Clients should use this property rather than hardcoding field
    sizes.
    
    **Changes**: New in Zulip 4.0 (feature level 53). Previously,
    this property always had a value of 10000.
    """

    server_min_deactivated_realm_deletion_days: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The minimum permitted number of days before full data deletion
    (users, channels, messages, etc.) of a deactivated organization.
    If `null`, then a deactivated organization's data can be
    deleted immediately.
    
    **Changes**: New in Zulip 10.0 (feature level 332)
    """

    server_max_deactivated_realm_deletion_days: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The maximum permitted number of days before full data deletion
    (users, channels, messages, etc.) of a deactivated organization.
    If `null`, then a deactivated organization's data can be
    retained indefinitely.
    
    **Changes**: New in Zulip 10.0 (feature level 332).
    """

    server_presence_ping_interval_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    For clients implementing the [presence](/api/get-presence) system,
    the time interval the client should use for sending presence requests
    to the server (and thus receive presence updates from the server).
    
    It is important for presence implementations to use both this and
    `server_presence_offline_threshold_seconds` correctly, so that a Zulip
    server can change these values to manage the trade-off between load and
    freshness of presence data.
    
    **Changes**: New in Zulip 7.0 (feature level 164). Clients should use 60
    for older Zulip servers, since that's the value that was hardcoded in the
    Zulip mobile apps prior to this parameter being introduced.
    """

    server_presence_offline_threshold_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    How old a presence timestamp for a given user can be before the user
    should be displayed as offline by clients displaying Zulip presence
    data. See the related `server_presence_ping_interval_seconds` for details.
    
    **Changes**: New in Zulip 7.0 (feature level 164). Clients should use 140
    for older Zulip servers, since that's the value that was hardcoded in the
    Zulip client apps prior to this parameter being introduced.
    """

    server_typing_started_expiry_period_milliseconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    For clients implementing [typing notifications](/api/set-typing-status)
    protocol, the time interval in milliseconds that the client should wait
    for additional [typing start](/api/get-events#typing-start) events from
    the server before removing an active typing indicator.
    
    **Changes**: New in Zulip 8.0 (feature level 204). Clients should use 15000
    for older Zulip servers, since that's the value that was hardcoded in the
    Zulip apps prior to this parameter being introduced.
    """

    server_typing_stopped_wait_period_milliseconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    For clients implementing [typing notifications](/api/set-typing-status)
    protocol, the time interval in milliseconds that the client should wait
    when a user stops interacting with the compose UI before sending a stop
    notification to the server.
    
    **Changes**: New in Zulip 8.0 (feature level 204). Clients should use 5000
    for older Zulip servers, since that's the value that was hardcoded in the
    Zulip apps prior to this parameter being introduced.
    """

    server_typing_started_wait_period_milliseconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    For clients implementing [typing notifications](/api/set-typing-status)
    protocol, the time interval in milliseconds that the client should use
    to send regular start notifications to the server to indicate that the
    user is still actively interacting with the compose UI.
    
    **Changes**: New in Zulip 8.0 (feature level 204). Clients should use 10000
    for older Zulip servers, since that's the value that was hardcoded in the
    Zulip apps prior to this parameter being introduced.
    """

    scheduled_messages: typing.Optional[typing.List[ScheduledMessage]] = pydantic.Field(default=None)
    """
    Present if `scheduled_messages` is present in `fetch_event_types`.
    
    An array of all undelivered scheduled messages by the user.
    
    **Changes**: New in Zulip 7.0 (feature level 179).
    """

    reminders: typing.Optional[typing.List[ScheduledMessage]] = pydantic.Field(default=None)
    """
    Present if `reminders` is present in `fetch_event_types`.
    
    An array of all undelivered reminders scheduled by the user.
    
    **Changes**: New in Zulip 11.0 (feature level 399).
    """

    muted_topics: typing.Optional[typing.List[typing.List[RegisterQueueResponseMutedTopicsItemItem]]] = pydantic.Field(
        default=None
    )
    """
    Present if `muted_topics` is present in `fetch_event_types`.
    
    Array of tuples, where each tuple describes a muted topic.
    The first element of the tuple is the channel name in which the topic
    has to be muted, the second element is the topic name to be muted
    and the third element is an integer UNIX timestamp representing
    when the topic was muted.
    
    **Changes**: Deprecated in Zulip 6.0 (feature level 134). Starting
    with this version, `muted_topics` will only be present in the
    response if the `user_topic` object, which generalizes and replaces
    this field, is not explicitly requested via `fetch_event_types`.
    
    Before Zulip 3.0 (feature level 1), the `muted_topics`
    array objects were 2-item tuples and did not include the timestamp
    information for when the topic was muted.
    """

    muted_users: typing.Optional[typing.List[RegisterQueueResponseMutedUsersItem]] = pydantic.Field(default=None)
    """
    Present if `muted_users` is present in `fetch_event_types`.
    
    A list of dictionaries where each dictionary describes
    a [muted user](/api/mute-user).
    
    **Changes**: New in Zulip 4.0 (feature level 48).
    """

    presences: typing.Optional[typing.Dict[str, RegisterQueueResponsePresencesValue]] = pydantic.Field(default=None)
    """
    Present if `presence` is present in `fetch_event_types`.
    
    A dictionary where each entry describes the presence details of a
    user in the Zulip organization.
    
    The format of the entry (modern or legacy) depends on the value of
    [`slim_presence`](#parameter-slim_presence).
    
    Users who have been offline for multiple weeks may not appear in this object.
    """

    presence_last_update_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `presence` is present in `fetch_event_types`.
    
    Provides the `last_update_id` value of the latest presence data fetched by
    the server and included in the response in `presences`. This can be used
    as the value of the `presence_last_update_id` parameter when polling
    for presence data at the [/users/me/presence](/api/update-presence) endpoint
    to tell the server to only fetch the relevant newer data in order to skip
    redundant already-known presence information.
    
    **Changes**: New in Zulip 9.0 (feature level 263).
    """

    server_timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    Present if `presence` is present in `fetch_event_types`.
    
    The time when the server fetched the
    `presences` data included in the response.
    Matches the similar field in presence
    responses.
    
    **Changes**: New in Zulip 5.0 (feature level 70).
    """

    realm_domains: typing.Optional[typing.List[RealmDomain]] = pydantic.Field(default=None)
    """
    Present if `realm_domains` is present in `fetch_event_types`.
    
    An array of dictionaries where each dictionary describes a domain within
    which users can join the organization without and invitation.
    """

    realm_emoji: typing.Optional[typing.Dict[str, RealmEmoji]] = pydantic.Field(default=None)
    """
    Present if `realm_emoji` is present in `fetch_event_types`.
    
    A dictionary of objects where each object describes a custom
    emoji that has been uploaded in this Zulip organization.
    """

    realm_linkifiers: typing.Optional[typing.List[RegisterQueueResponseRealmLinkifiersItem]] = pydantic.Field(
        default=None
    )
    """
    Present if `realm_linkifiers` is present in `fetch_event_types`.
    
    An ordered array of objects where each object describes a single
    [linkifier](/help/add-a-custom-linkifier).
    
    The order of the array reflects the order that each
    linkifier should be processed when linkifying messages
    and topics. By default, new linkifiers are ordered
    last. This order can be modified with [`PATCH
    /realm/linkifiers`](/api/reorder-linkifiers).
    
    Clients will receive an empty array unless the event queue is
    registered with the client capability `{"linkifier_url_template": true}`.
    See [`client_capabilities`](/api/register-queue#parameter-client_capabilities)
    parameter for how this can be specified.
    
    **Changes**: Before Zulip 7.0 (feature level 176), the
    `linkifier_url_template` client capability was not required. The
    requirement was added because linkifiers were updated to contain
    a URL template instead of a URL format string, which was a not
    backwards-compatible change.
    
    New in Zulip 4.0 (feature level 54). Clients can access this data for
    servers on earlier feature levels via the legacy `realm_filters` property.
    """

    realm_filters: typing.Optional[typing.List[typing.List[RegisterQueueResponseRealmFiltersItemItem]]] = (
        pydantic.Field(default=None)
    )
    """
    Legacy property for [linkifiers](/help/add-a-custom-linkifier).
    Present if `realm_filters` is present in `fetch_event_types`.
    
    When present, this is always an empty array.
    
    **Changes**: Prior to Zulip 7.0 (feature level 176), this was
    an array of tuples, where each tuple described a linkifier. The first
    element of the tuple was a string regex pattern which represented the
    pattern to be linkified on matching, for example `"#(?P<id>[123])"`.
    The second element was a URL format string that the pattern should be
    linkified with. A URL format string for the above example would be
    `"https://realm.com/my_realm_filter/%(id)s"`. And the third element
    was the ID of the realm filter.
    
    **Deprecated** in Zulip 4.0 (feature level 54), replaced by the
    `realm_linkifiers` key.
    """

    realm_playgrounds: typing.Optional[typing.List[RealmPlayground]] = pydantic.Field(default=None)
    """
    Present if `realm_playgrounds` is present in `fetch_event_types`.
    
    An array of dictionaries where each dictionary describes a
    [code playground](/help/code-blocks#code-playgrounds) configured for this Zulip organization.
    
    **Changes**: New in Zulip 4.0 (feature level 49).
    """

    realm_user_groups: typing.Optional[typing.List[UserGroup]] = pydantic.Field(default=None)
    """
    Present if `realm_user_groups` is present in `fetch_event_types`.
    
    An array of dictionaries where each dictionary describes a
    [user group](/help/user-groups) in the Zulip organization.
    
    Deactivated groups will only be included if `include_deactivated_groups`
    client capability is set to `true`.
    
    **Changes**: Prior to Zulip 10.0 (feature level 294), deactivated
    groups were included for all the clients.
    """

    realm_bots: typing.Optional[typing.List[Bot]] = pydantic.Field(default=None)
    """
    Present if `realm_bot` is present in `fetch_event_types`.
    
    An array of dictionaries where each dictionary describes a bot that the
    current user can administer. If the current user is an organization
    administrator, this will include all bots in the organization. Otherwise,
    it will only include bots owned by the user (either because the user created
    the bot or an administrator transferred the bot's ownership to the user).
    
    **Changes**: Removed `avatar_url`, `bot_type`, `email`, `full_name`, `is_active`
    and `owner_id` fields from the dictionary in Zulip 12.0 (feature level 474).
    Clients can get all these data from the corresponding user object.
    
    Removed `api_key` field from the dictionary in Zulip 12.0 (feature level 474).
    Clients now use [`GET /bots/{bot_id}/api_key`](/api/get-bot-api-key)
    to get api key for the bot.
    """

    realm_embedded_bots: typing.Optional[typing.List[RegisterQueueResponseRealmEmbeddedBotsItem]] = pydantic.Field(
        default=None
    )
    """
    Present if `realm_embedded_bots` is present in `fetch_event_types`.
    
    An array of dictionaries where each dictionary describes an type of embedded
    bot that is available to be configured on this Zulip server.
    
    Clients only need these data if they contain UI for creating or administering bots.
    """

    realm_incoming_webhook_bots: typing.Optional[typing.List[RegisterQueueResponseRealmIncomingWebhookBotsItem]] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm_incoming_webhook_bots` is present in `fetch_event_types`.
    
    An array of dictionaries where each dictionary describes a type of incoming webhook
    integration that is available to be configured on this Zulip server.
    
    Clients only need these data if they contain UI for creating or administering bots.
    """

    recent_private_conversations: typing.Optional[typing.List[RegisterQueueResponseRecentPrivateConversationsItem]] = (
        pydantic.Field(default=None)
    )
    """
    Present if `recent_private_conversations` is present in `fetch_event_types`.
    
    An array of dictionaries containing data on all direct message and group direct message
    conversations that the user has received (or sent) messages in, organized by
    conversation. This data set is designed to support UI elements such as the
    "Direct messages" widget in the web application showing recent direct message
    conversations that the user has participated in.
    
    "Recent" is defined as the server's discretion; the original implementation
    interpreted that as "the 1000 most recent direct messages the user received".
    """

    navigation_views: typing.Optional[typing.List[NavigationView]] = pydantic.Field(default=None)
    """
    Present if `navigation_views` is present in `fetch_event_types`.
    An array of dictionaries containing data on all of the current user's
    navigation views.
    
    **Changes**: New in Zulip 11.0 (feature level 390).
    """

    saved_snippets: typing.Optional[typing.List[SavedSnippet]] = pydantic.Field(default=None)
    """
    Present if `saved_snippets` is present in `fetch_event_types`.
    
    An array of dictionaries containing data on all of the current user's
    saved snippets.
    
    **Changes**: New in Zulip 10.0 (feature level 297).
    """

    subscriptions: typing.Optional[typing.List[Subscription]] = pydantic.Field(default=None)
    """
    Present if `subscription` is present in `fetch_event_types`.
    
    A array of dictionaries where each dictionary describes the properties
    of a channel the user is subscribed to (as well as that user's
    personal per-channel settings).
    
    **Changes**: Removed `email_address` field from the dictionary
    in Zulip 8.0 (feature level 226).
    
    Removed `role` field from the dictionary
    in Zulip 6.0 (feature level 133).
    """

    unsubscribed: typing.Optional[typing.List[Subscription]] = pydantic.Field(default=None)
    """
    Present if `subscription` is present in `fetch_event_types`.
    
    A array of dictionaries where each dictionary describes one of the
    channels the user has unsubscribed from but was previously subscribed to
    along with the subscription details.
    
    Unlike `never_subscribed`, the user might have messages in their personal
    message history that were sent to these channels.
    
    **Changes**: Prior to Zulip 10.0 (feature level 349), if a user was
    in `can_administer_channel_group` of a channel that they had
    unsubscribed from, but not an organization administrator, the channel
    in question would not be part of this array.
    
    Removed `email_address` field from the dictionary
    in Zulip 8.0 (feature level 226).
    
    Removed `role` field from the dictionary
    in Zulip 6.0 (feature level 133).
    """

    never_subscribed: typing.Optional[typing.List[RegisterQueueResponseNeverSubscribedItem]] = pydantic.Field(
        default=None
    )
    """
    Present if `subscription` is present in `fetch_event_types`.
    
    A array of dictionaries where each dictionary describes one of the
    channels that is visible to the user and the user has never been subscribed
    to.
    
    Important for clients containing UI where one can browse channels to subscribe
    to.
    
    **Changes**: Before Zulip 10.0 (feature level 362), archived channels did
    not appear in this list, even if the `archived_channels` [client
    capability][client-capabilities] was declared by the client.
    
    Prior to Zulip 10.0 (feature level 349), if a user was
    in `can_administer_channel_group` of a channel that they never
    subscribed to, but not an organization administrator, the channel
    in question would not be part of this array.
    """

    channel_folders: typing.Optional[typing.List[ChannelFolder]] = pydantic.Field(default=None)
    """
    Present if `channel_folders` is present in `fetch_event_types`.
    
    An array of dictionaries where each dictionary describes one
    of the channel folders in the organization.
    
    Only channel folders with one or more public web channels are
    visible to spectators.
    
    **Changes**: New in Zulip 11.0 (feature level 389).
    """

    unread_msgs: typing.Optional[RegisterQueueResponseUnreadMsgs] = pydantic.Field(default=None)
    """
    Present if `message` and `update_message_flags` are both present in
    `event_types`.
    
    A set of data structures describing the conversations containing
    the 50000 most recent unread messages the user has received. This will usually
    contain every unread message the user has received, but clients should support
    users with even more unread messages (and not hardcode the number 50000).
    """

    starred_messages: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Present if `starred_messages` is present in `fetch_event_types`.
    
    Array containing the IDs of all messages which have been
    [starred](/help/star-a-message) by the user.
    """

    streams: typing.Optional[typing.List[BasicChannel]] = pydantic.Field(default=None)
    """
    Present if `stream` is present in `fetch_event_types`.
    
    Array of dictionaries where each dictionary contains details about
    a single channel in the organization that is visible to the user.
    
    For organization administrators, this will include all private channels
    in the organization.
    
    **Changes**: Before Zulip 11.0 (feature level 378), archived channels
    did not appear in this list, even if the `archived_channels` [client
    capability][client-capabilities] was declared by the client.
    
    As of Zulip 8.0 (feature level 205), this will include all web-public
    channels in the organization as well.
    """

    realm_default_streams: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Present if `default_streams` is present in `fetch_event_types`.
    
    An array of IDs of all the [default channels](/help/set-default-streams-for-new-users)
    in the organization.
    
    **Changes**: Before Zulip 10.0 (feature level 330), we sent
    array of dictionaries where each dictionary contained details
    about a single default stream for the Zulip organization.
    """

    realm_default_stream_groups: typing.Optional[typing.List[DefaultChannelGroup]] = pydantic.Field(default=None)
    """
    Present if `default_stream_groups` is present in `fetch_event_types`.
    
    An array of dictionaries where each dictionary contains details
    about a single default channel group configured for this
    Zulip organization.
    
    Default channel groups are an experimental feature.
    """

    stop_words: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Present if `stop_words` is present in `fetch_event_types`.
    
    An array containing the stop words used by the Zulip server's
    full-text search implementation. Useful for showing helpful
    error messages when a search returns limited results because
    a stop word in the query was ignored.
    """

    user_status: typing.Optional[typing.Dict[str, RegisterQueueResponseUserStatusValue]] = pydantic.Field(default=None)
    """
    Present if `user_status` is present in `fetch_event_types`.
    
    A dictionary which contains the [status](/help/status-and-availability)
    of all users in the Zulip organization who have set a status.
    
    **Changes**: The emoji parameters are new in Zulip 5.0 (feature level 86).
    Previously, Zulip did not support emoji associated with statuses.
    """

    user_settings: typing.Optional[RegisterQueueResponseUserSettings] = pydantic.Field(default=None)
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

    user_topics: typing.Optional[typing.List[RegisterQueueResponseUserTopicsItem]] = pydantic.Field(default=None)
    """
    Present if `user_topic` is present in `fetch_event_types`.
    
    **Changes**: New in Zulip 6.0 (feature level 134), deprecating and
    replacing the previous `muted_topics` structure.
    """

    has_zoom_token: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `video_calls` is present in `fetch_event_types`.
    
    A boolean which signifies whether the user has a Zoom token and has thus
    completed OAuth flow for the [Zoom integration](/help/configure-call-provider).
    Clients need to know whether initiating Zoom OAuth is required before
    creating a Zoom call.
    """

    giphy_api_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `giphy` is present in `fetch_event_types`.
    
    GIPHY's client-side SDKs needs this API key to use the GIPHY API.
    GIPHY API keys are not secret (their main purpose appears to be
    allowing GIPHY to block a problematic app). Please don't use our API
    key for an app unrelated to Zulip.
    
    Developers of clients should also read the
    [GIPHY API TOS](https://support.giphy.com/hc/en-us/articles/360028134111-GIPHY-API-Terms-of-Service-)
    before using this API key.
    
    **Changes**: Added in Zulip 4.0 (feature level 47).
    """

    tenor_api_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `tenor` is present in `fetch_event_types`.
    
    Tenor API keys are meant to be sent to the clients, see the
    examples in the [Tenor Endpoints documentation](https://developers.google.com/tenor/guides/endpoints).
    Please don't use our API key for an app unrelated to Zulip.
    
    Developers of clients are recommended to use their Zulip client string,
    like `ZulipFlutter`, as the `client` in the Tenor API to differentiate
    across clients as per the [Tenor Endpoints documentation](https://developers.google.com/tenor/guides/endpoints).
    
    Developers of clients should also read the
    [Tenor API TOS](https://developers.google.com/tenor/guides/api-terms).
    
    **Changes**: New in Zulip 12.0 (feature level 442).
    """

    devices: typing.Optional[typing.Dict[str, RegisterQueueResponseDevicesValue]] = pydantic.Field(default=None)
    """
    Present if `device` is present in `fetch_event_types`.
    
    Dictionary where each entry describes the user's logged-in devices,
    registered using [`POST /register_client_device`](/api/register-client-device).
    
    **Changes**: New in Zulip 12.0 (feature level 468).
    """

    receives_typing_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user is configured to receive typing notifications from other
    users. The server will only deliver typing notifications events to users who
    for whom this is enabled.
    
    **Changes**: New in Zulip 9.0 (feature level 253). Previously, there were
    only options to disable sending typing notifications.
    """

    realm_message_edit_history_visibility_policy: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    What typesof message edit history are accessible to users via
    [message edit history](/help/view-a-messages-edit-history).
    
    - "all" = All edit history is visible.
    - "moves" = Only moves are visible.
    - "none" = No edit history is visible.
    
    **Changes**: New in Zulip 10.0 (feature level 358), replacing the previous
    `allow_edit_history` boolean setting; `true` corresponds to `all`,
    and `false` to `none`.
    """

    realm_allow_edit_history: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether this organization is configured to allow users to access
    [message edit history](/help/view-a-messages-edit-history).
    
    The value of `realm_allow_edit_history` is set as `false` if the
    `realm_message_edit_history_visibility_policy` is configured as "None"
    and `true` if it is configured as "Moves only" or "All".
    
    **Changes**: Deprecated in Zulip 10.0 (feature level 358) and will be
    removed in the future, as it is an inaccurate version
    `realm_message_edit_history_visibility_policy`, which replaces this field.
    """

    realm_can_add_custom_emoji_group: typing.Optional[RegisterQueueResponseRealmCanAddCustomEmojiGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to add custom emoji in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 307). Previously, this
    permission was controlled by the enum `add_custom_emoji_policy`. Values
    were 1=Members, 2=Admins, 3=Full members, 4=Moderators.
    
    Before Zulip 5.0 (feature level 85), the `realm_add_emoji_by_admins_only`
    boolean setting controlled this permission; `true` corresponded to `Admins`,
    and `false` to `Everyone`.
    """

    realm_can_add_subscribers_group: typing.Optional[RegisterQueueResponseRealmCanAddSubscribersGroup] = pydantic.Field(
        default=None
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to add subscribers to channels in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 341). Previously, this
    permission was controlled by the enum `invite_to_stream_policy`. Values
    were 1=Members, 2=Admins, 3=Full members, 4=Moderators.
    """

    realm_can_delete_any_message_group: typing.Optional[RegisterQueueResponseRealmCanDeleteAnyMessageGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to delete any message in the organization.
    
    Note that a user must also be able to access the content of a message
    in order to delete it. See [channel permissions](/help/channel-permissions)
    for information about content access for channel messages. For direct
    messages, the user must have received or sent the direct message to
    have content access.
    
    **Changes**: New in Zulip 10.0 (feature level 281). Previously, this
    permission was limited to administrators only and was uneditable.
    """

    realm_can_delete_own_message_group: typing.Optional[RegisterQueueResponseRealmCanDeleteOwnMessageGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to delete messages that they have sent in the
    organization.
    
    **Changes**: New in Zulip 10.0 (feature level 291). Previously, this
    permission was controlled by the enum `delete_own_message_policy`. Values
    were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 5=Everyone.
    
    Before Zulip 5.0 (feature level 101), the `allow_message_deleting` boolean
    setting controlled this permission; `true` corresponded to `Everyone`, and
    `false` to `Admins`.
    """

    realm_can_set_delete_message_policy_group: typing.Optional[
        RegisterQueueResponseRealmCanSetDeleteMessagePolicyGroup
    ] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to change per-channel `can_delete_any_message_group`
    and `can_delete_own_message_group` permission settings. Note that the user
    must be a member of both this group and the `can_administer_channel_group`
    of the channel whose message delete settings they want to change.
    
    Organization administrators can always change these settings of
    every channel.
    
    **Changes**: New in Zulip 11.0 (feature level 407).
    """

    realm_can_set_topics_policy_group: typing.Optional[RegisterQueueResponseRealmCanSetTopicsPolicyGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to change per-channel `topics_policy` setting. Note that
    the user must be a member of both this group and the `can_administer_channel_group`
    of the channel whose `topics_policy` they want to change.
    
    Organization administrators can always change the `topics_policy` setting of
    every channel.
    
    **Changes**: New in Zulip 11.0 (feature level 392).
    """

    realm_can_invite_users_group: typing.Optional[RegisterQueueResponseRealmCanInviteUsersGroup] = pydantic.Field(
        default=None
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to send email invitations for inviting other users
    to the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 321). Previously, this
    permission was controlled by the enum `invite_to_realm_policy`. Values
    were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 6=Nobody.
    
    Before Zulip 4.0 (feature level 50), the `invite_by_admins_only` boolean
    setting controlled this permission; `true` corresponded to `Admins`, and
    `false` to `Members`.
    """

    realm_can_mention_many_users_group: typing.Optional[RegisterQueueResponseRealmCanMentionManyUsersGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to use wildcard mentions in large channels.
    
    All users will receive a warning/reminder when using mentions in large
    channels, even when permitted to do so.
    
    **Changes**: New in Zulip 10.0 (feature level 352). Previously, this
    permission was controlled by the enum `wildcard_mention_policy`.
    """

    realm_can_move_messages_between_channels_group: typing.Optional[
        RegisterQueueResponseRealmCanMoveMessagesBetweenChannelsGroup
    ] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to move messages from one channel to another
    in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 310). Previously, this
    permission was controlled by the enum `move_messages_between_streams_policy`.
    Values were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 6=Nobody.
    
    In Zulip 7.0 (feature level 159), `Nobody` was added as an option to
    `move_messages_between_streams_policy` enum.
    """

    realm_can_move_messages_between_topics_group: typing.Optional[
        RegisterQueueResponseRealmCanMoveMessagesBetweenTopicsGroup
    ] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to move messages from one topic to another
    within a channel in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 316). Previously, this
    permission was controlled by the enum `edit_topic_policy`. Values were
    1=Members, 2=Admins, 3=Full members, 4=Moderators, 5=Everyone, 6=Nobody.
    
    In Zulip 7.0 (feature level 159), `Nobody` was added as an option to
    `edit_topic_policy` enum.
    """

    realm_can_create_groups: typing.Optional[RegisterQueueResponseRealmCanCreateGroups] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create user
    groups in this organization.
    
    **Changes**: New in Zulip 10.0 (feature level 299). Previously
    `realm_user_group_edit_policy` field used to control the
    permission to create user groups.
    """

    realm_can_create_bots_group: typing.Optional[RegisterQueueResponseRealmCanCreateBotsGroup] = pydantic.Field(
        default=None
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create all types of bot users
    in the organization. See also `can_create_write_only_bots_group`.
    
    **Changes**: New in Zulip 10.0 (feature level 344). Previously, this
    permission was controlled by the enum `bot_creation_policy`. Values
    were 1=Members, 2=Generic bots limited to administrators, 3=Administrators.
    """

    realm_can_create_write_only_bots_group: typing.Optional[RegisterQueueResponseRealmCanCreateWriteOnlyBotsGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create bot users that
    can only send messages in the organization, i.e. incoming webhooks,
    in addition to the users who are present in `can_create_bots_group`.
    
    **Changes**: New in Zulip 10.0 (feature level 344). Previously, this
    permission was controlled by the enum `bot_creation_policy`. Values
    were 1=Members, 2=Generic bots limited to administrators, 3=Administrators.
    """

    realm_can_manage_all_groups: typing.Optional[RegisterQueueResponseRealmCanManageAllGroups] = pydantic.Field(
        default=None
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values)
    defining the set of users who have permission to
    administer all existing groups in this organization.
    
    **Changes**: Prior to Zulip 10.0 (feature level 305), only users who
    were a member of the group or had the moderator role or above could
    exercise the permission on a given group.
    
    New in Zulip 10.0 (feature level 299). Previously the
    `user_group_edit_policy` field controlled the permission
    to manage user groups. Valid values were as follows:
    
    - 1 = All members can create and edit user groups
    - 2 = Only organization administrators can create and edit
      user groups
    - 3 = Only [full members][calc-full-member] can create and
      edit user groups.
    - 4 = Only organization administrators and moderators can
      create and edit user groups.
    
    [calc-full-member]: /api/roles-and-permissions#determining-if-a-user-is-a-full-member
    """

    realm_can_manage_billing_group: typing.Optional[RegisterQueueResponseRealmCanManageBillingGroup] = pydantic.Field(
        default=None
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to manage plans and billing in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 363). Previously, only owners
    and users with `is_billing_admin` property set to `true` were allowed to
    manage plans and billing.
    """

    realm_can_create_public_channel_group: typing.Optional[RegisterQueueResponseRealmCanCreatePublicChannelGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create public
    channels in this organization.
    
    **Changes**: New in Zulip 9.0 (feature level 264). Previously
    `realm_create_public_stream_policy` field used to control the
    permission to create public channels.
    """

    realm_can_create_private_channel_group: typing.Optional[RegisterQueueResponseRealmCanCreatePrivateChannelGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create private
    channels in this organization.
    
    **Changes**: New in Zulip 9.0 (feature level 266). Previously
    `realm_create_private_stream_policy` field used to control the
    permission to create private channels.
    """

    realm_can_create_web_public_channel_group: typing.Optional[
        RegisterQueueResponseRealmCanCreateWebPublicChannelGroup
    ] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create web-public
    channels in this organization.
    
    Has no effect and should not be displayed in settings UI
    unless the Zulip server has the `WEB_PUBLIC_STREAMS_ENABLED`
    server-level setting enabled and the organization has enabled
    the `enable_spectator_access` realm setting.
    
    **Changes**: New in Zulip 10.0 (feature level 280). Previously
    `realm_create_web_public_stream_policy` field used to control
    the permission to create web-public channels.
    """

    realm_can_resolve_topics_group: typing.Optional[RegisterQueueResponseRealmCanResolveTopicsGroup] = pydantic.Field(
        default=None
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to [resolve topics](/help/resolve-a-topic)
    in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 367). Previously, permission
    to resolve topics was controlled by the more general
    `can_move_messages_between_topics_group permission for moving messages`.
    """

    realm_create_public_stream_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A deprecated representation of a superset of the users who
    have permission to create public channels in the organization,
    available for backwards-compatibility. Clients should use
    `can_create_public_channel_group` instead.
    
    It is an enum with the following possible values, corresponding
    to roles/system groups:
    
    - 1 = Members only
    - 2 = Admins only
    - 3 = [Full members][calc-full-member] only
    - 4 = Admins and moderators only
    
    **Changes**: Deprecated in Zulip 9.0 (feature level 264) and
    replaced by `realm_can_create_public_channel_group`, which
    supports finer resolution of configurations, resulting in this
    property being inaccurate following that transition.
    
    Before Zulip 5.0 (feature level 102), permission to create
    channels was controlled by the `realm_create_stream_policy` setting.
    
    [permission-level]: /api/roles-and-permissions#permission-levels
    [calc-full-member]: /api/roles-and-permissions#determining-if-a-user-is-a-full-member
    """

    realm_create_private_stream_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A deprecated representation of a superset of the users who
    have permission to create private channels in the organization,
    available for backwards-compatibility. Clients should use
    `can_create_private_channel_group` instead.
    
    It is an enum with the following possible values, corresponding
    to roles/system groups:
    
    - 1 = Members only
    - 2 = Admins only
    - 3 = [Full members][calc-full-member] only
    - 4 = Admins and moderators only
    
    **Changes**: Deprecated in Zulip 9.0 (feature level 266) and
    replaced by `realm_can_create_private_channel_group`, which
    supports finer resolution of configurations, resulting in this
    property being inaccurate following that transition.
    
    **Changes**: Before Zulip 5.0 (feature level 102), permission to
    create channels was controlled by the `realm_create_stream_policy` setting.
    
    [permission-level]: /api/roles-and-permissions#permission-levels
    [calc-full-member]: /api/roles-and-permissions#determining-if-a-user-is-a-full-member
    """

    realm_create_web_public_stream_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A deprecated representation of a superset of the users who
    have permission to create web-public channels in the
    organization, available for backwards-compatibility. Clients
    should use `can_create_web_public_channel_group` instead.
    
    It is an enum with the following possible values, corresponding
    to roles/system groups:
    
    - 2 = Admins only
    - 4 = Admins and moderators only
    - 6 = Nobody
    - 7 = Owners only
    
    **Changes**: Deprecated in Zulip 10.0 (feature level 280) and
    replaced by `realm_can_create_web_public_channel_group`, which
    supports finer resolution of configurations, resulting in this
    property being inaccurate following that transition.
    
    **Changes**: Added in Zulip 5.0 (feature level 103).
    
    [permission-level]: /api/roles-and-permissions#permission-levels
    """

    realm_wildcard_mention_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A deprecated representation of a superset of the users who
    have permission to use wildcard mentions in large channels,
    available for backwards-compatibility. Clients should use
    `can_mention_many_users_group` instead.
    
    It is an enum with the following possible values, corresponding
    to roles/system groups:
    
    - 1 = Any user can use wildcard mentions in large channels.
    - 2 = Only members can use wildcard mentions in large channels.
    - 3 = Only [full members][calc-full-member] can use wildcard mentions in large channels.
    - 5 = Only organization administrators can use wildcard mentions in large channels.
    - 6 = Nobody can use wildcard mentions in large channels.
    - 7 = Only organization administrators and moderators can use wildcard mentions in large channels.
    
    All users will receive a warning/reminder when using
    mentions in large channels, even when permitted to do so.
    
    **Changes**: Deprecated in Zulip 10.0 (feature level 352) and
    replaced by `realm_can_mention_many_users_group`, which
    supports finer resolution of configurations, resulting in this
    property being inaccurate following that transition.
    
    Channel administrators option removed in Zulip 6.0 (feature level 133).
    
    Moderators option added in Zulip 4.0 (feature level 62).
    
    New in Zulip 4.0 (feature level 33).
    
    [permission-level]: /api/roles-and-permissions#permission-levels
    [calc-full-member]: /api/roles-and-permissions#determining-if-a-user-is-a-full-member
    """

    realm_default_language: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The [organization language][org-lang] for automated messages and invitation emails.
    
    [org-lang]: /help/configure-organization-language
    """

    realm_welcome_message_custom_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    This organization's configured custom message for Welcome Bot
    to send to new user accounts, in Zulip Markdown format.
    
    **Changes**: New in Zulip 11.0 (feature level 416).
    """

    realm_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The description of the organization, used on login and registration pages.
    """

    realm_digest_emails_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the organization has enabled [weekly digest emails](/help/digest-emails).
    """

    realm_disallow_disposable_email_addresses: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the organization disallows disposable email
    addresses.
    """

    realm_email_changes_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether users are allowed to change their own email address in this
    organization. This is typically disabled for organizations that
    synchronize accounts from LDAP or a similar corporate database.
    """

    realm_invite_required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether an invitation is required to join this organization.
    """

    realm_create_multiuse_invite_group: typing.Optional[RegisterQueueResponseRealmCreateMultiuseInviteGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the
    set of users who are allowed to create [reusable invitation
    links](/help/invite-new-users#create-a-reusable-invitation-link)
    to the organization.
    
    **Changes**: Prior to Zulip 10.0 (feature level 314), this value used
    to be of type integer and did not accept anonymous user groups.
    
    New in Zulip 8.0 (feature level 209).
    """

    realm_media_preview_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The organization's policy for the size of image and video
    thumbnails in messages, expressed as a percentage of the
    default height. Currently, only certain values are permitted.
    
    - `100`: 100% height (the default).
    - `150`: 150% height.
    - `200`: 200% height.
    
    **Changes**: New in Zulip 12.0 (feature level 469).
    """

    realm_inline_image_preview: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether this organization has been configured to enable
    [previews of linked images](/help/image-video-and-website-previews).
    """

    realm_inline_url_embed_preview: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether this organization has been configured to enable
    [previews of linked websites](/help/image-video-and-website-previews).
    """

    realm_topics_policy: typing.Optional[RegisterQueueResponseRealmTopicsPolicy] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The organization's default policy for sending channel messages to the
    [empty "general chat" topic](/help/require-topics).
    
    - `"allow_empty_topic"`: Channel messages can be sent to the empty topic.
    - `"disable_empty_topic"`: Channel messages cannot be sent to the empty topic.
    
    **Changes**: New in Zulip 11.0 (feature level 392). Previously, this was
    controlled by the boolean `realm_mandatory_topics` setting, which is now
    deprecated.
    """

    realm_mandatory_topics: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether [topics are required](/help/require-topics) for messages in this
    organization.
    
    **Changes**: Deprecated in Zulip 11.0 (feature level 392). This is now
    controlled by the realm `topics_policy` setting.
    """

    realm_message_retention_days: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The default [message retention policy](/help/message-retention-policy)
    for this organization. It can have one special value:
    
    - `-1` denoting that the messages will be retained forever for this realm, by default.
    
    **Changes**: Prior to Zulip 3.0 (feature level 22), no limit was
    encoded as `null` instead of `-1`. Clients can correctly handle all
    server versions by treating both `-1` and `null` as indicating
    unlimited message retention.
    """

    realm_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The name of the organization, used in login pages etc.
    """

    realm_require_e2ee_push_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether this realm is configured to disallow sending mobile
    push notifications with message content through the legacy
    mobile push notifications APIs. The new API uses end-to-end
    encryption to protect message content and metadata from
    being accessible to the push bouncer service, APNs, and
    FCM. Clients that support the new E2EE API will use it
    automatically regardless of this setting.
    
    If `true`, mobile push notifications sent to clients that
    lack support for E2EE push notifications will always have
    "New message" as their content. Note that these legacy
    mobile notifications will still contain metadata, which may
    include the message's ID, the sender's name, email address,
    and avatar.
    
    In a future release, once the official mobile apps have
    implemented fully validated their E2EE protocol support,
    this setting will become strict, and disable the legacy
    protocol entirely.
    
    **Changes**: New in Zulip 11.0 (feature level 409). Previously,
    this behavior was available only via the
    `PUSH_NOTIFICATION_REDACT_CONTENT` global server setting.
    """

    realm_require_unique_names: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Indicates whether the organization is configured to require users
    to have unique full names. If true, the server will reject attempts
    to create a new user, or change the name of an existing user, where
    doing so would lead to two users whose names are identical modulo
    case and unicode normalization.
    
    **Changes**: New in Zulip 9.0 (feature level 246). Previously, the Zulip
    server could not be configured to enforce unique names.
    """

    realm_name_changes_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Indicates whether users are
    [allowed to change](/help/restrict-name-and-email-changes) their name
    via the Zulip UI in this organization. Typically disabled
    in organizations syncing this type of account information from
    an external user database like LDAP.
    """

    realm_avatar_changes_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Indicates whether users are
    [allowed to change](/help/restrict-name-and-email-changes) their avatar
    via the Zulip UI in this organization. Typically disabled
    in organizations syncing this type of account information from
    an external user database like LDAP.
    """

    realm_emails_restricted_to_domains: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether [new users joining](/help/restrict-account-creation#configuring-email-domain-restrictions)
    this organization are required to have an email
    address in one of the `realm_domains` configured for the organization.
    """

    realm_send_channel_events_messages: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Indicates whether channel event messages are sent in this organization.
    
    **Changes**: New in Zulip 12.0 (feature level 434). Previously,
    channel events were sent unconditionally.
    """

    realm_send_welcome_emails: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether or not this organization is configured to send the standard Zulip
    [welcome emails](/help/disable-welcome-emails) to new users joining the organization.
    """

    realm_message_content_allowed_in_email_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether notification emails in this organization are allowed to
    contain Zulip the message content, or simply indicate that a new
    message was sent.
    """

    realm_enable_spectator_access: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether web-public channels and related anonymous access APIs/features
    are enabled in this organization.
    
    Can only be enabled if the `WEB_PUBLIC_STREAMS_ENABLED`
    [server setting][server-settings] is enabled on the Zulip
    server. See also the `can_create_web_public_channel_group` realm
    setting.
    
    **Changes**: New in Zulip 5.0 (feature level 109).
    
    [server-settings]: https://zulip.readthedocs.io/en/stable/production/settings.html
    """

    realm_want_advertise_in_communities_directory: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the organization has given permission to be advertised in the
    Zulip [communities directory](/help/communities-directory).
    
    Useful only to clients supporting changing this setting for the
    organization.
    
    Giving permission via this setting does not guarantee that an
    organization will be listed in the Zulip communities directory.
    
    **Changes**: New in Zulip 6.0 (feature level 129).
    """

    realm_video_chat_provider: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The configured [video call provider](/help/configure-call-provider) for the
    organization.
    
    - 0 = None
    - 1 = Jitsi Meet
    - 3 = Zoom (User OAuth integration)
    - 4 = BigBlueButton
    - 5 = Zoom (Server to Server OAuth integration)
    - 6 = Constructor Groups
    - 7 = Nextcloud Talk
    
    Note that only one of the [Zoom integrations][zoom-video-calls] can
    be configured on a Zulip server.
    
    **Changes**: In Zulip 12.0 (feature level 465), added the
    Nextcloud Talk option.
    
    In Zulip 12.0 (feature level 460), added the
    Constructor Groups option.
    
    In Zulip 10.0 (feature level 353), added the Zoom Server
    to Server OAuth option.
    
    In Zulip 3.0 (feature level 1), added the None option
    to disable video call UI.
    
    [zoom-video-calls]: https://zulip.readthedocs.io/en/latest/production/video-calls.html#zoom
    """

    realm_jitsi_server_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The URL of the custom Jitsi Meet server configured in this organization's
    settings.
    
    `null`, the default, means that the organization is using the should use the
    server-level configuration, `server_jitsi_server_url`. A correct client
    supporting only the modern API should use `realm_jitsi_server_url ||
    server_jitsi_server_url` to create calls.
    
    **Changes**: New in Zulip 8.0 (feature level 212). Previously, this was only
    available as a server-level configuration, which was available via the
    `jitsi_server_url` field.
    """

    realm_gif_rating_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Maximum rating of the GIFs that will be retrieved by the
    GIPHY and Tenor integrations in this organization.
    
    **Changes**: Before Zulip 12.0 (feature level 453), this was called
    `realm_giphy_rating`.
    
    **Changes**: Before Zulip 12.0 (feature level 442), this was only used by
    the Giphy integration.
    
    New in Zulip 4.0 (feature level 55).
    """

    realm_waiting_period_threshold: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Members whose accounts have been created at least this many days ago
    will be treated as [full members][calc-full-member]
    for the purpose of settings that restrict access to new members.
    
    [calc-full-member]: /api/roles-and-permissions#determining-if-a-user-is-a-full-member
    """

    realm_digest_weekday: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The day of the week when the organization will send
    its weekly digest email to inactive users.
    """

    realm_direct_message_initiator_group: typing.Optional[RegisterQueueResponseRealmDirectMessageInitiatorGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to start a new direct message conversation
    involving other non-bot users. Users who are outside this group and attempt
    to send the first direct message to a given collection of recipient users
    will receive an error, unless all other recipients are bots or the sender.
    
    **Changes**: New in Zulip 9.0 (feature level 270).
    
    Previously, access to send direct messages was controlled by the
    `private_message_policy` realm setting, which supported values of
    1 (enabled) and 2 (disabled).
    """

    realm_direct_message_permission_group: typing.Optional[RegisterQueueResponseRealmDirectMessagePermissionGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to fully use direct messages. Users outside
    this group can only send direct messages to conversations where all the
    recipients are in this group, are bots, or are the sender, ensuring that
    every direct message conversation will be visible to at least one user in
    this group.
    
    **Changes**: New in Zulip 9.0 (feature level 270).
    
    Previously, access to send direct messages was controlled by the
    `private_message_policy` realm setting, which supported values of
    1 (enabled) and 2 (disabled).
    """

    realm_default_code_block_language: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The default pygments language code to be used for code blocks in this
    organization. If an empty string, no default has been set.
    
    **Changes**: Prior to Zulip 8.0 (feature level 195), a server bug meant
    that both `null` and an empty string could represent that no default was
    set for this realm setting. Clients supporting older server versions
    should treat either value (`null` or `""`) as no default being set.
    """

    realm_message_content_delete_limit_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Messages sent more than this many seconds ago cannot be deleted
    with this organization's
    [message deletion policy](/help/restrict-message-editing-and-deletion).
    
    Will not be 0. A `null` value means no limit: messages can be deleted
    regardless of how long ago they were sent.
    
    **Changes**: No limit was represented using the
    special value `0` before Zulip 5.0 (feature level 100).
    """

    realm_authentication_methods: typing.Optional[typing.Dict[str, RealmAuthenticationMethod]] = pydantic.Field(
        default=None
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Dictionary of authentication method keys mapped to dictionaries that
    describe the properties of the named authentication method for the
    organization - its enabled status and availability for use by the
    organization.
    
    Clients should use this to implement server-settings UI to change which
    methods are enabled for the organization. For authentication UI itself,
    clients should use the pre-authentication metadata returned by
    [`GET /server_settings`](/api/get-server-settings).
    
    **Changes**: In Zulip 9.0 (feature level 241), the values in this
    dictionary were changed. Previously, the values were a simple boolean
    indicating whether the backend is enabled or not.
    """

    realm_allow_message_editing: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether this organization's [message edit policy][config-message-editing]
    allows editing the content of messages.
    
    See [`PATCH /messages/{message_id}`](/api/update-message) for details and
    history of how message editing permissions work.
    
    [config-message-editing]: /help/restrict-message-editing-and-deletion
    """

    realm_message_content_edit_limit_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Messages sent more than this many seconds ago cannot be edited
    with this organization's
    [message edit policy](/help/restrict-message-editing-and-deletion).
    
    Will not be `0`. A `null` value means no limit, so messages can be edited
    regardless of how long ago they were sent.
    
    See [`PATCH /messages/{message_id}`](/api/update-message) for details and
    history of how message editing permissions work.
    
    **Changes**: Before Zulip 6.0 (feature level 138), no limit was
    represented using the special value `0`.
    """

    realm_move_messages_within_stream_limit_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Messages sent more than this many seconds ago cannot be moved within a
    channel to another topic by users who have permission to do so based on this
    organization's [topic edit policy](/help/restrict-moving-messages). This
    setting does not affect moderators and administrators.
    
    Will not be `0`. A `null` value means no limit, so message topics can be
    edited regardless of how long ago they were sent.
    
    See [`PATCH /messages/{message_id}`](/api/update-message) for details and
    history of how message editing permissions work.
    
    **Changes**: New in Zulip 7.0 (feature level 162). Previously, this time
    limit was always 72 hours for users who were not administrators or
    moderators.
    """

    realm_move_messages_between_streams_limit_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Messages sent more than this many seconds ago cannot be moved between
    channels by users who have permission to do so based on this organization's
    [message move policy](/help/restrict-moving-messages). This setting does
    not affect moderators and administrators.
    
    Will not be `0`. A `null` value means no limit, so messages can be moved
    regardless of how long ago they were sent.
    
    See [`PATCH /messages/{message_id}`](/api/update-message) for details and
    history of how message editing permissions work.
    
    **Changes**: New in Zulip 7.0 (feature level 162). Previously, there was
    no time limit for moving messages between channels for users with permission
    to do so.
    """

    realm_enable_read_receipts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether read receipts is enabled in the organization or not.
    
    If disabled, read receipt data will be unavailable to clients, regardless
    of individual users' personal read receipt settings. See also the
    `send_read_receipts` setting within `realm_user_settings_defaults`.
    
    **Changes**: New in Zulip 6.0 (feature level 137).
    """

    realm_icon_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The URL of the organization's [profile icon](/help/create-your-organization-profile).
    """

    realm_icon_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    String indicating whether the organization's
    [profile icon](/help/create-your-organization-profile) was uploaded
    by a user or is the default. Useful for UI allowing editing the organization's icon.
    
    - "G" means generated by Gravatar (the default).
    - "U" means uploaded by an organization administrator.
    """

    realm_workplace_users_group: typing.Optional[RegisterQueueResponseRealmWorkplaceUsersGroup] = pydantic.Field(
        default=None
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the set of
    users who will be considered as workplace users for billing.
    
    **Changes**: New in Zulip 12.0 (feature level 477).
    """

    max_icon_file_size_mib: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The maximum file size allowed for the organization's
    icon. Useful for UI allowing editing the organization's icon.
    
    **Changes**: New in Zulip 5.0 (feature level 72). Previously,
    this was called `max_icon_file_size`.
    """

    realm_logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The URL of the organization's wide logo configured in the
    [organization profile](/help/create-your-organization-profile).
    """

    realm_logo_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    String indicating whether the organization's
    [profile wide logo](/help/create-your-organization-profile) was uploaded
    by a user or is the default. Useful for UI allowing editing the
    organization's wide logo.
    
    - "D" means the logo is the default Zulip logo.
    - "U" means uploaded by an organization administrator.
    """

    realm_night_logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The URL of the organization's dark theme wide-format logo configured in the
    [organization profile](/help/create-your-organization-profile).
    """

    realm_night_logo_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    String indicating whether the organization's dark theme
    [profile wide logo](/help/create-your-organization-profile) was uploaded
    by a user or is the default. Useful for UI allowing editing the
    organization's wide logo.
    
    - "D" means the logo is the default Zulip logo.
    - "U" means uploaded by an organization administrator.
    """

    max_logo_file_size_mib: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The maximum file size allowed for the uploaded organization logos.
    
    **Changes**: New in Zulip 5.0 (feature level 72). Previously,
    this was called `max_logo_file_size`.
    """

    realm_bot_domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The fake email domain that will be used for new bots created this
    organization. Useful for UI for creating bots.
    """

    realm_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The URL for the organization. Alias of `realm_url`.
    
    **Changes**: Deprecated in Zulip 9.0 (feature level 257). The term
    "URI" is deprecated in [web standards](https://url.spec.whatwg.org/#goals).
    """

    realm_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The URL for the organization.
    
    **Changes**: New in Zulip 9.0 (feature level 257), replacing the
    deprecated `realm_uri`.
    """

    realm_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A unique identifier for the organization, expected to be stable
    even if the organization migrates between hosting environments.
    
    Used as the salt for Jdenticon avatars; Clients that prefer to compute
    Jdenticon avatars may use `{realm_uuid}:{user_id}` as the Jdenticon key.
    
    **Changes**: New in Zulip 12.0 (feature level 466).
    """

    realm_available_video_chat_providers: typing.Optional[
        typing.Dict[str, RegisterQueueResponseRealmAvailableVideoChatProvidersValue]
    ] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Dictionary where each entry describes a supported [video call
    provider](/help/configure-call-provider) that is configured on this
    server and could be selected by an organization administrator.
    
    Useful for administrative settings UI that allows changing the realm
    setting `video_chat_provider`.
    """

    realm_presence_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether online presence of other users is shown in this
    organization.
    """

    settings_send_digest_emails: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether this Zulip server is configured to allow organizations to
    enable [digest emails](/help/digest-emails).
    
    Relevant for administrative settings UI that can change the digest
    email settings.
    """

    realm_email_auth_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the organization has enabled Zulip's default email and password
    authentication feature. Determines whether Zulip stores a password
    for the user and clients should offer any UI for changing the user's
    Zulip password.
    """

    realm_password_auth_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the organization allows any sort of password-based
    authentication (whether via EmailAuthBackend or LDAP passwords).
    
    Determines whether a client might ever need to display a password prompt
    (clients will primarily look at this attribute in [server_settings](/api/get-server-settings)
    before presenting a login page).
    """

    realm_push_notifications_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether push notifications are enabled for this organization. Typically
    `true` for Zulip Cloud and self-hosted realms that have a valid
    registration for the [Mobile push notifications
    service](https://zulip.readthedocs.io/en/latest/production/mobile-push-notifications.html),
    and `false` for self-hosted servers that do not.
    
    **Changes**: Before Zulip 8.0 (feature level 231), this incorrectly was
    `true` for servers that were partly configured to use the Mobile Push
    Notifications Service but not properly registered.
    """

    realm_push_notifications_enabled_end_timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    If the server expects the realm's push notifications access to end at a
    definite time in the future, the UNIX timestamp (UTC) at which this is
    expected to happen. Mobile clients should use this field to display warnings
    to users when the indicated timestamp is near.
    
    **Changes**: New in Zulip 8.0 (feature level 231).
    """

    realm_upload_quota_mib: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The total quota for uploaded files in this organization.
    
    Clients are not responsible for checking this quota; it is included
    in the API only for display purposes.
    
    If `null`, there is no limit.
    
    **Changes**: Before Zulip 9.0 (feature level 251), this field
    was incorrectly measured in bytes, not MiB.
    
    New in Zulip 5.0 (feature level 72). Previously,
    this was called `realm_upload_quota`.
    """

    realm_org_type: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The [organization type](/help/organization-type) for the realm.
    Useful only to clients supporting changing this setting for the
    organization, or clients implementing onboarding content or
    other features that varies with organization type.
    
    - 0 = Unspecified
    - 10 = Business
    - 20 = Open-source project
    - 30 = Education (non-profit)
    - 35 = Education (for-profit)
    - 40 = Research
    - 50 = Event or conference
    - 60 = Non-profit (registered)
    - 70 = Government
    - 80 = Political group
    - 90 = Community
    - 100 = Personal
    - 1000 = Other
    
    **Changes**: New in Zulip 6.0 (feature level 128).
    """

    realm_owner_full_content_access: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the organization's security model allows owners to access
    all private content in this organization.
    
    Note that this security model configuration can only be changed
    via a command-line management command.
    
    **Changes**: New in Zulip 12.0 (feature level 438).
    """

    realm_plan_type: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The plan type of the organization.
    
    - 1 = Self-hosted organization (SELF_HOSTED)
    - 2 = Zulip Cloud free plan (LIMITED)
    - 3 = Zulip Cloud Standard plan (STANDARD)
    - 4 = Zulip Cloud Standard plan, sponsored for free (STANDARD_FREE)
    """

    realm_enable_guest_user_dm_warning: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether clients should show a warning when a user is composing
    a DM to a guest user in this organization.
    
    **Changes**: New in Zulip 10.0 (feature level 348).
    """

    realm_enable_guest_user_indicator: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether clients should display "(guest)" after the names of
    guest users to prominently highlight their status.
    
    **Changes**: New in Zulip 8.0 (feature level 216).
    """

    realm_can_access_all_users_group: typing.Optional[RegisterQueueResponseRealmCanAccessAllUsersGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the
    set of users who are allowed to access all users in the
    organization.
    
    **Changes**: Prior to Zulip 10.0 (feature level 314), this value used
    to be of type integer and did not accept anonymous user groups.
    
    New in Zulip 8.0 (feature level 225).
    """

    realm_can_summarize_topics_group: typing.Optional[RegisterQueueResponseRealmCanSummarizeTopicsGroup] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A [group-setting value](/api/group-setting-values) defining the
    set of users who are allowed to use AI summarization.
    
    **Changes**: New in Zulip 10.0 (feature level 350).
    """

    zulip_plan_is_not_limited: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the organization is using a limited (Zulip Cloud Free) plan.
    """

    upgrade_text_for_wide_organization_logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Text to use when displaying UI for wide organization logos, a feature
    that is currently not available on the Zulip Cloud Free plan.
    
    Useful only for clients supporting administrative UI for uploading
    a new wide organization logo to brand the organization.
    """

    realm_default_external_accounts: typing.Optional[
        typing.Dict[str, RegisterQueueResponseRealmDefaultExternalAccountsValue]
    ] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Dictionary where each entry describes a default external
    account type that can be configured with Zulip's [custom
    profile fields feature](/help/custom-profile-fields).
    
    **Changes**: New in Zulip 2.1.0.
    """

    realm_default_avatar_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The avatar data source type for new users.
    
    - "G" = Hosted by Gravatar
    - "J" = Generated using Jdenticon
    
    Note that "U" is not a supported value here, since there is
    no such thing as a "default" user-uploaded avatar.
    
    **Changes**: New in Zulip 12.0 (feature level 456).
    """

    jitsi_server_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The base URL to be used to create Jitsi video calls. Equals
    `realm_jitsi_server_url || server_jitsi_server_url`.
    
    **Changes**: Deprecated in Zulip 8.0 (feature level 212) and will
    eventually be removed. Previously, the Jitsi server to use was not
    configurable on a per-realm basis, and this field contained the server's
    configured Jitsi server. (Which is now provided as
    `server_jitsi_server_url`). Clients supporting older versions should fall
    back to this field when creating calls: using `realm_jitsi_server_url ||
    server_jitsi_server_url` with newer servers and using `jitsi_server_url`
    with servers below feature level 212.
    """

    development_environment: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether this Zulip server is a development environment. Used
    to control certain features or UI (such as error popups)
    that should only apply when connected to a Zulip development
    environment.
    """

    server_generation: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A timestamp indicating when the process hosting this
    event queue was started. Clients will likely only find
    this value useful for inclusion in detailed error reports.
    """

    password_min_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    This Zulip server's configured minimum required length for passwords.
    Necessary for password change UI to show whether the password
    will be accepted.
    """

    password_max_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    This Zulip server's configured maximum length for passwords.
    Necessary for password change UI to show whether the password
    will be accepted.
    
    **Changes**: New in Zulip 10.0 (feature level 338).
    """

    password_min_guesses: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    This Zulip server's configured minimum `zxcvbn` minimum guesses.
    Necessary for password change UI to show whether the password
    will be accepted.
    """

    gif_rating_policy_options: typing.Optional[typing.Dict[str, RegisterQueueResponseGifRatingPolicyOptionsValue]] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Dictionary where each entry describes a valid rating configuration
    that is available on this server and could be selected by an
    organization administrator.
    
    Useful for administrative settings UI that allows changing the
    allowed rating of GIFs.
    
    **Changes**: Before Zulip 12.0 (feature level 453), this was
    called `gif_rating_options`.
    
    **Changes**: Before Zulip 12.0 (feature level 442), this was called
    `giphy_rating_options` and only supported the original GIPHY gif picker
    integration.
    
    `giphy_rating_options` was new in Zulip 4.0 (feature level 55).
    """

    max_file_upload_size_mib: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The maximum file size that can be uploaded to this Zulip organization.
    """

    max_avatar_file_size_mib: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The maximum avatar size that can be uploaded to this Zulip server.
    """

    server_inline_image_preview: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the server is configured with support for inline image previews.
    Clients containing administrative UI for changing
    `realm_inline_image_preview` should consult this field before offering
    that feature.
    """

    server_inline_url_embed_preview: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the server is configured with support for inline URL previews.
    Clients containing administrative UI for changing
    `realm_inline_url_embed_preview` should consult this field before offering
    that feature.
    """

    server_thumbnail_formats: typing.Optional[typing.List[RegisterQueueResponseServerThumbnailFormatsItem]] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A list describing the image formats that uploaded
    images will be thumbnailed into. Any image with a
    source starting with `/user_uploads/thumbnail/` can
    have its last path component replaced with any of the
    names contained in this list, to obtain the desired
    thumbnail size.
    
    See [Images in Markdown messages](/api/message-formatting#images)
    for details of how Zulip renders images, and how
    clients should handle them.
    
    **Changes**: New in Zulip 9.0 (feature level 273).
    """

    server_avatar_changes_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the server allows avatar changes. Similar to
    `realm_avatar_changes_disabled` but based on the `AVATAR_CHANGES_DISABLED`
    Zulip server level setting.
    """

    server_name_changes_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the server allows name changes. Similar to
    `realm_name_changes_disabled` but based on the `NAME_CHANGES_DISABLED`
    Zulip server level setting.
    """

    server_needs_upgrade: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Whether the server is running an old version based on the Zulip
    [server release lifecycle](https://zulip.readthedocs.io/en/latest/overview/release-lifecycle.html#upgrade-nag),
    such that the web app will display to the current user a prominent warning.
    
    **Changes**: New in Zulip 5.0 (feature level 74).
    """

    server_web_public_streams_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The value of the `WEB_PUBLIC_STREAMS_ENABLED` Zulip server level
    setting. A server that has disabled this setting intends to not offer [web
    public channels](/help/public-access-option) to realms it hosts. (Zulip Cloud
    defaults to `true`; self-hosted servers default to `false`).
    
    Clients should use this to determine whether to offer UI for the
    realm-level setting for enabling web-public channels
    (`realm_enable_spectator_access`).
    
    **Changes**: New in Zulip 5.0 (feature level 110).
    """

    server_emoji_data_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The URL to a JSON file that describes which emoji names map to which
    emoji codes, for all Unicode emoji this Zulip server accepts.
    
    The data at the given URL is a JSON object with one property, `code_to_names`.
    The value of that property is a JSON object where each key is an
    [emoji code](/api/add-reaction#parameter-emoji_code) for an available
    Unicode emoji, and each value is the corresponding
    [emoji names](/api/add-reaction#parameter-emoji_name) for this emoji,
    with the canonical name for the emoji always appearing first.
    
    The HTTP response at that URL will have appropriate HTTP caching headers, such
    any HTTP implementation should get a cached version if emoji haven't changed
    since the last request.
    
    **Changes**: New in Zulip 6.0 (feature level 140).
    """

    server_jitsi_server_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The URL of the Jitsi server that the Zulip server is configured to use by
    default; the organization-level setting `realm_jitsi_server_url` takes
    precedence over this setting when both are set.
    
    **Changes**: New in Zulip 8.0 (feature level 212). Previously, this value
    was available as the now-deprecated `jitsi_server_url`.
    """

    server_can_summarize_topics: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`
    
    Whether topic summarization is enabled in the server or
    not depending upon whether `TOPIC_SUMMARIZATION_MODEL`
    is set or not.
    
    **Changes**: New in Zulip 10.0 (feature level 350).
    """

    event_queue_longpoll_timeout_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Recommended client-side HTTP request timeout for [`GET /events`](/api/get-events) calls.
    This is guaranteed to be somewhat greater than the heartbeat frequency. It is important
    that clients respect this parameter, so that increases in the heartbeat frequency do not
    break clients.
    
    **Changes**: New in Zulip 5.0 (feature level 74). Previously,
    this was hardcoded to 90 seconds, and clients should use that as a fallback
    value when interacting with servers where this field is not present.
    """

    realm_billing: typing.Optional[RegisterQueueResponseRealmBilling] = pydantic.Field(default=None)
    """
    Present if `realm_billing` is present in `fetch_event_types`.
    
    A dictionary containing billing information of the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 363).
    """

    realm_moderation_request_channel_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The ID of the private channel to which messages flagged by users for
    moderation are sent. Moderators can use this channel to review and
    act on reported content.
    
    Will be `-1` if moderation requests are disabled.
    
    Clients should check whether moderation requests are disabled to
    determine whether to present a "report message" feature in their UI
    within a given organization.
    
    **Changes**: New in Zulip 10.0 (feature level 331). Previously,
    no "report message" feature existed in Zulip.
    """

    realm_new_stream_announcements_stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The ID of the channel to which automated messages announcing the
    [creation of new channels][new-channel-announce] are sent.
    
    Will be `-1` if such automated messages are disabled.
    
    Since these automated messages are sent by the server, this field is
    primarily relevant to clients containing UI for changing it.
    
    [new-channel-announce]: /help/configure-automated-notices#new-channel-announcements
    
    **Changes**: In Zulip 9.0 (feature level 241), renamed 'realm_notifications_stream_id'
    to `realm_new_stream_announcements_stream_id`.
    """

    realm_signup_announcements_stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The ID of the channel to which automated messages announcing
    that [new users have joined the organization][new-user-announce] are sent.
    
    Will be `-1` if such automated messages are disabled.
    
    Since these automated messages are sent by the server, this field is
    primarily relevant to clients containing UI for changing it.
    
    [new-user-announce]: /help/configure-automated-notices#new-user-announcements
    
    **Changes**: In Zulip 9.0 (feature level 241), renamed
    'realm_signup_notifications_stream_id' to `realm_signup_announcements_stream_id`.
    """

    realm_zulip_update_announcements_stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    The ID of the channel to which automated messages announcing
    new features or other end-user updates about the Zulip software are sent.
    
    Will be `-1` if such automated messages are disabled.
    
    Since these automated messages are sent by the server, this field is
    primarily relevant to clients containing UI for changing it.
    
    **Changes**: New in Zulip 9.0 (feature level 242).
    """

    realm_empty_topic_display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Clients declaring the `empty_topic_name` client capability
    should use the value of `realm_empty_topic_display_name` to
    determine how to display the empty string topic.
    
    Clients not declaring the `empty_topic_name` client capability
    receive `realm_empty_topic_display_name` value as the topic name
    replacing empty string.
    
    **Changes**: New in Zulip 10.0 (feature level 334). Previously,
    the empty string was not a valid topic name.
    """

    realm_user_settings_defaults: typing.Optional[RegisterQueueResponseRealmUserSettingsDefaults] = pydantic.Field(
        default=None
    )
    """
    Present if `realm_user_settings_defaults` is present in `fetch_event_types`.
    
    A dictionary containing the default values of settings for new users.
    
    **Changes**: New in Zulip 5.0 (feature level 95).
    """

    realm_users: typing.Optional[typing.List[User]] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    A array of dictionaries where each entry describes a user
    whose account has not been deactivated. Note that unlike
    the usual User dictionary, this does not contain the `is_active`
    key, as all the users present in this array have active accounts.
    
    If the current user is a guest whose access to users is limited by a
    `can_access_all_users_group` policy, and the event queue was registered
    with the `user_list_incomplete` client capability, then users that the
    current user cannot access will not be included in this array. If the
    current user's access to a user is restricted but the client lacks this
    capability, then that inaccessible user will appear in the users array as
    an "Unknown user" object with the usual format but placeholder data whose
    only variable content is the user ID.
    
    See also `cross_realm_bots` and `realm_non_active_users`.
    
    **Changes**: Before Zulip 8.0 (feature level 232), the
    `user_list_incomplete` client capability did not exist, and so all
    clients whose access to a new user was prevented by
    `can_access_all_users_group` policy would receive a fake "Unknown
    user" event for such users.
    """

    realm_non_active_users: typing.Optional[typing.List[User]] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    A array of dictionaries where each entry describes a user
    whose account has been deactivated. Note that unlike
    the usual User dictionary this does not contain the `is_active`
    key as all the users present in this array have deactivated
    accounts.
    """

    avatar_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    The avatar data source type for the current user. Valid values are:
    
    - "G" = Hosted by Gravatar
    - "J" = Generated using Jdenticon
    - "U" = Uploaded by user
    
    **Changes**: The "J" value is new in Zulip 12.0 (feature level 466).
    The avatar data source type for the current user.
    """

    avatar_url_medium: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    The avatar URL for the current user at 500x500 resolution, appropriate
    for use in settings UI showing the user's avatar.
    """

    avatar_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    The URL of the avatar for the current user at 100x100
    resolution. See also `avatar_url_medium`.
    """

    can_create_streams: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    Whether the current user is allowed to create at least one type
    of channel with the organization's [channel creation
    policy](/help/configure-who-can-create-channels). Its value will
    always equal `can_create_public_streams || can_create_private_streams`.
    
    **Changes**: Deprecated in Zulip 5.0 (feature level 102), when
    the new `create_private_stream_policy` and
    `create_public_stream_policy` properties introduced the
    possibility that a user could only create one type of channel.
    
    This field will be removed in a future release.
    """

    can_create_public_streams: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    Whether the current user is allowed to create public channels with
    the organization's [channel creation policy](/help/configure-who-can-create-channels).
    
    **Changes**: New in Zulip 5.0 (feature level 102). In older
    versions, the deprecated `can_create_streams` property should be
    used to determine whether the user can create public channels.
    """

    can_create_private_streams: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    Whether the current user is allowed to create private channels with
    the organization's [channel creation policy](/help/configure-who-can-create-channels).
    
    **Changes**: New in Zulip 5.0 (feature level 102). In older
    versions, the deprecated `can_create_streams` property should be
    used to determine whether the user can create private channels.
    """

    can_create_web_public_streams: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    Whether the current user is allowed to create public channels with
    the organization's [channel creation policy](/help/configure-who-can-create-channels).
    
    Note that this will be false if the Zulip server does not have the
    `WEB_PUBLIC_STREAMS_ENABLED` setting enabled or if the organization has
    not enabled the `enable_spectator_access` realm setting.
    
    **Changes**: New in Zulip 5.0 (feature level 103).
    """

    can_subscribe_other_users: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    Whether the current user is allowed to subscribe other users to channels with
    the organization's [channels policy](/help/configure-who-can-invite-to-channels).
    """

    can_invite_others_to_realm: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    Whether the current user [is allowed to invite others][who-can-send-invitations]
    to the organization.
    
    **Changes**: New in Zulip 4.0 (feature level 51).
    
    [who-can-send-invitations]: /help/restrict-account-creation#change-who-can-send-invitations
    """

    is_admin: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    Whether the current user is at least an [organization administrator](/api/roles-and-permissions).
    """

    is_owner: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    Whether the current user is an [organization owner](/api/roles-and-permissions).
    
    **Changes**: New in Zulip 3.0 (feature level 11).
    """

    is_moderator: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    Whether the current user is at least an [organization moderator](/api/roles-and-permissions).
    
    **Changes**: Prior to Zulip 11.0 (feature level 380), this was only true
    for users whose role was exactly the moderator role.
    
    New in Zulip 4.0 (feature level 60).
    """

    is_guest: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    Whether the current user is a [guest user](/api/roles-and-permissions).
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    The unique ID for the current user.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    The Zulip API email address for the current user. See also
    `delivery_email`; these may be the same or different depending
    on the user's `email_address_visibility` policy.
    """

    delivery_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    The user's email address, appropriate for UI for changing
    the user's email address. See also `email`.
    """

    full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    The full name of the current user.
    """

    cross_realm_bots: typing.Optional[typing.List[RegisterQueueResponseCrossRealmBotsItem]] = pydantic.Field(
        default=None
    )
    """
    Present if `realm_user` is present in `fetch_event_types`.
    
    Array of dictionaries where each dictionary contains details of
    a single cross realm bot. Cross-realm bots are special system bot accounts
    like Notification Bot.
    
    Most clients will want to combine this with `realm_users` in many
    contexts.
    """

    server_report_message_types: typing.Optional[typing.List[RegisterQueueResponseServerReportMessageTypesItem]] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    A list of objects where each object describes a supported
    report type for the [message report](/help/report-a-message)
    feature.
    
    **Changes**: New in Zulip 12.0 (feature level 435).
    """

    server_supported_permission_settings: typing.Optional[RegisterQueueResponseServerSupportedPermissionSettings] = (
        pydantic.Field(default=None)
    )
    """
    Present if `realm` is present in `fetch_event_types`.
    
    Metadata detailing the valid values for permission settings that
    use [group-setting values](/api/group-setting-values). Clients
    should use these data as explained in the
    [main documentation](/api/group-setting-values#permitted-values)
    to determine what values to present as possible values for these
    settings in UI components.
    
    **Changes**: Before Zulip 10.0 (feature level 326), this part of
    the response had a documented-as-unstable format not suitable
    for general client use, and should be ignored.
    
    New in Zulip 8.0 (feature level 221).
    """

    max_bulk_new_subscription_messages: typing.Optional[float] = pydantic.Field(default=None)
    """
    Maximum number of new subscribers for which the server will
    respect the `send_new_subscription_messages` parameter when
    [adding subscribers to a channel](/api/subscribe#parameter-send_new_subscription_messages).
    
    **Changes**: New in Zulip 11.0 (feature level 397).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
