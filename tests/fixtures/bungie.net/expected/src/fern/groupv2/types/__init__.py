



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .group_v2abdicate_foundership_response import GroupV2AbdicateFoundershipResponse
    from .group_v2add_optional_conversation_response import GroupV2AddOptionalConversationResponse
    from .group_v2approve_all_pending_response import GroupV2ApproveAllPendingResponse
    from .group_v2approve_pending_for_list_response import GroupV2ApprovePendingForListResponse
    from .group_v2approve_pending_response import GroupV2ApprovePendingResponse
    from .group_v2ban_member_response import GroupV2BanMemberResponse
    from .group_v2deny_all_pending_response import GroupV2DenyAllPendingResponse
    from .group_v2deny_pending_for_list_response import GroupV2DenyPendingForListResponse
    from .group_v2edit_clan_banner_response import GroupV2EditClanBannerResponse
    from .group_v2edit_founder_options_response import GroupV2EditFounderOptionsResponse
    from .group_v2edit_group_membership_response import GroupV2EditGroupMembershipResponse
    from .group_v2edit_group_response import GroupV2EditGroupResponse
    from .group_v2edit_optional_conversation_response import GroupV2EditOptionalConversationResponse
    from .group_v2get_admins_and_founder_of_group_response import GroupV2GetAdminsAndFounderOfGroupResponse
    from .group_v2get_available_avatars_response import GroupV2GetAvailableAvatarsResponse
    from .group_v2get_available_themes_response import GroupV2GetAvailableThemesResponse
    from .group_v2get_banned_members_of_group_response import GroupV2GetBannedMembersOfGroupResponse
    from .group_v2get_group_by_name_response import GroupV2GetGroupByNameResponse
    from .group_v2get_group_by_name_v2response import GroupV2GetGroupByNameV2Response
    from .group_v2get_group_optional_conversations_response import GroupV2GetGroupOptionalConversationsResponse
    from .group_v2get_group_response import GroupV2GetGroupResponse
    from .group_v2get_groups_for_member_response import GroupV2GetGroupsForMemberResponse
    from .group_v2get_invited_individuals_response import GroupV2GetInvitedIndividualsResponse
    from .group_v2get_members_of_group_response import GroupV2GetMembersOfGroupResponse
    from .group_v2get_pending_memberships_response import GroupV2GetPendingMembershipsResponse
    from .group_v2get_potential_groups_for_member_response import GroupV2GetPotentialGroupsForMemberResponse
    from .group_v2get_recommended_groups_response import GroupV2GetRecommendedGroupsResponse
    from .group_v2get_user_clan_invite_setting_response import GroupV2GetUserClanInviteSettingResponse
    from .group_v2group_search_response import GroupV2GroupSearchResponse
    from .group_v2individual_group_invite_cancel_response import GroupV2IndividualGroupInviteCancelResponse
    from .group_v2individual_group_invite_response import GroupV2IndividualGroupInviteResponse
    from .group_v2kick_member_response import GroupV2KickMemberResponse
    from .group_v2recover_group_for_founder_response import GroupV2RecoverGroupForFounderResponse
    from .group_v2unban_member_response import GroupV2UnbanMemberResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GroupV2AbdicateFoundershipResponse": ".group_v2abdicate_foundership_response",
    "GroupV2AddOptionalConversationResponse": ".group_v2add_optional_conversation_response",
    "GroupV2ApproveAllPendingResponse": ".group_v2approve_all_pending_response",
    "GroupV2ApprovePendingForListResponse": ".group_v2approve_pending_for_list_response",
    "GroupV2ApprovePendingResponse": ".group_v2approve_pending_response",
    "GroupV2BanMemberResponse": ".group_v2ban_member_response",
    "GroupV2DenyAllPendingResponse": ".group_v2deny_all_pending_response",
    "GroupV2DenyPendingForListResponse": ".group_v2deny_pending_for_list_response",
    "GroupV2EditClanBannerResponse": ".group_v2edit_clan_banner_response",
    "GroupV2EditFounderOptionsResponse": ".group_v2edit_founder_options_response",
    "GroupV2EditGroupMembershipResponse": ".group_v2edit_group_membership_response",
    "GroupV2EditGroupResponse": ".group_v2edit_group_response",
    "GroupV2EditOptionalConversationResponse": ".group_v2edit_optional_conversation_response",
    "GroupV2GetAdminsAndFounderOfGroupResponse": ".group_v2get_admins_and_founder_of_group_response",
    "GroupV2GetAvailableAvatarsResponse": ".group_v2get_available_avatars_response",
    "GroupV2GetAvailableThemesResponse": ".group_v2get_available_themes_response",
    "GroupV2GetBannedMembersOfGroupResponse": ".group_v2get_banned_members_of_group_response",
    "GroupV2GetGroupByNameResponse": ".group_v2get_group_by_name_response",
    "GroupV2GetGroupByNameV2Response": ".group_v2get_group_by_name_v2response",
    "GroupV2GetGroupOptionalConversationsResponse": ".group_v2get_group_optional_conversations_response",
    "GroupV2GetGroupResponse": ".group_v2get_group_response",
    "GroupV2GetGroupsForMemberResponse": ".group_v2get_groups_for_member_response",
    "GroupV2GetInvitedIndividualsResponse": ".group_v2get_invited_individuals_response",
    "GroupV2GetMembersOfGroupResponse": ".group_v2get_members_of_group_response",
    "GroupV2GetPendingMembershipsResponse": ".group_v2get_pending_memberships_response",
    "GroupV2GetPotentialGroupsForMemberResponse": ".group_v2get_potential_groups_for_member_response",
    "GroupV2GetRecommendedGroupsResponse": ".group_v2get_recommended_groups_response",
    "GroupV2GetUserClanInviteSettingResponse": ".group_v2get_user_clan_invite_setting_response",
    "GroupV2GroupSearchResponse": ".group_v2group_search_response",
    "GroupV2IndividualGroupInviteCancelResponse": ".group_v2individual_group_invite_cancel_response",
    "GroupV2IndividualGroupInviteResponse": ".group_v2individual_group_invite_response",
    "GroupV2KickMemberResponse": ".group_v2kick_member_response",
    "GroupV2RecoverGroupForFounderResponse": ".group_v2recover_group_for_founder_response",
    "GroupV2UnbanMemberResponse": ".group_v2unban_member_response",
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
    "GroupV2AbdicateFoundershipResponse",
    "GroupV2AddOptionalConversationResponse",
    "GroupV2ApproveAllPendingResponse",
    "GroupV2ApprovePendingForListResponse",
    "GroupV2ApprovePendingResponse",
    "GroupV2BanMemberResponse",
    "GroupV2DenyAllPendingResponse",
    "GroupV2DenyPendingForListResponse",
    "GroupV2EditClanBannerResponse",
    "GroupV2EditFounderOptionsResponse",
    "GroupV2EditGroupMembershipResponse",
    "GroupV2EditGroupResponse",
    "GroupV2EditOptionalConversationResponse",
    "GroupV2GetAdminsAndFounderOfGroupResponse",
    "GroupV2GetAvailableAvatarsResponse",
    "GroupV2GetAvailableThemesResponse",
    "GroupV2GetBannedMembersOfGroupResponse",
    "GroupV2GetGroupByNameResponse",
    "GroupV2GetGroupByNameV2Response",
    "GroupV2GetGroupOptionalConversationsResponse",
    "GroupV2GetGroupResponse",
    "GroupV2GetGroupsForMemberResponse",
    "GroupV2GetInvitedIndividualsResponse",
    "GroupV2GetMembersOfGroupResponse",
    "GroupV2GetPendingMembershipsResponse",
    "GroupV2GetPotentialGroupsForMemberResponse",
    "GroupV2GetRecommendedGroupsResponse",
    "GroupV2GetUserClanInviteSettingResponse",
    "GroupV2GroupSearchResponse",
    "GroupV2IndividualGroupInviteCancelResponse",
    "GroupV2IndividualGroupInviteResponse",
    "GroupV2KickMemberResponse",
    "GroupV2RecoverGroupForFounderResponse",
    "GroupV2UnbanMemberResponse",
]
