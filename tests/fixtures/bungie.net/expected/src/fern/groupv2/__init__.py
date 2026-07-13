



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GroupV2AbdicateFoundershipResponse,
        GroupV2AddOptionalConversationResponse,
        GroupV2ApproveAllPendingResponse,
        GroupV2ApprovePendingForListResponse,
        GroupV2ApprovePendingResponse,
        GroupV2BanMemberResponse,
        GroupV2DenyAllPendingResponse,
        GroupV2DenyPendingForListResponse,
        GroupV2EditClanBannerResponse,
        GroupV2EditFounderOptionsResponse,
        GroupV2EditGroupMembershipResponse,
        GroupV2EditGroupResponse,
        GroupV2EditOptionalConversationResponse,
        GroupV2GetAdminsAndFounderOfGroupResponse,
        GroupV2GetAvailableAvatarsResponse,
        GroupV2GetAvailableThemesResponse,
        GroupV2GetBannedMembersOfGroupResponse,
        GroupV2GetGroupByNameResponse,
        GroupV2GetGroupByNameV2Response,
        GroupV2GetGroupOptionalConversationsResponse,
        GroupV2GetGroupResponse,
        GroupV2GetGroupsForMemberResponse,
        GroupV2GetInvitedIndividualsResponse,
        GroupV2GetMembersOfGroupResponse,
        GroupV2GetPendingMembershipsResponse,
        GroupV2GetPotentialGroupsForMemberResponse,
        GroupV2GetRecommendedGroupsResponse,
        GroupV2GetUserClanInviteSettingResponse,
        GroupV2GroupSearchResponse,
        GroupV2IndividualGroupInviteCancelResponse,
        GroupV2IndividualGroupInviteResponse,
        GroupV2KickMemberResponse,
        GroupV2RecoverGroupForFounderResponse,
        GroupV2UnbanMemberResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GroupV2AbdicateFoundershipResponse": ".types",
    "GroupV2AddOptionalConversationResponse": ".types",
    "GroupV2ApproveAllPendingResponse": ".types",
    "GroupV2ApprovePendingForListResponse": ".types",
    "GroupV2ApprovePendingResponse": ".types",
    "GroupV2BanMemberResponse": ".types",
    "GroupV2DenyAllPendingResponse": ".types",
    "GroupV2DenyPendingForListResponse": ".types",
    "GroupV2EditClanBannerResponse": ".types",
    "GroupV2EditFounderOptionsResponse": ".types",
    "GroupV2EditGroupMembershipResponse": ".types",
    "GroupV2EditGroupResponse": ".types",
    "GroupV2EditOptionalConversationResponse": ".types",
    "GroupV2GetAdminsAndFounderOfGroupResponse": ".types",
    "GroupV2GetAvailableAvatarsResponse": ".types",
    "GroupV2GetAvailableThemesResponse": ".types",
    "GroupV2GetBannedMembersOfGroupResponse": ".types",
    "GroupV2GetGroupByNameResponse": ".types",
    "GroupV2GetGroupByNameV2Response": ".types",
    "GroupV2GetGroupOptionalConversationsResponse": ".types",
    "GroupV2GetGroupResponse": ".types",
    "GroupV2GetGroupsForMemberResponse": ".types",
    "GroupV2GetInvitedIndividualsResponse": ".types",
    "GroupV2GetMembersOfGroupResponse": ".types",
    "GroupV2GetPendingMembershipsResponse": ".types",
    "GroupV2GetPotentialGroupsForMemberResponse": ".types",
    "GroupV2GetRecommendedGroupsResponse": ".types",
    "GroupV2GetUserClanInviteSettingResponse": ".types",
    "GroupV2GroupSearchResponse": ".types",
    "GroupV2IndividualGroupInviteCancelResponse": ".types",
    "GroupV2IndividualGroupInviteResponse": ".types",
    "GroupV2KickMemberResponse": ".types",
    "GroupV2RecoverGroupForFounderResponse": ".types",
    "GroupV2UnbanMemberResponse": ".types",
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
