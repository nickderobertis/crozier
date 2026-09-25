

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.realm_authentication_method import RealmAuthenticationMethod
from .get_events_response_events_item_seventy_data_can_access_all_users_group import (
    GetEventsResponseEventsItemSeventyDataCanAccessAllUsersGroup,
)
from .get_events_response_events_item_seventy_data_can_add_custom_emoji_group import (
    GetEventsResponseEventsItemSeventyDataCanAddCustomEmojiGroup,
)
from .get_events_response_events_item_seventy_data_can_add_subscribers_group import (
    GetEventsResponseEventsItemSeventyDataCanAddSubscribersGroup,
)
from .get_events_response_events_item_seventy_data_can_create_bots_group import (
    GetEventsResponseEventsItemSeventyDataCanCreateBotsGroup,
)
from .get_events_response_events_item_seventy_data_can_create_groups import (
    GetEventsResponseEventsItemSeventyDataCanCreateGroups,
)
from .get_events_response_events_item_seventy_data_can_create_private_channel_group import (
    GetEventsResponseEventsItemSeventyDataCanCreatePrivateChannelGroup,
)
from .get_events_response_events_item_seventy_data_can_create_public_channel_group import (
    GetEventsResponseEventsItemSeventyDataCanCreatePublicChannelGroup,
)
from .get_events_response_events_item_seventy_data_can_create_web_public_channel_group import (
    GetEventsResponseEventsItemSeventyDataCanCreateWebPublicChannelGroup,
)
from .get_events_response_events_item_seventy_data_can_create_write_only_bots_group import (
    GetEventsResponseEventsItemSeventyDataCanCreateWriteOnlyBotsGroup,
)
from .get_events_response_events_item_seventy_data_can_delete_any_message_group import (
    GetEventsResponseEventsItemSeventyDataCanDeleteAnyMessageGroup,
)
from .get_events_response_events_item_seventy_data_can_delete_own_message_group import (
    GetEventsResponseEventsItemSeventyDataCanDeleteOwnMessageGroup,
)
from .get_events_response_events_item_seventy_data_can_invite_users_group import (
    GetEventsResponseEventsItemSeventyDataCanInviteUsersGroup,
)
from .get_events_response_events_item_seventy_data_can_manage_all_groups import (
    GetEventsResponseEventsItemSeventyDataCanManageAllGroups,
)
from .get_events_response_events_item_seventy_data_can_manage_billing_group import (
    GetEventsResponseEventsItemSeventyDataCanManageBillingGroup,
)
from .get_events_response_events_item_seventy_data_can_mention_many_users_group import (
    GetEventsResponseEventsItemSeventyDataCanMentionManyUsersGroup,
)
from .get_events_response_events_item_seventy_data_can_move_messages_between_channels_group import (
    GetEventsResponseEventsItemSeventyDataCanMoveMessagesBetweenChannelsGroup,
)
from .get_events_response_events_item_seventy_data_can_move_messages_between_topics_group import (
    GetEventsResponseEventsItemSeventyDataCanMoveMessagesBetweenTopicsGroup,
)
from .get_events_response_events_item_seventy_data_can_resolve_topics_group import (
    GetEventsResponseEventsItemSeventyDataCanResolveTopicsGroup,
)
from .get_events_response_events_item_seventy_data_can_set_delete_message_policy_group import (
    GetEventsResponseEventsItemSeventyDataCanSetDeleteMessagePolicyGroup,
)
from .get_events_response_events_item_seventy_data_can_set_topics_policy_group import (
    GetEventsResponseEventsItemSeventyDataCanSetTopicsPolicyGroup,
)
from .get_events_response_events_item_seventy_data_can_summarize_topics_group import (
    GetEventsResponseEventsItemSeventyDataCanSummarizeTopicsGroup,
)
from .get_events_response_events_item_seventy_data_create_multiuse_invite_group import (
    GetEventsResponseEventsItemSeventyDataCreateMultiuseInviteGroup,
)
from .get_events_response_events_item_seventy_data_direct_message_initiator_group import (
    GetEventsResponseEventsItemSeventyDataDirectMessageInitiatorGroup,
)
from .get_events_response_events_item_seventy_data_direct_message_permission_group import (
    GetEventsResponseEventsItemSeventyDataDirectMessagePermissionGroup,
)
from .get_events_response_events_item_seventy_data_topics_policy import (
    GetEventsResponseEventsItemSeventyDataTopicsPolicy,
)
from .get_events_response_events_item_seventy_data_workplace_users_group import (
    GetEventsResponseEventsItemSeventyDataWorkplaceUsersGroup,
)


class GetEventsResponseEventsItemSeventyData(UniversalBaseModel):
    """
    An object containing the properties that have changed.

    **Changes**: In Zulip 10.0 (feature level 316), `edit_topic_policy`
    property was removed and replaced by `can_move_messages_between_topics_group`
    realm setting.

    In Zulip 7.0 (feature level 183), the
    `community_topic_editing_limit_seconds` property was removed.
    It was documented as potentially returned as a changed property
    in this event, but in fact it was only ever returned in the
    [`POST /register`](/api/register-queue) response.

    Before Zulip 6.0 (feature level 150), on changing any of
    `allow_message_editing`, `message_content_edit_limit_seconds`, or
    `edit_topic_policy` settings, this object included all the three settings
    irrespective of which of these settings were changed. Now, a separate event
    is sent for each changed setting.
    """

    allow_message_editing: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this organization's [message edit policy][config-message-editing]
    allows editing the content of messages.
    
    See [`PATCH /messages/{message_id}`](/api/update-message) for details and
    history of how message editing permissions work.
    
    [config-message-editing]: /help/restrict-message-editing-and-deletion
    """

    authentication_methods: typing.Optional[typing.Dict[str, RealmAuthenticationMethod]] = pydantic.Field(default=None)
    """
    Dictionary of authentication method keys mapped to dictionaries that
    describe the properties of the named authentication method for the
    organization - its enabled status and availability for use by the
    organization.
    
    Clients should use this to implement server-settings UI to change which
    methods are enabled for the organization. For authentication UI itself,
    clients should use the pre-authentication metadata returned by
    [`GET /server_settings`](/api/get-server-settings).
    
    **Changes**: In Zulip 9.0 (feature level 243), the values in this
    dictionary were changed. Previously, the values were a simple boolean
    indicating whether the backend is enabled or not.
    """

    can_access_all_users_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanAccessAllUsersGroup] = (
        pydantic.Field(default=None)
    )
    """
    A [group-setting value](/api/group-setting-values) defining the
    set of users who are allowed to access all users in the
    organization.
    
    **Changes**: Prior to Zulip 10.0 (feature level 314), this value used
    to be of type integer and did not accept anonymous user groups.
    
    New in Zulip 8.0 (feature level 225).
    """

    can_create_groups: typing.Optional[GetEventsResponseEventsItemSeventyDataCanCreateGroups] = pydantic.Field(
        default=None
    )
    """
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create user
    groups in this organization.
    
    **Changes**: New in Zulip 10.0 (feature level 299). Previously
    `user_group_edit_policy` field used to control the permission
    to create user groups.
    """

    can_create_bots_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanCreateBotsGroup] = pydantic.Field(
        default=None
    )
    """
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create all types of bot users
    in the organization. See also `can_create_write_only_bots_group`.
    
    **Changes**: New in Zulip 10.0 (feature level 344). Previously, this
    permission was controlled by the enum `bot_creation_policy`. Values
    were 1=Members, 2=Generic bots limited to administrators, 3=Administrators.
    """

    can_create_write_only_bots_group: typing.Optional[
        GetEventsResponseEventsItemSeventyDataCanCreateWriteOnlyBotsGroup
    ] = pydantic.Field(default=None)
    """
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create bot users that
    can only send messages in the organization, i.e. incoming webhooks,
    in addition to the users who are present in `can_create_bots_group`.
    
    **Changes**: New in Zulip 10.0 (feature level 344). Previously, this
    permission was controlled by the enum `bot_creation_policy`. Values
    were 1=Members, 2=Generic bots limited to administrators, 3=Administrators.
    """

    can_create_public_channel_group: typing.Optional[
        GetEventsResponseEventsItemSeventyDataCanCreatePublicChannelGroup
    ] = pydantic.Field(default=None)
    """
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create public
    channels in this organization.
    
    **Changes**: New in Zulip 9.0 (feature level 264). Previously
    `realm_create_public_stream_policy` field used to control the
    permission to create public channels.
    """

    can_create_private_channel_group: typing.Optional[
        GetEventsResponseEventsItemSeventyDataCanCreatePrivateChannelGroup
    ] = pydantic.Field(default=None)
    """
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create private
    channels in this organization.
    
    **Changes**: New in Zulip 9.0 (feature level 266). Previously
    `realm_create_private_stream_policy` field used to control the
    permission to create private channels.
    """

    can_create_web_public_channel_group: typing.Optional[
        GetEventsResponseEventsItemSeventyDataCanCreateWebPublicChannelGroup
    ] = pydantic.Field(default=None)
    """
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to create web-public
    channels in this organization.
    
    **Changes**: New in Zulip 10.0 (feature level 280). Previously
    `realm_create_web_public_stream_policy` field used to control
    the permission to create web-public channels.
    """

    can_add_custom_emoji_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanAddCustomEmojiGroup] = (
        pydantic.Field(default=None)
    )
    """
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to add custom emoji in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 307). Previously, this
    permission was controlled by the enum `add_custom_emoji_policy`. Values
    were 1=Members, 2=Admins, 3=Full members, 4=Moderators.
    
    Before Zulip 5.0 (feature level 85), the `realm_add_emoji_by_admins_only`
    boolean setting controlled this permission; `true` corresponded to `Admins`,
    and `false` to `Everyone`.
    """

    can_add_subscribers_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanAddSubscribersGroup] = (
        pydantic.Field(default=None)
    )
    """
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to add subscribers to channels in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 341). Previously, this
    permission was controlled by the enum `invite_to_stream_policy`. Values
    were 1=Members, 2=Admins, 3=Full members, 4=Moderators.
    """

    can_delete_any_message_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanDeleteAnyMessageGroup] = (
        pydantic.Field(default=None)
    )
    """
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to delete any message in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 281). Previously, this
    permission was limited to administrators only and was uneditable.
    """

    can_delete_own_message_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanDeleteOwnMessageGroup] = (
        pydantic.Field(default=None)
    )
    """
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

    can_set_delete_message_policy_group: typing.Optional[
        GetEventsResponseEventsItemSeventyDataCanSetDeleteMessagePolicyGroup
    ] = pydantic.Field(default=None)
    """
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to change per-channel `can_delete_any_message_group`
    and `can_delete_own_message_group` permission settings. Note that the user
    must be a member of both this group and the `can_administer_channel_group`
    of the channel whose message delete settings they want to change.
    
    Organization administrators can always change these settings of
    every channel.
    
    **Changes**: New in Zulip 11.0 (feature level 407).
    """

    can_set_topics_policy_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanSetTopicsPolicyGroup] = (
        pydantic.Field(default=None)
    )
    """
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to change per-channel `topics_policy` setting. Note that
    the user must be a member of both this group and the `can_administer_channel_group`
    of the channel whose `topics_policy` they want to change.
    
    Organization administrators can always change the `topics_policy` setting of
    every channel.
    
    **Changes**: New in Zulip 11.0 (feature level 392).
    """

    can_invite_users_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanInviteUsersGroup] = pydantic.Field(
        default=None
    )
    """
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

    can_mention_many_users_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanMentionManyUsersGroup] = (
        pydantic.Field(default=None)
    )
    """
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to use wildcard mentions in large channels.
    
    All users will receive a warning/reminder when using mentions in large
    channels, even when permitted to do so.
    
    **Changes**: New in Zulip 10.0 (feature level 352). Previously, this
    permission was controlled by the enum `wildcard_mention_policy`.
    """

    can_move_messages_between_channels_group: typing.Optional[
        GetEventsResponseEventsItemSeventyDataCanMoveMessagesBetweenChannelsGroup
    ] = pydantic.Field(default=None)
    """
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to move messages from one channel to another
    in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 310). Previously, this
    permission was controlled by the enum `move_messages_between_streams_policy`.
    Values were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 6=Nobody.
    
    In Zulip 7.0 (feature level 159), `Nobody` was added as an option to
    `move_messages_between_streams_policy` enum.
    """

    can_move_messages_between_topics_group: typing.Optional[
        GetEventsResponseEventsItemSeventyDataCanMoveMessagesBetweenTopicsGroup
    ] = pydantic.Field(default=None)
    """
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to move messages from one topic to another
    within a channel in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 316). Previously, this
    permission was controlled by the enum `edit_topic_policy`. Values were
    1=Members, 2=Admins, 3=Full members, 4=Moderators, 5=Everyone, 6=Nobody.
    
    In Zulip 7.0 (feature level 159), `Nobody` was added as an option to
    `edit_topic_policy` enum.
    """

    can_resolve_topics_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanResolveTopicsGroup] = (
        pydantic.Field(default=None)
    )
    """
    A [group-setting value](/api/group-setting-values) defining
    the set of users who have permission to [resolve topics](/help/resolve-a-topic)
    in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 367). Previously, permission to
    resolve topics was controlled by the more general
    can_move_messages_between_topics_group permission for moving messages.
    """

    can_manage_all_groups: typing.Optional[GetEventsResponseEventsItemSeventyDataCanManageAllGroups] = pydantic.Field(
        default=None
    )
    """
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

    can_manage_billing_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanManageBillingGroup] = (
        pydantic.Field(default=None)
    )
    """
    A [group-setting value](/api/group-setting-values) defining the set of
    users who have permission to manage plans and billing in the organization.
    
    **Changes**: New in Zulip 10.0 (feature level 363). Previously, only owners
    and users with `is_billing_admin` property set to `true` were allowed to
    manage plans and billing.
    """

    can_summarize_topics_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCanSummarizeTopicsGroup] = (
        pydantic.Field(default=None)
    )
    """
    A [group-setting value](/api/group-setting-values) defining the
    set of users who are allowed to use AI summarization.
    
    **Changes**: New in Zulip 10.0 (feature level 350).
    """

    create_multiuse_invite_group: typing.Optional[GetEventsResponseEventsItemSeventyDataCreateMultiuseInviteGroup] = (
        pydantic.Field(default=None)
    )
    """
    A [group-setting value](/api/group-setting-values) defining the
    set of users who are allowed to create [reusable invitation
    links](/help/invite-new-users#create-a-reusable-invitation-link)
    to the organization.
    
    **Changes**: Prior to Zulip 10.0 (feature level 314), this value used
    to be of type integer and did not accept anonymous user groups.
    
    New in Zulip 8.0 (feature level 209).
    """

    default_avatar_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The avatar data source type for new users.
    
    - "G" = Hosted by Gravatar
    - "J" = Generated using Jdenticon
    
    Note that "U" is not a supported value here, since there is
    no such thing as a "default" user-uploaded avatar.
    
    **Changes**: New in Zulip 12.0 (feature level 456).
    """

    default_code_block_language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The default pygments language code to be used for code blocks in this
    organization. If an empty string, no default has been set.
    
    **Changes**: Prior to Zulip 8.0 (feature level 195), a server bug meant
    that both `null` and an empty string could represent that no default was
    set for this realm setting in the [`POST /register`](/api/register-queue)
    response. The documentation for both that endpoint and this event
    incorrectly stated that the only representation for no default language
    was `null`. This event in fact uses the empty string to indicate that no
    default has been set in all server versions.
    """

    default_language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The default language for the organization.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the organization, used on login and registration pages.
    """

    digest_emails_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the organization has enabled [weekly digest emails](/help/digest-emails).
    """

    digest_weekday: typing.Optional[int] = pydantic.Field(default=None)
    """
    The day of the week when the organization will send
    its weekly digest email to inactive users.
    """

    direct_message_initiator_group: typing.Optional[
        GetEventsResponseEventsItemSeventyDataDirectMessageInitiatorGroup
    ] = pydantic.Field(default=None)
    """
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

    direct_message_permission_group: typing.Optional[
        GetEventsResponseEventsItemSeventyDataDirectMessagePermissionGroup
    ] = pydantic.Field(default=None)
    """
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

    disallow_disposable_email_addresses: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the organization disallows disposable email
    addresses.
    """

    email_changes_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether users are allowed to change their own email address in this
    organization. This is typically disabled for organizations that
    synchronize accounts from LDAP or a similar corporate database.
    """

    enable_read_receipts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether read receipts is enabled in the organization or not.
    
    If disabled, read receipt data will be unavailable to clients, regardless
    of individual users' personal read receipt settings. See also the
    `send_read_receipts` setting within `realm_user_settings_defaults`.
    
    **Changes**: New in Zulip 6.0 (feature level 137).
    """

    emails_restricted_to_domains: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [new users joining](/help/restrict-account-creation#configuring-email-domain-restrictions)
    this organization are required to have an email
    address in one of the `realm_domains` configured for the organization.
    """

    enable_guest_user_dm_warning: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether clients should show a warning when a user is composing
    a DM to a guest user in this organization.
    
    **Changes**: New in Zulip 10.0 (feature level 348).
    """

    enable_guest_user_indicator: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether clients should display "(guest)" after the names of
    guest users to prominently highlight their status.
    
    **Changes**: New in Zulip 8.0 (feature level 216).
    """

    enable_spectator_access: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether web-public channels are enabled in this organization.
    
    Can only be enabled if the `WEB_PUBLIC_STREAMS_ENABLED`
    [server setting][server-settings] is enabled on the Zulip
    server. See also the `can_create_web_public_channel_group`
    realm setting.
    
    [server-settings]: https://zulip.readthedocs.io/en/stable/production/settings.html
    
    **Changes**: New in Zulip 5.0 (feature level 109).
    """

    gif_rating_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum rating of the GIFs that will be retrieved by the
    GIPHY and Tenor integrations in this organization.
    
    **Changes**: Before Zulip 12.0 (feature level 453),
    this was called `giphy_rating`.
    
    Before Zulip 12.0 (feature level 442), this was only used
    for the Giphy integration.
    
    New in Zulip 4.0 (feature level 55).
    """

    icon_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    String indicating whether the organization's
    [profile icon](/help/create-your-organization-profile) was uploaded
    by a user or is the default. Useful for UI allowing editing the organization's icon.
    
    - "G" means generated by Gravatar (the default).
    - "U" means uploaded by an organization administrator.
    """

    icon_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the organization's [profile icon](/help/create-your-organization-profile).
    """

    media_preview_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The organization's policy for the size of image and video
    thumbnails in messages, expressed as a percentage of the
    default height. Currently, only certain values are permitted.
    
    - `100`: 100% height (the default).
    - `150`: 150% height.
    - `200`: 200% height.
    
    **Changes**: New in Zulip 12.0 (feature level 469).
    """

    inline_image_preview: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this organization has been configured to enable
    [previews of linked images](/help/image-video-and-website-previews).
    """

    inline_url_embed_preview: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this organization has been configured to enable
    [previews of linked websites](/help/image-video-and-website-previews).
    """

    invite_required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether an invitation is required to join this organization.
    """

    jitsi_server_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the custom Jitsi Meet server configured in this organization's
    settings.
    
    `null`, the default, means that the organization is using the server-level
    configuration, `server_jitsi_server_url`.
    
    **Changes**: New in Zulip 8.0 (feature level 212). Previously, this was only
    available as a server-level configuration, and required a server restart to
    change.
    """

    logo_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    String indicating whether the organization's
    [profile wide logo](/help/create-your-organization-profile) was uploaded
    by a user or is the default. Useful for UI allowing editing the
    organization's wide logo.
    
    - "D" means the logo is the default Zulip logo.
    - "U" means uploaded by an organization administrator.
    """

    logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the organization's wide logo configured in the
    [organization profile](/help/create-your-organization-profile).
    """

    topics_policy: typing.Optional[GetEventsResponseEventsItemSeventyDataTopicsPolicy] = pydantic.Field(default=None)
    """
    The organization's default policy for sending channel messages to the
    [empty "general chat" topic](/help/general-chat-topic).
    
    - `"allow_empty_topic"`: Channel messages can be sent to the empty topic.
    - `"disable_empty_topic"`: Channel messages cannot be sent to the empty topic.
    
    **Changes**: New in Zulip 11.0 (feature level 392). Previously, this was
    controlled by the boolean realm `mandatory_topics` setting, which is now
    deprecated.
    """

    mandatory_topics: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [topics are required](/help/require-topics) for messages in this
    organization.
    
    **Changes**: Deprecated in Zulip 11.0 (feature level 392). This is now
    controlled by the realm `topics_policy` setting.
    """

    max_file_upload_size_mib: typing.Optional[int] = pydantic.Field(default=None)
    """
    The new maximum file size that can be uploaded to this Zulip organization.
    
    **Changes**: New in Zulip 10.0 (feature level 306). Previously, this field of
    the core state did not support being updated via the events system, as it was
    typically hardcoded for a given Zulip installation.
    """

    message_content_allowed_in_email_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether notification emails in this organization are allowed to
    contain Zulip the message content, or simply indicate that a new
    message was sent.
    """

    message_content_delete_limit_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Messages sent more than this many seconds ago cannot be deleted
    with this organization's
    [message deletion policy](/help/restrict-message-editing-and-deletion).
    
    Will not be 0. A `null` value means no limit: messages can be deleted
    regardless of how long ago they were sent.
    
    **Changes**: No limit was represented using the
    special value `0` before Zulip 5.0 (feature level 100).
    """

    message_content_edit_limit_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
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

    message_edit_history_visibility_policy: typing.Optional[str] = pydantic.Field(default=None)
    """
    Which type of message edit history is configured to allow users to
    access [message edit history](/help/view-a-messages-edit-history).
    
    - "all" = All edit history is visible.
    - "moves" = Only moves are visible.
    - "none" = No edit history is visible.
    
    **Changes**: New in Zulip 10.0 (feature level 358), replacing the previous
    `allow_edit_history` boolean setting; `true` corresponds to `all`,
    and `false` to `none`.
    """

    moderation_request_channel_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the private channel to which messages flagged by users for
    moderation are sent. Moderators can use this channel to review and
    act on reported content.
    
    Will be `-1` if moderation requests are disabled.
    
    Clients should check whether moderation requests are disabled to
    determine whether to present a "report message" feature in their UI
    within a given organization.
    
    **Changes**: New in Zulip 10.0 (feature level 331). Previously,
    no "report message" features existed in Zulip.
    """

    move_messages_within_stream_limit_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
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

    move_messages_between_streams_limit_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
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

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the organization, used in login pages etc.
    """

    name_changes_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether users are
    [allowed to change](/help/restrict-name-and-email-changes) their name
    via the Zulip UI in this organization. Typically disabled
    in organizations syncing this type of account information from
    an external user database like LDAP.
    """

    night_logo_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    String indicating whether the organization's dark theme
    [profile wide logo](/help/create-your-organization-profile) was uploaded
    by a user or is the default. Useful for UI allowing editing the
    organization's wide logo.
    
    - "D" means the logo is the default Zulip logo.
    - "U" means uploaded by an organization administrator.
    """

    night_logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the organization's dark theme wide-format logo configured in the
    [organization profile](/help/create-your-organization-profile).
    """

    new_stream_announcements_stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the channel to which automated messages announcing the
    [creation of new channels][new-channel-announce] are sent.
    
    Will be `-1` if such automated messages are disabled.
    
    Since these automated messages are sent by the server, this field is
    primarily relevant to clients containing UI for changing it.
    
    [new-channel-announce]: /help/configure-automated-notices#new-channel-announcements
    
    **Changes**: In Zulip 9.0 (feature level 241), renamed `notifications_stream_id`
    to `new_stream_announcements_stream_id`.
    """

    org_type: typing.Optional[int] = pydantic.Field(default=None)
    """
    The [organization type](/help/organization-type)
    for the realm.
    
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

    plan_type: typing.Optional[int] = pydantic.Field(default=None)
    """
    The plan type of the organization.
    
    - 1 = Self-hosted organization (SELF_HOSTED)
    - 2 = Zulip Cloud free plan (LIMITED)
    - 3 = Zulip Cloud Standard plan (STANDARD)
    - 4 = Zulip Cloud Standard plan, sponsored for free (STANDARD_FREE)
    """

    presence_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether online presence of other users is shown in this
    organization.
    """

    push_notifications_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether push notifications are enabled for this organization. Typically
    `true` for Zulip Cloud and self-hosted realms that have a valid
    registration for the [Mobile push notifications
    service](https://zulip.readthedocs.io/en/latest/production/mobile-push-notifications.html),
    and `false` for self-hosted servers that do not.
    
    **Changes**: New in Zulip 8.0 (feature level 231).
    Previously, this value was never updated via events.
    """

    push_notifications_enabled_end_timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    If the server expects the realm's push notifications access to end at a
    definite time in the future, the time at which this is expected to happen.
    Mobile clients should use this field to display warnings to users when the
    indicated timestamp is near.
    
    **Changes**: New in Zulip 8.0 (feature level 231).
    """

    rendered_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Note: Only present if the changed property was `description`.
    
    The organization description rendered as HTML, intended to
    be used when displaying the organization description in a UI.
    
    One should use the standard Zulip rendered_markdown CSS when
    displaying this content so that emoji, LaTeX, and other syntax
    work correctly. And any client-side security logic for
    user-generated message content should be applied when displaying
    this HTML as though it were the body of a Zulip message.
    
    **Changes**: New in Zulip 12.0 (feature level 464). Previously
    in feature levels 462-463, an `update` event had been sent
    when updating the realm's `description`.
    """

    require_e2ee_push_notifications: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this realm is configured to disallow sending mobile
    push notifications through the legacy mobile push
    notifications APIs. The new API uses end-to-end encryption
    to protect message content and metadata from being
    accessible to the push bouncer service, APNs, and FCM.
    Clients that support the new E2EE API will use it
    automatically regardless of this setting.
    
    If `true`, legacy mobile push notifications will not be
    sent. Only updated version of clients (which support E2EE
    push notifications) will receive push notifications.
    
    **Changes**: In Zulip 12.1 (feature levels 500-501, and 504+), this
    setting now completely disables legacy push notifications
    rather than sending them with redacted content.
    
    New in Zulip 11.0 (feature level 409). Previously,
    this behavior was available only via the
    `PUSH_NOTIFICATION_REDACT_CONTENT` global server setting.
    """

    require_unique_names: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the organization is configured to require users to have
    unique full names. If true, the server will reject attempts to create a
    new user, or change the name of an existing user, where doing so would
    lead to two users whose names are identical modulo case and unicode
    normalization.
    
    **Changes**: New in Zulip 9.0 (feature level 246). Previously, the Zulip
    server could not be configured to enforce unique names.
    """

    send_channel_events_messages: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether channel event messages are sent in this organization.
    
    **Changes**: New in Zulip 12.0 (feature level 434). Previously,
    channel events were sent unconditionally.
    """

    send_welcome_emails: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this organization is configured to send the standard Zulip
    [welcome emails](/help/disable-welcome-emails) to new users joining the organization.
    """

    signup_announcements_stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the channel to which automated messages announcing
    that [new users have joined the organization][new-user-announce] are sent.
    
    Will be `-1` if such automated messages are disabled.
    
    Since these automated messages are sent by the server, this field is
    primarily relevant to clients containing UI for changing it.
    
    [new-user-announce]: /help/configure-automated-notices#new-user-announcements
    
    **Changes**: In Zulip 9.0 (feature level 241), renamed
    `signup_notifications_stream_id` to `signup_announcements_stream_id`.
    """

    upload_quota_mib: typing.Optional[int] = pydantic.Field(default=None)
    """
    The new upload quota for the Zulip organization.
    
    If `null`, there is no limit.
    
    **Changes**: New in Zulip 10.0 (feature level 306). Previously,
    this was present changed via an `upload_quota` field in `extra_data` property
    of [realm/update](#realm-update) event format for `plan_type` events.
    """

    video_chat_provider: typing.Optional[int] = pydantic.Field(default=None)
    """
    The configured [video call provider](/help/configure-call-provider) for the
    organization.
    
    - 0 = None
    - 1 = Jitsi Meet
    - 3 = Zoom (User OAuth integration)
    - 4 = BigBlueButton
    - 5 = Zoom (Server to Server OAuth integration)
    - 6 = Constructor Groups
    - 7 = Nextcloud Talk
    - 8 = Webex (User OAuth integration)
    
    Note that only one of the [Zoom integrations][zoom-video-calls] can
    be configured on a Zulip server.
    
    **Changes**: In Zulip 12.0 (feature level 493),
    added the Webex OAuth option.
    
    In Zulip 12.0 (feature level 465), added the
    Nextcloud Talk option.
    
    In Zulip 12.0 (feature level 460), added the
    Constructor Groups option.
    
    In Zulip 10.0 (feature level 353), added the Zoom Server
    to Server OAuth option.
    
    In Zulip 3.0 (feature level 1), added the None option
    to disable video call UI.
    
    [zoom-video-calls]: https://zulip.readthedocs.io/en/latest/production/video-calls.html#zoom
    """

    waiting_period_threshold: typing.Optional[int] = pydantic.Field(default=None)
    """
    Members whose accounts have been created at least this many days ago
    will be treated as [full members][calc-full-member]
    for the purpose of settings that restrict access to new members.
    
    [calc-full-member]: /api/roles-and-permissions#determining-if-a-user-is-a-full-member
    """

    want_advertise_in_communities_directory: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the organization has given permission to be advertised in the
    Zulip [communities directory](/help/communities-directory).
    
    **Changes**: New in Zulip 6.0 (feature level 129).
    """

    welcome_message_custom_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    This organization's configured custom message for Welcome Bot
    to send to new user accounts, in Zulip Markdown format.
    
    Maximum length is 8000 Unicode code points.
    
    **Changes**: New in Zulip 11.0 (feature level 416).
    """

    workplace_users_group: typing.Optional[GetEventsResponseEventsItemSeventyDataWorkplaceUsersGroup] = pydantic.Field(
        default=None
    )
    """
    A [group-setting value](/api/group-setting-values) defining the set of
    users who will be considered as workplace users for billing.
    
    **Changes**: New in Zulip 12.0 (feature level 477).
    """

    zulip_update_announcements_stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the channel to which automated messages announcing
    new features or other end-user updates about the Zulip software are sent.
    
    Will be `-1` if such automated messages are disabled.
    
    Since these automated messages are sent by the server, this field is
    primarily relevant to clients containing UI for changing it.
    
    **Changes**: New in Zulip 9.0 (feature level 242).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
