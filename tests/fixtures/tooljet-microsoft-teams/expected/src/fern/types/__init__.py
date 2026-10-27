



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .aad_user_conversation_member import AadUserConversationMember
    from .aad_user_conversation_member_user import AadUserConversationMemberUser
    from .channel import Channel
    from .channel_files_folder import ChannelFilesFolder
    from .channel_files_folder_file_system_info import ChannelFilesFolderFileSystemInfo
    from .channel_files_folder_folder import ChannelFilesFolderFolder
    from .channel_files_folder_parent_reference import ChannelFilesFolderParentReference
    from .channel_membership_type import ChannelMembershipType
    from .channel_summary import ChannelSummary
    from .chat import Chat
    from .chat_chat_type import ChatChatType
    from .chat_installed_apps_item import ChatInstalledAppsItem
    from .chat_installed_apps_item_teams_app import ChatInstalledAppsItemTeamsApp
    from .chat_last_message_preview import ChatLastMessagePreview
    from .chat_last_message_preview_body import ChatLastMessagePreviewBody
    from .chat_last_message_preview_from import ChatLastMessagePreviewFrom
    from .chat_last_message_preview_from_user import ChatLastMessagePreviewFromUser
    from .chat_message import ChatMessage
    from .chat_message_attachment import ChatMessageAttachment
    from .chat_message_body import ChatMessageBody
    from .chat_message_body_content_type import ChatMessageBodyContentType
    from .chat_message_channel_identity import ChatMessageChannelIdentity
    from .chat_message_from import ChatMessageFrom
    from .chat_message_from_application import ChatMessageFromApplication
    from .chat_message_from_device import ChatMessageFromDevice
    from .chat_message_from_user import ChatMessageFromUser
    from .chat_message_from_user_user_identity_type import ChatMessageFromUserUserIdentityType
    from .chat_message_hosted_contents_item import ChatMessageHostedContentsItem
    from .chat_message_importance import ChatMessageImportance
    from .chat_message_mentions_item import ChatMessageMentionsItem
    from .chat_message_mentions_item_mentioned import ChatMessageMentionsItemMentioned
    from .chat_message_mentions_item_mentioned_user import ChatMessageMentionsItemMentionedUser
    from .chat_message_message_type import ChatMessageMessageType
    from .chat_message_policy_violation import ChatMessagePolicyViolation
    from .chat_message_policy_violation_dlp_action import ChatMessagePolicyViolationDlpAction
    from .chat_message_policy_violation_policy_tip import ChatMessagePolicyViolationPolicyTip
    from .chat_message_policy_violation_user_action import ChatMessagePolicyViolationUserAction
    from .chat_message_policy_violation_verdict_details import ChatMessagePolicyViolationVerdictDetails
    from .chat_message_reactions_item import ChatMessageReactionsItem
    from .chat_message_reactions_item_user import ChatMessageReactionsItemUser
    from .chat_message_reactions_item_user_user import ChatMessageReactionsItemUserUser
    from .chat_online_meeting_info import ChatOnlineMeetingInfo
    from .chat_online_meeting_info_organizer import ChatOnlineMeetingInfoOrganizer
    from .chat_viewpoint import ChatViewpoint
    from .conversation_member import ConversationMember
    from .conversation_member_input import ConversationMemberInput
    from .conversation_member_input_roles_item import ConversationMemberInputRolesItem
    from .error import Error
    from .error_error import ErrorError
    from .error_error_details_item import ErrorErrorDetailsItem
    from .error_error_innererror import ErrorErrorInnererror
    from .team import Team
    from .team_discovery_settings import TeamDiscoverySettings
    from .team_fun_settings import TeamFunSettings
    from .team_fun_settings_giphy_content_rating import TeamFunSettingsGiphyContentRating
    from .team_guest_settings import TeamGuestSettings
    from .team_member_settings import TeamMemberSettings
    from .team_messaging_settings import TeamMessagingSettings
    from .team_specialization import TeamSpecialization
    from .team_summary import TeamSummary
    from .team_visibility import TeamVisibility
_dynamic_imports: typing.Dict[str, str] = {
    "AadUserConversationMember": ".aad_user_conversation_member",
    "AadUserConversationMemberUser": ".aad_user_conversation_member_user",
    "Channel": ".channel",
    "ChannelFilesFolder": ".channel_files_folder",
    "ChannelFilesFolderFileSystemInfo": ".channel_files_folder_file_system_info",
    "ChannelFilesFolderFolder": ".channel_files_folder_folder",
    "ChannelFilesFolderParentReference": ".channel_files_folder_parent_reference",
    "ChannelMembershipType": ".channel_membership_type",
    "ChannelSummary": ".channel_summary",
    "Chat": ".chat",
    "ChatChatType": ".chat_chat_type",
    "ChatInstalledAppsItem": ".chat_installed_apps_item",
    "ChatInstalledAppsItemTeamsApp": ".chat_installed_apps_item_teams_app",
    "ChatLastMessagePreview": ".chat_last_message_preview",
    "ChatLastMessagePreviewBody": ".chat_last_message_preview_body",
    "ChatLastMessagePreviewFrom": ".chat_last_message_preview_from",
    "ChatLastMessagePreviewFromUser": ".chat_last_message_preview_from_user",
    "ChatMessage": ".chat_message",
    "ChatMessageAttachment": ".chat_message_attachment",
    "ChatMessageBody": ".chat_message_body",
    "ChatMessageBodyContentType": ".chat_message_body_content_type",
    "ChatMessageChannelIdentity": ".chat_message_channel_identity",
    "ChatMessageFrom": ".chat_message_from",
    "ChatMessageFromApplication": ".chat_message_from_application",
    "ChatMessageFromDevice": ".chat_message_from_device",
    "ChatMessageFromUser": ".chat_message_from_user",
    "ChatMessageFromUserUserIdentityType": ".chat_message_from_user_user_identity_type",
    "ChatMessageHostedContentsItem": ".chat_message_hosted_contents_item",
    "ChatMessageImportance": ".chat_message_importance",
    "ChatMessageMentionsItem": ".chat_message_mentions_item",
    "ChatMessageMentionsItemMentioned": ".chat_message_mentions_item_mentioned",
    "ChatMessageMentionsItemMentionedUser": ".chat_message_mentions_item_mentioned_user",
    "ChatMessageMessageType": ".chat_message_message_type",
    "ChatMessagePolicyViolation": ".chat_message_policy_violation",
    "ChatMessagePolicyViolationDlpAction": ".chat_message_policy_violation_dlp_action",
    "ChatMessagePolicyViolationPolicyTip": ".chat_message_policy_violation_policy_tip",
    "ChatMessagePolicyViolationUserAction": ".chat_message_policy_violation_user_action",
    "ChatMessagePolicyViolationVerdictDetails": ".chat_message_policy_violation_verdict_details",
    "ChatMessageReactionsItem": ".chat_message_reactions_item",
    "ChatMessageReactionsItemUser": ".chat_message_reactions_item_user",
    "ChatMessageReactionsItemUserUser": ".chat_message_reactions_item_user_user",
    "ChatOnlineMeetingInfo": ".chat_online_meeting_info",
    "ChatOnlineMeetingInfoOrganizer": ".chat_online_meeting_info_organizer",
    "ChatViewpoint": ".chat_viewpoint",
    "ConversationMember": ".conversation_member",
    "ConversationMemberInput": ".conversation_member_input",
    "ConversationMemberInputRolesItem": ".conversation_member_input_roles_item",
    "Error": ".error",
    "ErrorError": ".error_error",
    "ErrorErrorDetailsItem": ".error_error_details_item",
    "ErrorErrorInnererror": ".error_error_innererror",
    "Team": ".team",
    "TeamDiscoverySettings": ".team_discovery_settings",
    "TeamFunSettings": ".team_fun_settings",
    "TeamFunSettingsGiphyContentRating": ".team_fun_settings_giphy_content_rating",
    "TeamGuestSettings": ".team_guest_settings",
    "TeamMemberSettings": ".team_member_settings",
    "TeamMessagingSettings": ".team_messaging_settings",
    "TeamSpecialization": ".team_specialization",
    "TeamSummary": ".team_summary",
    "TeamVisibility": ".team_visibility",
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
    "AadUserConversationMember",
    "AadUserConversationMemberUser",
    "Channel",
    "ChannelFilesFolder",
    "ChannelFilesFolderFileSystemInfo",
    "ChannelFilesFolderFolder",
    "ChannelFilesFolderParentReference",
    "ChannelMembershipType",
    "ChannelSummary",
    "Chat",
    "ChatChatType",
    "ChatInstalledAppsItem",
    "ChatInstalledAppsItemTeamsApp",
    "ChatLastMessagePreview",
    "ChatLastMessagePreviewBody",
    "ChatLastMessagePreviewFrom",
    "ChatLastMessagePreviewFromUser",
    "ChatMessage",
    "ChatMessageAttachment",
    "ChatMessageBody",
    "ChatMessageBodyContentType",
    "ChatMessageChannelIdentity",
    "ChatMessageFrom",
    "ChatMessageFromApplication",
    "ChatMessageFromDevice",
    "ChatMessageFromUser",
    "ChatMessageFromUserUserIdentityType",
    "ChatMessageHostedContentsItem",
    "ChatMessageImportance",
    "ChatMessageMentionsItem",
    "ChatMessageMentionsItemMentioned",
    "ChatMessageMentionsItemMentionedUser",
    "ChatMessageMessageType",
    "ChatMessagePolicyViolation",
    "ChatMessagePolicyViolationDlpAction",
    "ChatMessagePolicyViolationPolicyTip",
    "ChatMessagePolicyViolationUserAction",
    "ChatMessagePolicyViolationVerdictDetails",
    "ChatMessageReactionsItem",
    "ChatMessageReactionsItemUser",
    "ChatMessageReactionsItemUserUser",
    "ChatOnlineMeetingInfo",
    "ChatOnlineMeetingInfoOrganizer",
    "ChatViewpoint",
    "ConversationMember",
    "ConversationMemberInput",
    "ConversationMemberInputRolesItem",
    "Error",
    "ErrorError",
    "ErrorErrorDetailsItem",
    "ErrorErrorInnererror",
    "Team",
    "TeamDiscoverySettings",
    "TeamFunSettings",
    "TeamFunSettingsGiphyContentRating",
    "TeamGuestSettings",
    "TeamMemberSettings",
    "TeamMessagingSettings",
    "TeamSpecialization",
    "TeamSummary",
    "TeamVisibility",
]
