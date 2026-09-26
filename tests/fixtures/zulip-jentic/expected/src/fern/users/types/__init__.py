



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_alert_words_response import AddAlertWordsResponse
    from .create_user_group_request_can_add_members_group import CreateUserGroupRequestCanAddMembersGroup
    from .create_user_group_request_can_add_members_group_direct_members import (
        CreateUserGroupRequestCanAddMembersGroupDirectMembers,
    )
    from .create_user_group_request_can_join_group import CreateUserGroupRequestCanJoinGroup
    from .create_user_group_request_can_join_group_direct_members import CreateUserGroupRequestCanJoinGroupDirectMembers
    from .create_user_group_request_can_leave_group import CreateUserGroupRequestCanLeaveGroup
    from .create_user_group_request_can_leave_group_direct_members import (
        CreateUserGroupRequestCanLeaveGroupDirectMembers,
    )
    from .create_user_group_request_can_manage_group import CreateUserGroupRequestCanManageGroup
    from .create_user_group_request_can_manage_group_direct_members import (
        CreateUserGroupRequestCanManageGroupDirectMembers,
    )
    from .create_user_group_request_can_mention_group import CreateUserGroupRequestCanMentionGroup
    from .create_user_group_request_can_mention_group_direct_members import (
        CreateUserGroupRequestCanMentionGroupDirectMembers,
    )
    from .create_user_group_request_can_remove_members_group import CreateUserGroupRequestCanRemoveMembersGroup
    from .create_user_group_request_can_remove_members_group_direct_members import (
        CreateUserGroupRequestCanRemoveMembersGroupDirectMembers,
    )
    from .create_user_group_response import CreateUserGroupResponse
    from .create_user_response import CreateUserResponse
    from .get_alert_words_response import GetAlertWordsResponse
    from .get_attachments_response import GetAttachmentsResponse
    from .get_bot_api_key_response import GetBotApiKeyResponse
    from .get_is_user_group_member_response import GetIsUserGroupMemberResponse
    from .get_own_user_response import GetOwnUserResponse
    from .get_user_by_email_response import GetUserByEmailResponse
    from .get_user_group_members_response import GetUserGroupMembersResponse
    from .get_user_group_subgroups_response import GetUserGroupSubgroupsResponse
    from .get_user_groups_response import GetUserGroupsResponse
    from .get_user_groups_response_user_groups_item import GetUserGroupsResponseUserGroupsItem
    from .get_user_groups_response_user_groups_item_can_add_members_group import (
        GetUserGroupsResponseUserGroupsItemCanAddMembersGroup,
    )
    from .get_user_groups_response_user_groups_item_can_add_members_group_direct_members import (
        GetUserGroupsResponseUserGroupsItemCanAddMembersGroupDirectMembers,
    )
    from .get_user_groups_response_user_groups_item_can_join_group import (
        GetUserGroupsResponseUserGroupsItemCanJoinGroup,
    )
    from .get_user_groups_response_user_groups_item_can_join_group_direct_members import (
        GetUserGroupsResponseUserGroupsItemCanJoinGroupDirectMembers,
    )
    from .get_user_groups_response_user_groups_item_can_leave_group import (
        GetUserGroupsResponseUserGroupsItemCanLeaveGroup,
    )
    from .get_user_groups_response_user_groups_item_can_leave_group_direct_members import (
        GetUserGroupsResponseUserGroupsItemCanLeaveGroupDirectMembers,
    )
    from .get_user_groups_response_user_groups_item_can_manage_group import (
        GetUserGroupsResponseUserGroupsItemCanManageGroup,
    )
    from .get_user_groups_response_user_groups_item_can_manage_group_direct_members import (
        GetUserGroupsResponseUserGroupsItemCanManageGroupDirectMembers,
    )
    from .get_user_groups_response_user_groups_item_can_mention_group import (
        GetUserGroupsResponseUserGroupsItemCanMentionGroup,
    )
    from .get_user_groups_response_user_groups_item_can_mention_group_direct_members import (
        GetUserGroupsResponseUserGroupsItemCanMentionGroupDirectMembers,
    )
    from .get_user_groups_response_user_groups_item_can_remove_members_group import (
        GetUserGroupsResponseUserGroupsItemCanRemoveMembersGroup,
    )
    from .get_user_groups_response_user_groups_item_can_remove_members_group_direct_members import (
        GetUserGroupsResponseUserGroupsItemCanRemoveMembersGroupDirectMembers,
    )
    from .get_user_presence_response import GetUserPresenceResponse
    from .get_user_presence_response_presence_value import GetUserPresenceResponsePresenceValue
    from .get_user_response import GetUserResponse
    from .get_user_status_response import GetUserStatusResponse
    from .get_user_status_response_status import GetUserStatusResponseStatus
    from .get_user_status_response_status_reaction_type import GetUserStatusResponseStatusReactionType
    from .get_users_response import GetUsersResponse
    from .regenerate_api_key_response import RegenerateApiKeyResponse
    from .regenerate_bot_api_key_response import RegenerateBotApiKeyResponse
    from .remove_alert_words_response import RemoveAlertWordsResponse
    from .set_typing_status_for_message_edit_request_op import SetTypingStatusForMessageEditRequestOp
    from .set_typing_status_request_op import SetTypingStatusRequestOp
    from .set_typing_status_request_type import SetTypingStatusRequestType
    from .update_presence_request_status import UpdatePresenceRequestStatus
    from .update_presence_response import UpdatePresenceResponse
    from .update_presence_response_presences_value import UpdatePresenceResponsePresencesValue
    from .update_settings_request_resolved_topic_notice_auto_read_policy import (
        UpdateSettingsRequestResolvedTopicNoticeAutoReadPolicy,
    )
    from .update_settings_request_target_users import UpdateSettingsRequestTargetUsers
    from .update_settings_request_web_animate_image_previews import UpdateSettingsRequestWebAnimateImagePreviews
    from .update_user_group_request_can_add_members_group import UpdateUserGroupRequestCanAddMembersGroup
    from .update_user_group_request_can_add_members_group_new import UpdateUserGroupRequestCanAddMembersGroupNew
    from .update_user_group_request_can_add_members_group_new_direct_members import (
        UpdateUserGroupRequestCanAddMembersGroupNewDirectMembers,
    )
    from .update_user_group_request_can_add_members_group_old import UpdateUserGroupRequestCanAddMembersGroupOld
    from .update_user_group_request_can_add_members_group_old_direct_members import (
        UpdateUserGroupRequestCanAddMembersGroupOldDirectMembers,
    )
    from .update_user_group_request_can_join_group import UpdateUserGroupRequestCanJoinGroup
    from .update_user_group_request_can_join_group_new import UpdateUserGroupRequestCanJoinGroupNew
    from .update_user_group_request_can_join_group_new_direct_members import (
        UpdateUserGroupRequestCanJoinGroupNewDirectMembers,
    )
    from .update_user_group_request_can_join_group_old import UpdateUserGroupRequestCanJoinGroupOld
    from .update_user_group_request_can_join_group_old_direct_members import (
        UpdateUserGroupRequestCanJoinGroupOldDirectMembers,
    )
    from .update_user_group_request_can_leave_group import UpdateUserGroupRequestCanLeaveGroup
    from .update_user_group_request_can_leave_group_new import UpdateUserGroupRequestCanLeaveGroupNew
    from .update_user_group_request_can_leave_group_new_direct_members import (
        UpdateUserGroupRequestCanLeaveGroupNewDirectMembers,
    )
    from .update_user_group_request_can_leave_group_old import UpdateUserGroupRequestCanLeaveGroupOld
    from .update_user_group_request_can_leave_group_old_direct_members import (
        UpdateUserGroupRequestCanLeaveGroupOldDirectMembers,
    )
    from .update_user_group_request_can_manage_group import UpdateUserGroupRequestCanManageGroup
    from .update_user_group_request_can_manage_group_new import UpdateUserGroupRequestCanManageGroupNew
    from .update_user_group_request_can_manage_group_new_direct_members import (
        UpdateUserGroupRequestCanManageGroupNewDirectMembers,
    )
    from .update_user_group_request_can_manage_group_old import UpdateUserGroupRequestCanManageGroupOld
    from .update_user_group_request_can_manage_group_old_direct_members import (
        UpdateUserGroupRequestCanManageGroupOldDirectMembers,
    )
    from .update_user_group_request_can_mention_group import UpdateUserGroupRequestCanMentionGroup
    from .update_user_group_request_can_mention_group_new import UpdateUserGroupRequestCanMentionGroupNew
    from .update_user_group_request_can_mention_group_new_direct_members import (
        UpdateUserGroupRequestCanMentionGroupNewDirectMembers,
    )
    from .update_user_group_request_can_mention_group_old import UpdateUserGroupRequestCanMentionGroupOld
    from .update_user_group_request_can_mention_group_old_direct_members import (
        UpdateUserGroupRequestCanMentionGroupOldDirectMembers,
    )
    from .update_user_group_request_can_remove_members_group import UpdateUserGroupRequestCanRemoveMembersGroup
    from .update_user_group_request_can_remove_members_group_new import UpdateUserGroupRequestCanRemoveMembersGroupNew
    from .update_user_group_request_can_remove_members_group_new_direct_members import (
        UpdateUserGroupRequestCanRemoveMembersGroupNewDirectMembers,
    )
    from .update_user_group_request_can_remove_members_group_old import UpdateUserGroupRequestCanRemoveMembersGroupOld
    from .update_user_group_request_can_remove_members_group_old_direct_members import (
        UpdateUserGroupRequestCanRemoveMembersGroupOldDirectMembers,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AddAlertWordsResponse": ".add_alert_words_response",
    "CreateUserGroupRequestCanAddMembersGroup": ".create_user_group_request_can_add_members_group",
    "CreateUserGroupRequestCanAddMembersGroupDirectMembers": ".create_user_group_request_can_add_members_group_direct_members",
    "CreateUserGroupRequestCanJoinGroup": ".create_user_group_request_can_join_group",
    "CreateUserGroupRequestCanJoinGroupDirectMembers": ".create_user_group_request_can_join_group_direct_members",
    "CreateUserGroupRequestCanLeaveGroup": ".create_user_group_request_can_leave_group",
    "CreateUserGroupRequestCanLeaveGroupDirectMembers": ".create_user_group_request_can_leave_group_direct_members",
    "CreateUserGroupRequestCanManageGroup": ".create_user_group_request_can_manage_group",
    "CreateUserGroupRequestCanManageGroupDirectMembers": ".create_user_group_request_can_manage_group_direct_members",
    "CreateUserGroupRequestCanMentionGroup": ".create_user_group_request_can_mention_group",
    "CreateUserGroupRequestCanMentionGroupDirectMembers": ".create_user_group_request_can_mention_group_direct_members",
    "CreateUserGroupRequestCanRemoveMembersGroup": ".create_user_group_request_can_remove_members_group",
    "CreateUserGroupRequestCanRemoveMembersGroupDirectMembers": ".create_user_group_request_can_remove_members_group_direct_members",
    "CreateUserGroupResponse": ".create_user_group_response",
    "CreateUserResponse": ".create_user_response",
    "GetAlertWordsResponse": ".get_alert_words_response",
    "GetAttachmentsResponse": ".get_attachments_response",
    "GetBotApiKeyResponse": ".get_bot_api_key_response",
    "GetIsUserGroupMemberResponse": ".get_is_user_group_member_response",
    "GetOwnUserResponse": ".get_own_user_response",
    "GetUserByEmailResponse": ".get_user_by_email_response",
    "GetUserGroupMembersResponse": ".get_user_group_members_response",
    "GetUserGroupSubgroupsResponse": ".get_user_group_subgroups_response",
    "GetUserGroupsResponse": ".get_user_groups_response",
    "GetUserGroupsResponseUserGroupsItem": ".get_user_groups_response_user_groups_item",
    "GetUserGroupsResponseUserGroupsItemCanAddMembersGroup": ".get_user_groups_response_user_groups_item_can_add_members_group",
    "GetUserGroupsResponseUserGroupsItemCanAddMembersGroupDirectMembers": ".get_user_groups_response_user_groups_item_can_add_members_group_direct_members",
    "GetUserGroupsResponseUserGroupsItemCanJoinGroup": ".get_user_groups_response_user_groups_item_can_join_group",
    "GetUserGroupsResponseUserGroupsItemCanJoinGroupDirectMembers": ".get_user_groups_response_user_groups_item_can_join_group_direct_members",
    "GetUserGroupsResponseUserGroupsItemCanLeaveGroup": ".get_user_groups_response_user_groups_item_can_leave_group",
    "GetUserGroupsResponseUserGroupsItemCanLeaveGroupDirectMembers": ".get_user_groups_response_user_groups_item_can_leave_group_direct_members",
    "GetUserGroupsResponseUserGroupsItemCanManageGroup": ".get_user_groups_response_user_groups_item_can_manage_group",
    "GetUserGroupsResponseUserGroupsItemCanManageGroupDirectMembers": ".get_user_groups_response_user_groups_item_can_manage_group_direct_members",
    "GetUserGroupsResponseUserGroupsItemCanMentionGroup": ".get_user_groups_response_user_groups_item_can_mention_group",
    "GetUserGroupsResponseUserGroupsItemCanMentionGroupDirectMembers": ".get_user_groups_response_user_groups_item_can_mention_group_direct_members",
    "GetUserGroupsResponseUserGroupsItemCanRemoveMembersGroup": ".get_user_groups_response_user_groups_item_can_remove_members_group",
    "GetUserGroupsResponseUserGroupsItemCanRemoveMembersGroupDirectMembers": ".get_user_groups_response_user_groups_item_can_remove_members_group_direct_members",
    "GetUserPresenceResponse": ".get_user_presence_response",
    "GetUserPresenceResponsePresenceValue": ".get_user_presence_response_presence_value",
    "GetUserResponse": ".get_user_response",
    "GetUserStatusResponse": ".get_user_status_response",
    "GetUserStatusResponseStatus": ".get_user_status_response_status",
    "GetUserStatusResponseStatusReactionType": ".get_user_status_response_status_reaction_type",
    "GetUsersResponse": ".get_users_response",
    "RegenerateApiKeyResponse": ".regenerate_api_key_response",
    "RegenerateBotApiKeyResponse": ".regenerate_bot_api_key_response",
    "RemoveAlertWordsResponse": ".remove_alert_words_response",
    "SetTypingStatusForMessageEditRequestOp": ".set_typing_status_for_message_edit_request_op",
    "SetTypingStatusRequestOp": ".set_typing_status_request_op",
    "SetTypingStatusRequestType": ".set_typing_status_request_type",
    "UpdatePresenceRequestStatus": ".update_presence_request_status",
    "UpdatePresenceResponse": ".update_presence_response",
    "UpdatePresenceResponsePresencesValue": ".update_presence_response_presences_value",
    "UpdateSettingsRequestResolvedTopicNoticeAutoReadPolicy": ".update_settings_request_resolved_topic_notice_auto_read_policy",
    "UpdateSettingsRequestTargetUsers": ".update_settings_request_target_users",
    "UpdateSettingsRequestWebAnimateImagePreviews": ".update_settings_request_web_animate_image_previews",
    "UpdateUserGroupRequestCanAddMembersGroup": ".update_user_group_request_can_add_members_group",
    "UpdateUserGroupRequestCanAddMembersGroupNew": ".update_user_group_request_can_add_members_group_new",
    "UpdateUserGroupRequestCanAddMembersGroupNewDirectMembers": ".update_user_group_request_can_add_members_group_new_direct_members",
    "UpdateUserGroupRequestCanAddMembersGroupOld": ".update_user_group_request_can_add_members_group_old",
    "UpdateUserGroupRequestCanAddMembersGroupOldDirectMembers": ".update_user_group_request_can_add_members_group_old_direct_members",
    "UpdateUserGroupRequestCanJoinGroup": ".update_user_group_request_can_join_group",
    "UpdateUserGroupRequestCanJoinGroupNew": ".update_user_group_request_can_join_group_new",
    "UpdateUserGroupRequestCanJoinGroupNewDirectMembers": ".update_user_group_request_can_join_group_new_direct_members",
    "UpdateUserGroupRequestCanJoinGroupOld": ".update_user_group_request_can_join_group_old",
    "UpdateUserGroupRequestCanJoinGroupOldDirectMembers": ".update_user_group_request_can_join_group_old_direct_members",
    "UpdateUserGroupRequestCanLeaveGroup": ".update_user_group_request_can_leave_group",
    "UpdateUserGroupRequestCanLeaveGroupNew": ".update_user_group_request_can_leave_group_new",
    "UpdateUserGroupRequestCanLeaveGroupNewDirectMembers": ".update_user_group_request_can_leave_group_new_direct_members",
    "UpdateUserGroupRequestCanLeaveGroupOld": ".update_user_group_request_can_leave_group_old",
    "UpdateUserGroupRequestCanLeaveGroupOldDirectMembers": ".update_user_group_request_can_leave_group_old_direct_members",
    "UpdateUserGroupRequestCanManageGroup": ".update_user_group_request_can_manage_group",
    "UpdateUserGroupRequestCanManageGroupNew": ".update_user_group_request_can_manage_group_new",
    "UpdateUserGroupRequestCanManageGroupNewDirectMembers": ".update_user_group_request_can_manage_group_new_direct_members",
    "UpdateUserGroupRequestCanManageGroupOld": ".update_user_group_request_can_manage_group_old",
    "UpdateUserGroupRequestCanManageGroupOldDirectMembers": ".update_user_group_request_can_manage_group_old_direct_members",
    "UpdateUserGroupRequestCanMentionGroup": ".update_user_group_request_can_mention_group",
    "UpdateUserGroupRequestCanMentionGroupNew": ".update_user_group_request_can_mention_group_new",
    "UpdateUserGroupRequestCanMentionGroupNewDirectMembers": ".update_user_group_request_can_mention_group_new_direct_members",
    "UpdateUserGroupRequestCanMentionGroupOld": ".update_user_group_request_can_mention_group_old",
    "UpdateUserGroupRequestCanMentionGroupOldDirectMembers": ".update_user_group_request_can_mention_group_old_direct_members",
    "UpdateUserGroupRequestCanRemoveMembersGroup": ".update_user_group_request_can_remove_members_group",
    "UpdateUserGroupRequestCanRemoveMembersGroupNew": ".update_user_group_request_can_remove_members_group_new",
    "UpdateUserGroupRequestCanRemoveMembersGroupNewDirectMembers": ".update_user_group_request_can_remove_members_group_new_direct_members",
    "UpdateUserGroupRequestCanRemoveMembersGroupOld": ".update_user_group_request_can_remove_members_group_old",
    "UpdateUserGroupRequestCanRemoveMembersGroupOldDirectMembers": ".update_user_group_request_can_remove_members_group_old_direct_members",
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
    "AddAlertWordsResponse",
    "CreateUserGroupRequestCanAddMembersGroup",
    "CreateUserGroupRequestCanAddMembersGroupDirectMembers",
    "CreateUserGroupRequestCanJoinGroup",
    "CreateUserGroupRequestCanJoinGroupDirectMembers",
    "CreateUserGroupRequestCanLeaveGroup",
    "CreateUserGroupRequestCanLeaveGroupDirectMembers",
    "CreateUserGroupRequestCanManageGroup",
    "CreateUserGroupRequestCanManageGroupDirectMembers",
    "CreateUserGroupRequestCanMentionGroup",
    "CreateUserGroupRequestCanMentionGroupDirectMembers",
    "CreateUserGroupRequestCanRemoveMembersGroup",
    "CreateUserGroupRequestCanRemoveMembersGroupDirectMembers",
    "CreateUserGroupResponse",
    "CreateUserResponse",
    "GetAlertWordsResponse",
    "GetAttachmentsResponse",
    "GetBotApiKeyResponse",
    "GetIsUserGroupMemberResponse",
    "GetOwnUserResponse",
    "GetUserByEmailResponse",
    "GetUserGroupMembersResponse",
    "GetUserGroupSubgroupsResponse",
    "GetUserGroupsResponse",
    "GetUserGroupsResponseUserGroupsItem",
    "GetUserGroupsResponseUserGroupsItemCanAddMembersGroup",
    "GetUserGroupsResponseUserGroupsItemCanAddMembersGroupDirectMembers",
    "GetUserGroupsResponseUserGroupsItemCanJoinGroup",
    "GetUserGroupsResponseUserGroupsItemCanJoinGroupDirectMembers",
    "GetUserGroupsResponseUserGroupsItemCanLeaveGroup",
    "GetUserGroupsResponseUserGroupsItemCanLeaveGroupDirectMembers",
    "GetUserGroupsResponseUserGroupsItemCanManageGroup",
    "GetUserGroupsResponseUserGroupsItemCanManageGroupDirectMembers",
    "GetUserGroupsResponseUserGroupsItemCanMentionGroup",
    "GetUserGroupsResponseUserGroupsItemCanMentionGroupDirectMembers",
    "GetUserGroupsResponseUserGroupsItemCanRemoveMembersGroup",
    "GetUserGroupsResponseUserGroupsItemCanRemoveMembersGroupDirectMembers",
    "GetUserPresenceResponse",
    "GetUserPresenceResponsePresenceValue",
    "GetUserResponse",
    "GetUserStatusResponse",
    "GetUserStatusResponseStatus",
    "GetUserStatusResponseStatusReactionType",
    "GetUsersResponse",
    "RegenerateApiKeyResponse",
    "RegenerateBotApiKeyResponse",
    "RemoveAlertWordsResponse",
    "SetTypingStatusForMessageEditRequestOp",
    "SetTypingStatusRequestOp",
    "SetTypingStatusRequestType",
    "UpdatePresenceRequestStatus",
    "UpdatePresenceResponse",
    "UpdatePresenceResponsePresencesValue",
    "UpdateSettingsRequestResolvedTopicNoticeAutoReadPolicy",
    "UpdateSettingsRequestTargetUsers",
    "UpdateSettingsRequestWebAnimateImagePreviews",
    "UpdateUserGroupRequestCanAddMembersGroup",
    "UpdateUserGroupRequestCanAddMembersGroupNew",
    "UpdateUserGroupRequestCanAddMembersGroupNewDirectMembers",
    "UpdateUserGroupRequestCanAddMembersGroupOld",
    "UpdateUserGroupRequestCanAddMembersGroupOldDirectMembers",
    "UpdateUserGroupRequestCanJoinGroup",
    "UpdateUserGroupRequestCanJoinGroupNew",
    "UpdateUserGroupRequestCanJoinGroupNewDirectMembers",
    "UpdateUserGroupRequestCanJoinGroupOld",
    "UpdateUserGroupRequestCanJoinGroupOldDirectMembers",
    "UpdateUserGroupRequestCanLeaveGroup",
    "UpdateUserGroupRequestCanLeaveGroupNew",
    "UpdateUserGroupRequestCanLeaveGroupNewDirectMembers",
    "UpdateUserGroupRequestCanLeaveGroupOld",
    "UpdateUserGroupRequestCanLeaveGroupOldDirectMembers",
    "UpdateUserGroupRequestCanManageGroup",
    "UpdateUserGroupRequestCanManageGroupNew",
    "UpdateUserGroupRequestCanManageGroupNewDirectMembers",
    "UpdateUserGroupRequestCanManageGroupOld",
    "UpdateUserGroupRequestCanManageGroupOldDirectMembers",
    "UpdateUserGroupRequestCanMentionGroup",
    "UpdateUserGroupRequestCanMentionGroupNew",
    "UpdateUserGroupRequestCanMentionGroupNewDirectMembers",
    "UpdateUserGroupRequestCanMentionGroupOld",
    "UpdateUserGroupRequestCanMentionGroupOldDirectMembers",
    "UpdateUserGroupRequestCanRemoveMembersGroup",
    "UpdateUserGroupRequestCanRemoveMembersGroupNew",
    "UpdateUserGroupRequestCanRemoveMembersGroupNewDirectMembers",
    "UpdateUserGroupRequestCanRemoveMembersGroupOld",
    "UpdateUserGroupRequestCanRemoveMembersGroupOldDirectMembers",
]
