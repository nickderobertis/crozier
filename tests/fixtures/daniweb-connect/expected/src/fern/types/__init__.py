



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .api_pagination import ApiPagination
    from .app import App
    from .app_about import AppAbout
    from .app_about_website import AppAboutWebsite
    from .app_legal import AppLegal
    from .bubble import Bubble
    from .bubble_about import BubbleAbout
    from .conversation import Conversation
    from .conversation_first_message import ConversationFirstMessage
    from .endpoint_delete_groups_id_memberships import EndpointDeleteGroupsIdMemberships
    from .endpoint_delete_groups_messages_id import EndpointDeleteGroupsMessagesId
    from .endpoint_delete_positions_id import EndpointDeletePositionsId
    from .endpoint_delete_webhooks_id import EndpointDeleteWebhooksId
    from .endpoint_get_apps import EndpointGetApps
    from .endpoint_get_apps_id import EndpointGetAppsId
    from .endpoint_get_audiences import EndpointGetAudiences
    from .endpoint_get_audiences_id import EndpointGetAudiencesId
    from .endpoint_get_autocompletes import EndpointGetAutocompletes
    from .endpoint_get_autocompletes_data import EndpointGetAutocompletesData
    from .endpoint_get_conversations_id import EndpointGetConversationsId
    from .endpoint_get_conversations_id_messages import EndpointGetConversationsIdMessages
    from .endpoint_get_conversations_id_statuses import EndpointGetConversationsIdStatuses
    from .endpoint_get_conversations_id_statuses_data_item import EndpointGetConversationsIdStatusesDataItem
    from .endpoint_get_conversations_id_statuses_data_item_bubbled import (
        EndpointGetConversationsIdStatusesDataItemBubbled,
    )
    from .endpoint_get_conversations_statuses import EndpointGetConversationsStatuses
    from .endpoint_get_conversations_statuses_data_item import EndpointGetConversationsStatusesDataItem
    from .endpoint_get_conversations_statuses_data_item_bubbled import EndpointGetConversationsStatusesDataItemBubbled
    from .endpoint_get_groups import EndpointGetGroups
    from .endpoint_get_groups_id import EndpointGetGroupsId
    from .endpoint_get_groups_id_memberships import EndpointGetGroupsIdMemberships
    from .endpoint_get_groups_id_memberships_data_item import EndpointGetGroupsIdMembershipsDataItem
    from .endpoint_get_groups_id_memberships_data_item_privileges import (
        EndpointGetGroupsIdMembershipsDataItemPrivileges,
    )
    from .endpoint_get_groups_id_messages import EndpointGetGroupsIdMessages
    from .endpoint_get_groups_id_statuses import EndpointGetGroupsIdStatuses
    from .endpoint_get_groups_id_statuses_data_item import EndpointGetGroupsIdStatusesDataItem
    from .endpoint_get_groups_messages_id import EndpointGetGroupsMessagesId
    from .endpoint_get_groups_messages_id_metadata import EndpointGetGroupsMessagesIdMetadata
    from .endpoint_get_groups_messages_id_metadata_collections import EndpointGetGroupsMessagesIdMetadataCollections
    from .endpoint_get_groups_statuses import EndpointGetGroupsStatuses
    from .endpoint_get_groups_statuses_data_item import EndpointGetGroupsStatusesDataItem
    from .endpoint_get_industries import EndpointGetIndustries
    from .endpoint_get_markdown_emoticons import EndpointGetMarkdownEmoticons
    from .endpoint_get_markdown_emoticons_data_item import EndpointGetMarkdownEmoticonsDataItem
    from .endpoint_get_messages_id import EndpointGetMessagesId
    from .endpoint_get_messages_id_metadata import EndpointGetMessagesIdMetadata
    from .endpoint_get_messages_id_metadata_collections import EndpointGetMessagesIdMetadataCollections
    from .endpoint_get_users import EndpointGetUsers
    from .endpoint_get_users_id import EndpointGetUsersId
    from .endpoint_get_users_id_groups import EndpointGetUsersIdGroups
    from .endpoint_get_users_id_groups_messages import EndpointGetUsersIdGroupsMessages
    from .endpoint_get_users_id_metadata import EndpointGetUsersIdMetadata
    from .endpoint_get_users_id_metadata_collections import EndpointGetUsersIdMetadataCollections
    from .endpoint_get_users_id_positions import EndpointGetUsersIdPositions
    from .endpoint_get_users_id_synergies import EndpointGetUsersIdSynergies
    from .endpoint_get_users_id_synergies_data_item import EndpointGetUsersIdSynergiesDataItem
    from .endpoint_get_users_id_synergies_data_item_additional import EndpointGetUsersIdSynergiesDataItemAdditional
    from .endpoint_get_users_id_synergies_data_item_match import EndpointGetUsersIdSynergiesDataItemMatch
    from .endpoint_get_users_id_synergies_data_item_match_distance_away import (
        EndpointGetUsersIdSynergiesDataItemMatchDistanceAway,
    )
    from .endpoint_get_users_id_synergies_data_item_match_industry import (
        EndpointGetUsersIdSynergiesDataItemMatchIndustry,
    )
    from .endpoint_get_users_id_synergies_data_item_match_mutual_connections import (
        EndpointGetUsersIdSynergiesDataItemMatchMutualConnections,
    )
    from .endpoint_get_users_id_synergies_data_item_meet import EndpointGetUsersIdSynergiesDataItemMeet
    from .endpoint_get_users_id_synergies_data_item_meet_payment import EndpointGetUsersIdSynergiesDataItemMeetPayment
    from .endpoint_get_users_id_synergies_data_item_meet_payment_paypal import (
        EndpointGetUsersIdSynergiesDataItemMeetPaymentPaypal,
    )
    from .endpoint_get_users_id_synergies_data_item_relationship import EndpointGetUsersIdSynergiesDataItemRelationship
    from .endpoint_get_users_nearby import EndpointGetUsersNearby
    from .endpoint_get_users_nearby_data_item import EndpointGetUsersNearbyDataItem
    from .endpoint_get_users_nearby_data_item_distance_away import EndpointGetUsersNearbyDataItemDistanceAway
    from .endpoint_get_webhooks import EndpointGetWebhooks
    from .endpoint_patch_conversations_id_statuses import EndpointPatchConversationsIdStatuses
    from .endpoint_patch_conversations_id_statuses_data import EndpointPatchConversationsIdStatusesData
    from .endpoint_patch_groups_id import EndpointPatchGroupsId
    from .endpoint_patch_groups_id_memberships import EndpointPatchGroupsIdMemberships
    from .endpoint_patch_groups_id_memberships_data_item import EndpointPatchGroupsIdMembershipsDataItem
    from .endpoint_patch_groups_id_memberships_data_item_privileges import (
        EndpointPatchGroupsIdMembershipsDataItemPrivileges,
    )
    from .endpoint_patch_positions_id import EndpointPatchPositionsId
    from .endpoint_patch_users import EndpointPatchUsers
    from .endpoint_patch_users_id_synergies import EndpointPatchUsersIdSynergies
    from .endpoint_patch_users_id_synergies_data import EndpointPatchUsersIdSynergiesData
    from .endpoint_patch_users_id_synergies_data_relationship import EndpointPatchUsersIdSynergiesDataRelationship
    from .endpoint_post_audiences_id_memberships import EndpointPostAudiencesIdMemberships
    from .endpoint_post_audiences_id_memberships_data import EndpointPostAudiencesIdMembershipsData
    from .endpoint_post_audiences_id_memberships_data_audience import EndpointPostAudiencesIdMembershipsDataAudience
    from .endpoint_post_conversations_id_messages import EndpointPostConversationsIdMessages
    from .endpoint_post_conversations_id_schedules import EndpointPostConversationsIdSchedules
    from .endpoint_post_conversations_id_schedules_data_item import EndpointPostConversationsIdSchedulesDataItem
    from .endpoint_post_conversations_id_schedules_data_item_navigation import (
        EndpointPostConversationsIdSchedulesDataItemNavigation,
    )
    from .endpoint_post_conversations_id_searches import EndpointPostConversationsIdSearches
    from .endpoint_post_conversations_id_searches_data_item import EndpointPostConversationsIdSearchesDataItem
    from .endpoint_post_conversations_id_searches_data_item_relevance import (
        EndpointPostConversationsIdSearchesDataItemRelevance,
    )
    from .endpoint_post_conversations_schedules import EndpointPostConversationsSchedules
    from .endpoint_post_conversations_schedules_data_item import EndpointPostConversationsSchedulesDataItem
    from .endpoint_post_conversations_schedules_data_item_navigation import (
        EndpointPostConversationsSchedulesDataItemNavigation,
    )
    from .endpoint_post_conversations_searches import EndpointPostConversationsSearches
    from .endpoint_post_conversations_searches_data_item import EndpointPostConversationsSearchesDataItem
    from .endpoint_post_conversations_searches_data_item_relevance import (
        EndpointPostConversationsSearchesDataItemRelevance,
    )
    from .endpoint_post_groups import EndpointPostGroups
    from .endpoint_post_groups_id_memberships import EndpointPostGroupsIdMemberships
    from .endpoint_post_groups_id_memberships_data import EndpointPostGroupsIdMembershipsData
    from .endpoint_post_groups_id_messages import EndpointPostGroupsIdMessages
    from .endpoint_post_groups_id_schedules import EndpointPostGroupsIdSchedules
    from .endpoint_post_groups_id_schedules_data_item import EndpointPostGroupsIdSchedulesDataItem
    from .endpoint_post_groups_id_schedules_data_item_navigation import EndpointPostGroupsIdSchedulesDataItemNavigation
    from .endpoint_post_groups_messages_id_metadata import EndpointPostGroupsMessagesIdMetadata
    from .endpoint_post_groups_messages_metadata_filters import EndpointPostGroupsMessagesMetadataFilters
    from .endpoint_post_groups_messages_metadata_filters_data_item import (
        EndpointPostGroupsMessagesMetadataFiltersDataItem,
    )
    from .endpoint_post_groups_schedules import EndpointPostGroupsSchedules
    from .endpoint_post_groups_schedules_data_item import EndpointPostGroupsSchedulesDataItem
    from .endpoint_post_groups_schedules_data_item_navigation import EndpointPostGroupsSchedulesDataItemNavigation
    from .endpoint_post_markdown import EndpointPostMarkdown
    from .endpoint_post_markdown_data import EndpointPostMarkdownData
    from .endpoint_post_messages_id_metadata import EndpointPostMessagesIdMetadata
    from .endpoint_post_messages_metadata_filters import EndpointPostMessagesMetadataFilters
    from .endpoint_post_messages_metadata_filters_data_item import EndpointPostMessagesMetadataFiltersDataItem
    from .endpoint_post_positions import EndpointPostPositions
    from .endpoint_post_users_id_messages import EndpointPostUsersIdMessages
    from .endpoint_post_users_id_metadata import EndpointPostUsersIdMetadata
    from .endpoint_post_users_invites import EndpointPostUsersInvites
    from .endpoint_post_users_invites_data import EndpointPostUsersInvitesData
    from .endpoint_post_users_invites_data_discovered import EndpointPostUsersInvitesDataDiscovered
    from .endpoint_post_users_invites_data_emailed import EndpointPostUsersInvitesDataEmailed
    from .endpoint_post_users_invites_data_existing import EndpointPostUsersInvitesDataExisting
    from .endpoint_post_users_invites_data_invalid import EndpointPostUsersInvitesDataInvalid
    from .endpoint_post_users_metadata_filters import EndpointPostUsersMetadataFilters
    from .endpoint_post_users_metadata_filters_data_item import EndpointPostUsersMetadataFiltersDataItem
    from .endpoint_post_users_searches import EndpointPostUsersSearches
    from .endpoint_post_users_searches_data_item import EndpointPostUsersSearchesDataItem
    from .endpoint_post_users_searches_data_item_relevance import EndpointPostUsersSearchesDataItemRelevance
    from .endpoint_post_webhooks import EndpointPostWebhooks
    from .group import Group
    from .group_first_message import GroupFirstMessage
    from .group_message import GroupMessage
    from .group_message_data import GroupMessageData
    from .group_message_data_content import GroupMessageDataContent
    from .group_message_data_settings import GroupMessageDataSettings
    from .group_message_data_status import GroupMessageDataStatus
    from .group_message_last_seen import GroupMessageLastSeen
    from .group_message_moderated import GroupMessageModerated
    from .group_message_text import GroupMessageText
    from .group_properties import GroupProperties
    from .me import Me
    from .me_business_card import MeBusinessCard
    from .me_business_card_website import MeBusinessCardWebsite
    from .me_location import MeLocation
    from .me_matching import MeMatching
    from .me_profile import MeProfile
    from .me_settings import MeSettings
    from .me_usage import MeUsage
    from .member import Member
    from .member_identity import MemberIdentity
    from .member_location import MemberLocation
    from .member_personal import MemberPersonal
    from .member_signature import MemberSignature
    from .member_stats import MemberStats
    from .message import Message
    from .message_data import MessageData
    from .message_data_content import MessageDataContent
    from .message_data_settings import MessageDataSettings
    from .message_data_status import MessageDataStatus
    from .message_last_seen import MessageLastSeen
    from .message_text import MessageText
    from .oauth_scope import OauthScope
    from .position import Position
    from .position_organization import PositionOrganization
    from .position_role import PositionRole
    from .user import User
    from .user_business_card import UserBusinessCard
    from .user_business_card_website import UserBusinessCardWebsite
    from .user_data import UserData
    from .user_data_content import UserDataContent
    from .user_data_settings import UserDataSettings
    from .user_data_status import UserDataStatus
    from .user_profile import UserProfile
    from .user_usage import UserUsage
    from .webhook import Webhook
    from .webhook_event import WebhookEvent
    from .webhook_object import WebhookObject
_dynamic_imports: typing.Dict[str, str] = {
    "ApiPagination": ".api_pagination",
    "App": ".app",
    "AppAbout": ".app_about",
    "AppAboutWebsite": ".app_about_website",
    "AppLegal": ".app_legal",
    "Bubble": ".bubble",
    "BubbleAbout": ".bubble_about",
    "Conversation": ".conversation",
    "ConversationFirstMessage": ".conversation_first_message",
    "EndpointDeleteGroupsIdMemberships": ".endpoint_delete_groups_id_memberships",
    "EndpointDeleteGroupsMessagesId": ".endpoint_delete_groups_messages_id",
    "EndpointDeletePositionsId": ".endpoint_delete_positions_id",
    "EndpointDeleteWebhooksId": ".endpoint_delete_webhooks_id",
    "EndpointGetApps": ".endpoint_get_apps",
    "EndpointGetAppsId": ".endpoint_get_apps_id",
    "EndpointGetAudiences": ".endpoint_get_audiences",
    "EndpointGetAudiencesId": ".endpoint_get_audiences_id",
    "EndpointGetAutocompletes": ".endpoint_get_autocompletes",
    "EndpointGetAutocompletesData": ".endpoint_get_autocompletes_data",
    "EndpointGetConversationsId": ".endpoint_get_conversations_id",
    "EndpointGetConversationsIdMessages": ".endpoint_get_conversations_id_messages",
    "EndpointGetConversationsIdStatuses": ".endpoint_get_conversations_id_statuses",
    "EndpointGetConversationsIdStatusesDataItem": ".endpoint_get_conversations_id_statuses_data_item",
    "EndpointGetConversationsIdStatusesDataItemBubbled": ".endpoint_get_conversations_id_statuses_data_item_bubbled",
    "EndpointGetConversationsStatuses": ".endpoint_get_conversations_statuses",
    "EndpointGetConversationsStatusesDataItem": ".endpoint_get_conversations_statuses_data_item",
    "EndpointGetConversationsStatusesDataItemBubbled": ".endpoint_get_conversations_statuses_data_item_bubbled",
    "EndpointGetGroups": ".endpoint_get_groups",
    "EndpointGetGroupsId": ".endpoint_get_groups_id",
    "EndpointGetGroupsIdMemberships": ".endpoint_get_groups_id_memberships",
    "EndpointGetGroupsIdMembershipsDataItem": ".endpoint_get_groups_id_memberships_data_item",
    "EndpointGetGroupsIdMembershipsDataItemPrivileges": ".endpoint_get_groups_id_memberships_data_item_privileges",
    "EndpointGetGroupsIdMessages": ".endpoint_get_groups_id_messages",
    "EndpointGetGroupsIdStatuses": ".endpoint_get_groups_id_statuses",
    "EndpointGetGroupsIdStatusesDataItem": ".endpoint_get_groups_id_statuses_data_item",
    "EndpointGetGroupsMessagesId": ".endpoint_get_groups_messages_id",
    "EndpointGetGroupsMessagesIdMetadata": ".endpoint_get_groups_messages_id_metadata",
    "EndpointGetGroupsMessagesIdMetadataCollections": ".endpoint_get_groups_messages_id_metadata_collections",
    "EndpointGetGroupsStatuses": ".endpoint_get_groups_statuses",
    "EndpointGetGroupsStatusesDataItem": ".endpoint_get_groups_statuses_data_item",
    "EndpointGetIndustries": ".endpoint_get_industries",
    "EndpointGetMarkdownEmoticons": ".endpoint_get_markdown_emoticons",
    "EndpointGetMarkdownEmoticonsDataItem": ".endpoint_get_markdown_emoticons_data_item",
    "EndpointGetMessagesId": ".endpoint_get_messages_id",
    "EndpointGetMessagesIdMetadata": ".endpoint_get_messages_id_metadata",
    "EndpointGetMessagesIdMetadataCollections": ".endpoint_get_messages_id_metadata_collections",
    "EndpointGetUsers": ".endpoint_get_users",
    "EndpointGetUsersId": ".endpoint_get_users_id",
    "EndpointGetUsersIdGroups": ".endpoint_get_users_id_groups",
    "EndpointGetUsersIdGroupsMessages": ".endpoint_get_users_id_groups_messages",
    "EndpointGetUsersIdMetadata": ".endpoint_get_users_id_metadata",
    "EndpointGetUsersIdMetadataCollections": ".endpoint_get_users_id_metadata_collections",
    "EndpointGetUsersIdPositions": ".endpoint_get_users_id_positions",
    "EndpointGetUsersIdSynergies": ".endpoint_get_users_id_synergies",
    "EndpointGetUsersIdSynergiesDataItem": ".endpoint_get_users_id_synergies_data_item",
    "EndpointGetUsersIdSynergiesDataItemAdditional": ".endpoint_get_users_id_synergies_data_item_additional",
    "EndpointGetUsersIdSynergiesDataItemMatch": ".endpoint_get_users_id_synergies_data_item_match",
    "EndpointGetUsersIdSynergiesDataItemMatchDistanceAway": ".endpoint_get_users_id_synergies_data_item_match_distance_away",
    "EndpointGetUsersIdSynergiesDataItemMatchIndustry": ".endpoint_get_users_id_synergies_data_item_match_industry",
    "EndpointGetUsersIdSynergiesDataItemMatchMutualConnections": ".endpoint_get_users_id_synergies_data_item_match_mutual_connections",
    "EndpointGetUsersIdSynergiesDataItemMeet": ".endpoint_get_users_id_synergies_data_item_meet",
    "EndpointGetUsersIdSynergiesDataItemMeetPayment": ".endpoint_get_users_id_synergies_data_item_meet_payment",
    "EndpointGetUsersIdSynergiesDataItemMeetPaymentPaypal": ".endpoint_get_users_id_synergies_data_item_meet_payment_paypal",
    "EndpointGetUsersIdSynergiesDataItemRelationship": ".endpoint_get_users_id_synergies_data_item_relationship",
    "EndpointGetUsersNearby": ".endpoint_get_users_nearby",
    "EndpointGetUsersNearbyDataItem": ".endpoint_get_users_nearby_data_item",
    "EndpointGetUsersNearbyDataItemDistanceAway": ".endpoint_get_users_nearby_data_item_distance_away",
    "EndpointGetWebhooks": ".endpoint_get_webhooks",
    "EndpointPatchConversationsIdStatuses": ".endpoint_patch_conversations_id_statuses",
    "EndpointPatchConversationsIdStatusesData": ".endpoint_patch_conversations_id_statuses_data",
    "EndpointPatchGroupsId": ".endpoint_patch_groups_id",
    "EndpointPatchGroupsIdMemberships": ".endpoint_patch_groups_id_memberships",
    "EndpointPatchGroupsIdMembershipsDataItem": ".endpoint_patch_groups_id_memberships_data_item",
    "EndpointPatchGroupsIdMembershipsDataItemPrivileges": ".endpoint_patch_groups_id_memberships_data_item_privileges",
    "EndpointPatchPositionsId": ".endpoint_patch_positions_id",
    "EndpointPatchUsers": ".endpoint_patch_users",
    "EndpointPatchUsersIdSynergies": ".endpoint_patch_users_id_synergies",
    "EndpointPatchUsersIdSynergiesData": ".endpoint_patch_users_id_synergies_data",
    "EndpointPatchUsersIdSynergiesDataRelationship": ".endpoint_patch_users_id_synergies_data_relationship",
    "EndpointPostAudiencesIdMemberships": ".endpoint_post_audiences_id_memberships",
    "EndpointPostAudiencesIdMembershipsData": ".endpoint_post_audiences_id_memberships_data",
    "EndpointPostAudiencesIdMembershipsDataAudience": ".endpoint_post_audiences_id_memberships_data_audience",
    "EndpointPostConversationsIdMessages": ".endpoint_post_conversations_id_messages",
    "EndpointPostConversationsIdSchedules": ".endpoint_post_conversations_id_schedules",
    "EndpointPostConversationsIdSchedulesDataItem": ".endpoint_post_conversations_id_schedules_data_item",
    "EndpointPostConversationsIdSchedulesDataItemNavigation": ".endpoint_post_conversations_id_schedules_data_item_navigation",
    "EndpointPostConversationsIdSearches": ".endpoint_post_conversations_id_searches",
    "EndpointPostConversationsIdSearchesDataItem": ".endpoint_post_conversations_id_searches_data_item",
    "EndpointPostConversationsIdSearchesDataItemRelevance": ".endpoint_post_conversations_id_searches_data_item_relevance",
    "EndpointPostConversationsSchedules": ".endpoint_post_conversations_schedules",
    "EndpointPostConversationsSchedulesDataItem": ".endpoint_post_conversations_schedules_data_item",
    "EndpointPostConversationsSchedulesDataItemNavigation": ".endpoint_post_conversations_schedules_data_item_navigation",
    "EndpointPostConversationsSearches": ".endpoint_post_conversations_searches",
    "EndpointPostConversationsSearchesDataItem": ".endpoint_post_conversations_searches_data_item",
    "EndpointPostConversationsSearchesDataItemRelevance": ".endpoint_post_conversations_searches_data_item_relevance",
    "EndpointPostGroups": ".endpoint_post_groups",
    "EndpointPostGroupsIdMemberships": ".endpoint_post_groups_id_memberships",
    "EndpointPostGroupsIdMembershipsData": ".endpoint_post_groups_id_memberships_data",
    "EndpointPostGroupsIdMessages": ".endpoint_post_groups_id_messages",
    "EndpointPostGroupsIdSchedules": ".endpoint_post_groups_id_schedules",
    "EndpointPostGroupsIdSchedulesDataItem": ".endpoint_post_groups_id_schedules_data_item",
    "EndpointPostGroupsIdSchedulesDataItemNavigation": ".endpoint_post_groups_id_schedules_data_item_navigation",
    "EndpointPostGroupsMessagesIdMetadata": ".endpoint_post_groups_messages_id_metadata",
    "EndpointPostGroupsMessagesMetadataFilters": ".endpoint_post_groups_messages_metadata_filters",
    "EndpointPostGroupsMessagesMetadataFiltersDataItem": ".endpoint_post_groups_messages_metadata_filters_data_item",
    "EndpointPostGroupsSchedules": ".endpoint_post_groups_schedules",
    "EndpointPostGroupsSchedulesDataItem": ".endpoint_post_groups_schedules_data_item",
    "EndpointPostGroupsSchedulesDataItemNavigation": ".endpoint_post_groups_schedules_data_item_navigation",
    "EndpointPostMarkdown": ".endpoint_post_markdown",
    "EndpointPostMarkdownData": ".endpoint_post_markdown_data",
    "EndpointPostMessagesIdMetadata": ".endpoint_post_messages_id_metadata",
    "EndpointPostMessagesMetadataFilters": ".endpoint_post_messages_metadata_filters",
    "EndpointPostMessagesMetadataFiltersDataItem": ".endpoint_post_messages_metadata_filters_data_item",
    "EndpointPostPositions": ".endpoint_post_positions",
    "EndpointPostUsersIdMessages": ".endpoint_post_users_id_messages",
    "EndpointPostUsersIdMetadata": ".endpoint_post_users_id_metadata",
    "EndpointPostUsersInvites": ".endpoint_post_users_invites",
    "EndpointPostUsersInvitesData": ".endpoint_post_users_invites_data",
    "EndpointPostUsersInvitesDataDiscovered": ".endpoint_post_users_invites_data_discovered",
    "EndpointPostUsersInvitesDataEmailed": ".endpoint_post_users_invites_data_emailed",
    "EndpointPostUsersInvitesDataExisting": ".endpoint_post_users_invites_data_existing",
    "EndpointPostUsersInvitesDataInvalid": ".endpoint_post_users_invites_data_invalid",
    "EndpointPostUsersMetadataFilters": ".endpoint_post_users_metadata_filters",
    "EndpointPostUsersMetadataFiltersDataItem": ".endpoint_post_users_metadata_filters_data_item",
    "EndpointPostUsersSearches": ".endpoint_post_users_searches",
    "EndpointPostUsersSearchesDataItem": ".endpoint_post_users_searches_data_item",
    "EndpointPostUsersSearchesDataItemRelevance": ".endpoint_post_users_searches_data_item_relevance",
    "EndpointPostWebhooks": ".endpoint_post_webhooks",
    "Group": ".group",
    "GroupFirstMessage": ".group_first_message",
    "GroupMessage": ".group_message",
    "GroupMessageData": ".group_message_data",
    "GroupMessageDataContent": ".group_message_data_content",
    "GroupMessageDataSettings": ".group_message_data_settings",
    "GroupMessageDataStatus": ".group_message_data_status",
    "GroupMessageLastSeen": ".group_message_last_seen",
    "GroupMessageModerated": ".group_message_moderated",
    "GroupMessageText": ".group_message_text",
    "GroupProperties": ".group_properties",
    "Me": ".me",
    "MeBusinessCard": ".me_business_card",
    "MeBusinessCardWebsite": ".me_business_card_website",
    "MeLocation": ".me_location",
    "MeMatching": ".me_matching",
    "MeProfile": ".me_profile",
    "MeSettings": ".me_settings",
    "MeUsage": ".me_usage",
    "Member": ".member",
    "MemberIdentity": ".member_identity",
    "MemberLocation": ".member_location",
    "MemberPersonal": ".member_personal",
    "MemberSignature": ".member_signature",
    "MemberStats": ".member_stats",
    "Message": ".message",
    "MessageData": ".message_data",
    "MessageDataContent": ".message_data_content",
    "MessageDataSettings": ".message_data_settings",
    "MessageDataStatus": ".message_data_status",
    "MessageLastSeen": ".message_last_seen",
    "MessageText": ".message_text",
    "OauthScope": ".oauth_scope",
    "Position": ".position",
    "PositionOrganization": ".position_organization",
    "PositionRole": ".position_role",
    "User": ".user",
    "UserBusinessCard": ".user_business_card",
    "UserBusinessCardWebsite": ".user_business_card_website",
    "UserData": ".user_data",
    "UserDataContent": ".user_data_content",
    "UserDataSettings": ".user_data_settings",
    "UserDataStatus": ".user_data_status",
    "UserProfile": ".user_profile",
    "UserUsage": ".user_usage",
    "Webhook": ".webhook",
    "WebhookEvent": ".webhook_event",
    "WebhookObject": ".webhook_object",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "ApiPagination",
    "App",
    "AppAbout",
    "AppAboutWebsite",
    "AppLegal",
    "Bubble",
    "BubbleAbout",
    "Conversation",
    "ConversationFirstMessage",
    "EndpointDeleteGroupsIdMemberships",
    "EndpointDeleteGroupsMessagesId",
    "EndpointDeletePositionsId",
    "EndpointDeleteWebhooksId",
    "EndpointGetApps",
    "EndpointGetAppsId",
    "EndpointGetAudiences",
    "EndpointGetAudiencesId",
    "EndpointGetAutocompletes",
    "EndpointGetAutocompletesData",
    "EndpointGetConversationsId",
    "EndpointGetConversationsIdMessages",
    "EndpointGetConversationsIdStatuses",
    "EndpointGetConversationsIdStatusesDataItem",
    "EndpointGetConversationsIdStatusesDataItemBubbled",
    "EndpointGetConversationsStatuses",
    "EndpointGetConversationsStatusesDataItem",
    "EndpointGetConversationsStatusesDataItemBubbled",
    "EndpointGetGroups",
    "EndpointGetGroupsId",
    "EndpointGetGroupsIdMemberships",
    "EndpointGetGroupsIdMembershipsDataItem",
    "EndpointGetGroupsIdMembershipsDataItemPrivileges",
    "EndpointGetGroupsIdMessages",
    "EndpointGetGroupsIdStatuses",
    "EndpointGetGroupsIdStatusesDataItem",
    "EndpointGetGroupsMessagesId",
    "EndpointGetGroupsMessagesIdMetadata",
    "EndpointGetGroupsMessagesIdMetadataCollections",
    "EndpointGetGroupsStatuses",
    "EndpointGetGroupsStatusesDataItem",
    "EndpointGetIndustries",
    "EndpointGetMarkdownEmoticons",
    "EndpointGetMarkdownEmoticonsDataItem",
    "EndpointGetMessagesId",
    "EndpointGetMessagesIdMetadata",
    "EndpointGetMessagesIdMetadataCollections",
    "EndpointGetUsers",
    "EndpointGetUsersId",
    "EndpointGetUsersIdGroups",
    "EndpointGetUsersIdGroupsMessages",
    "EndpointGetUsersIdMetadata",
    "EndpointGetUsersIdMetadataCollections",
    "EndpointGetUsersIdPositions",
    "EndpointGetUsersIdSynergies",
    "EndpointGetUsersIdSynergiesDataItem",
    "EndpointGetUsersIdSynergiesDataItemAdditional",
    "EndpointGetUsersIdSynergiesDataItemMatch",
    "EndpointGetUsersIdSynergiesDataItemMatchDistanceAway",
    "EndpointGetUsersIdSynergiesDataItemMatchIndustry",
    "EndpointGetUsersIdSynergiesDataItemMatchMutualConnections",
    "EndpointGetUsersIdSynergiesDataItemMeet",
    "EndpointGetUsersIdSynergiesDataItemMeetPayment",
    "EndpointGetUsersIdSynergiesDataItemMeetPaymentPaypal",
    "EndpointGetUsersIdSynergiesDataItemRelationship",
    "EndpointGetUsersNearby",
    "EndpointGetUsersNearbyDataItem",
    "EndpointGetUsersNearbyDataItemDistanceAway",
    "EndpointGetWebhooks",
    "EndpointPatchConversationsIdStatuses",
    "EndpointPatchConversationsIdStatusesData",
    "EndpointPatchGroupsId",
    "EndpointPatchGroupsIdMemberships",
    "EndpointPatchGroupsIdMembershipsDataItem",
    "EndpointPatchGroupsIdMembershipsDataItemPrivileges",
    "EndpointPatchPositionsId",
    "EndpointPatchUsers",
    "EndpointPatchUsersIdSynergies",
    "EndpointPatchUsersIdSynergiesData",
    "EndpointPatchUsersIdSynergiesDataRelationship",
    "EndpointPostAudiencesIdMemberships",
    "EndpointPostAudiencesIdMembershipsData",
    "EndpointPostAudiencesIdMembershipsDataAudience",
    "EndpointPostConversationsIdMessages",
    "EndpointPostConversationsIdSchedules",
    "EndpointPostConversationsIdSchedulesDataItem",
    "EndpointPostConversationsIdSchedulesDataItemNavigation",
    "EndpointPostConversationsIdSearches",
    "EndpointPostConversationsIdSearchesDataItem",
    "EndpointPostConversationsIdSearchesDataItemRelevance",
    "EndpointPostConversationsSchedules",
    "EndpointPostConversationsSchedulesDataItem",
    "EndpointPostConversationsSchedulesDataItemNavigation",
    "EndpointPostConversationsSearches",
    "EndpointPostConversationsSearchesDataItem",
    "EndpointPostConversationsSearchesDataItemRelevance",
    "EndpointPostGroups",
    "EndpointPostGroupsIdMemberships",
    "EndpointPostGroupsIdMembershipsData",
    "EndpointPostGroupsIdMessages",
    "EndpointPostGroupsIdSchedules",
    "EndpointPostGroupsIdSchedulesDataItem",
    "EndpointPostGroupsIdSchedulesDataItemNavigation",
    "EndpointPostGroupsMessagesIdMetadata",
    "EndpointPostGroupsMessagesMetadataFilters",
    "EndpointPostGroupsMessagesMetadataFiltersDataItem",
    "EndpointPostGroupsSchedules",
    "EndpointPostGroupsSchedulesDataItem",
    "EndpointPostGroupsSchedulesDataItemNavigation",
    "EndpointPostMarkdown",
    "EndpointPostMarkdownData",
    "EndpointPostMessagesIdMetadata",
    "EndpointPostMessagesMetadataFilters",
    "EndpointPostMessagesMetadataFiltersDataItem",
    "EndpointPostPositions",
    "EndpointPostUsersIdMessages",
    "EndpointPostUsersIdMetadata",
    "EndpointPostUsersInvites",
    "EndpointPostUsersInvitesData",
    "EndpointPostUsersInvitesDataDiscovered",
    "EndpointPostUsersInvitesDataEmailed",
    "EndpointPostUsersInvitesDataExisting",
    "EndpointPostUsersInvitesDataInvalid",
    "EndpointPostUsersMetadataFilters",
    "EndpointPostUsersMetadataFiltersDataItem",
    "EndpointPostUsersSearches",
    "EndpointPostUsersSearchesDataItem",
    "EndpointPostUsersSearchesDataItemRelevance",
    "EndpointPostWebhooks",
    "Group",
    "GroupFirstMessage",
    "GroupMessage",
    "GroupMessageData",
    "GroupMessageDataContent",
    "GroupMessageDataSettings",
    "GroupMessageDataStatus",
    "GroupMessageLastSeen",
    "GroupMessageModerated",
    "GroupMessageText",
    "GroupProperties",
    "Me",
    "MeBusinessCard",
    "MeBusinessCardWebsite",
    "MeLocation",
    "MeMatching",
    "MeProfile",
    "MeSettings",
    "MeUsage",
    "Member",
    "MemberIdentity",
    "MemberLocation",
    "MemberPersonal",
    "MemberSignature",
    "MemberStats",
    "Message",
    "MessageData",
    "MessageDataContent",
    "MessageDataSettings",
    "MessageDataStatus",
    "MessageLastSeen",
    "MessageText",
    "OauthScope",
    "Position",
    "PositionOrganization",
    "PositionRole",
    "User",
    "UserBusinessCard",
    "UserBusinessCardWebsite",
    "UserData",
    "UserDataContent",
    "UserDataSettings",
    "UserDataStatus",
    "UserProfile",
    "UserUsage",
    "Webhook",
    "WebhookEvent",
    "WebhookObject",
]
