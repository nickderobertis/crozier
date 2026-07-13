

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGroupv2Client, RawGroupv2Client
from .types.group_v2abdicate_foundership_response import GroupV2AbdicateFoundershipResponse
from .types.group_v2add_optional_conversation_response import GroupV2AddOptionalConversationResponse
from .types.group_v2approve_all_pending_response import GroupV2ApproveAllPendingResponse
from .types.group_v2approve_pending_for_list_response import GroupV2ApprovePendingForListResponse
from .types.group_v2approve_pending_response import GroupV2ApprovePendingResponse
from .types.group_v2ban_member_response import GroupV2BanMemberResponse
from .types.group_v2deny_all_pending_response import GroupV2DenyAllPendingResponse
from .types.group_v2deny_pending_for_list_response import GroupV2DenyPendingForListResponse
from .types.group_v2edit_clan_banner_response import GroupV2EditClanBannerResponse
from .types.group_v2edit_founder_options_response import GroupV2EditFounderOptionsResponse
from .types.group_v2edit_group_membership_response import GroupV2EditGroupMembershipResponse
from .types.group_v2edit_group_response import GroupV2EditGroupResponse
from .types.group_v2edit_optional_conversation_response import GroupV2EditOptionalConversationResponse
from .types.group_v2get_admins_and_founder_of_group_response import GroupV2GetAdminsAndFounderOfGroupResponse
from .types.group_v2get_available_avatars_response import GroupV2GetAvailableAvatarsResponse
from .types.group_v2get_available_themes_response import GroupV2GetAvailableThemesResponse
from .types.group_v2get_banned_members_of_group_response import GroupV2GetBannedMembersOfGroupResponse
from .types.group_v2get_group_by_name_response import GroupV2GetGroupByNameResponse
from .types.group_v2get_group_by_name_v2response import GroupV2GetGroupByNameV2Response
from .types.group_v2get_group_optional_conversations_response import GroupV2GetGroupOptionalConversationsResponse
from .types.group_v2get_group_response import GroupV2GetGroupResponse
from .types.group_v2get_groups_for_member_response import GroupV2GetGroupsForMemberResponse
from .types.group_v2get_invited_individuals_response import GroupV2GetInvitedIndividualsResponse
from .types.group_v2get_members_of_group_response import GroupV2GetMembersOfGroupResponse
from .types.group_v2get_pending_memberships_response import GroupV2GetPendingMembershipsResponse
from .types.group_v2get_potential_groups_for_member_response import GroupV2GetPotentialGroupsForMemberResponse
from .types.group_v2get_recommended_groups_response import GroupV2GetRecommendedGroupsResponse
from .types.group_v2get_user_clan_invite_setting_response import GroupV2GetUserClanInviteSettingResponse
from .types.group_v2group_search_response import GroupV2GroupSearchResponse
from .types.group_v2individual_group_invite_cancel_response import GroupV2IndividualGroupInviteCancelResponse
from .types.group_v2individual_group_invite_response import GroupV2IndividualGroupInviteResponse
from .types.group_v2kick_member_response import GroupV2KickMemberResponse
from .types.group_v2recover_group_for_founder_response import GroupV2RecoverGroupForFounderResponse
from .types.group_v2unban_member_response import GroupV2UnbanMemberResponse


class Groupv2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGroupv2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGroupv2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGroupv2Client
        """
        return self._raw_client

    def getavailableavatars(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetAvailableAvatarsResponse:
        """
        Returns a list of all available group avatars for the signed-in user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetAvailableAvatarsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getavailableavatars()
        """
        _response = self._raw_client.getavailableavatars(request_options=request_options)
        return _response.data

    def getavailablethemes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetAvailableThemesResponse:
        """
        Returns a list of all available group themes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetAvailableThemesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getavailablethemes()
        """
        _response = self._raw_client.getavailablethemes(request_options=request_options)
        return _response.data

    def getuserclaninvitesetting(
        self, m_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetUserClanInviteSettingResponse:
        """
        Gets the state of the user's clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.

        Parameters
        ----------
        m_type : int
            The Destiny membership type of the account we wish to access settings.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetUserClanInviteSettingResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getuserclaninvitesetting(
            m_type=1,
        )
        """
        _response = self._raw_client.getuserclaninvitesetting(m_type, request_options=request_options)
        return _response.data

    def getgroupbyname(
        self, group_name: str, group_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetGroupByNameResponse:
        """
        Get information about a specific group with the given name and type.

        Parameters
        ----------
        group_name : str
            Exact name of the group to find.

        group_type : int
            Type of group to find.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetGroupByNameResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getgroupbyname(
            group_name="groupName",
            group_type=1,
        )
        """
        _response = self._raw_client.getgroupbyname(group_name, group_type, request_options=request_options)
        return _response.data

    def getgroupbynamev2(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetGroupByNameV2Response:
        """
        Get information about a specific group with the given name and type. The POST version.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetGroupByNameV2Response
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getgroupbynamev2()
        """
        _response = self._raw_client.getgroupbynamev2(request_options=request_options)
        return _response.data

    def getrecommendedgroups(
        self, group_type: int, create_date_range: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetRecommendedGroupsResponse:
        """
        Gets groups recommended for you based on the groups to whom those you follow belong.

        Parameters
        ----------
        group_type : int
            Type of groups requested

        create_date_range : int
            Requested range in which to pull recommended groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetRecommendedGroupsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getrecommendedgroups(
            group_type=1,
            create_date_range=1,
        )
        """
        _response = self._raw_client.getrecommendedgroups(
            group_type, create_date_range, request_options=request_options
        )
        return _response.data

    def recovergroupforfounder(
        self,
        membership_type: int,
        membership_id: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2RecoverGroupForFounderResponse:
        """
        Allows a founder to manually recover a group they can see in game but not on bungie.net

        Parameters
        ----------
        membership_type : int
            Membership type of the supplied membership ID.

        membership_id : int
            Membership ID to for which to find founded groups.

        group_type : int
            Type of group the supplied member founded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2RecoverGroupForFounderResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.recovergroupforfounder(
            membership_type=1,
            membership_id=1000000,
            group_type=1,
        )
        """
        _response = self._raw_client.recovergroupforfounder(
            membership_type, membership_id, group_type, request_options=request_options
        )
        return _response.data

    def groupsearch(self, *, request_options: typing.Optional[RequestOptions] = None) -> GroupV2GroupSearchResponse:
        """
        Search for Groups.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GroupSearchResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.groupsearch()
        """
        _response = self._raw_client.groupsearch(request_options=request_options)
        return _response.data

    def getpotentialgroupsformember(
        self,
        membership_type: int,
        membership_id: int,
        filter: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2GetPotentialGroupsForMemberResponse:
        """
        Get information about the groups that a given member has applied to or been invited to.

        Parameters
        ----------
        membership_type : int
            Membership type of the supplied membership ID.

        membership_id : int
            Membership ID to for which to find applied groups.

        filter : int
            Filter apply to list of potential joined groups.

        group_type : int
            Type of group the supplied member applied.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetPotentialGroupsForMemberResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getpotentialgroupsformember(
            membership_type=1,
            membership_id=1000000,
            filter=1,
            group_type=1,
        )
        """
        _response = self._raw_client.getpotentialgroupsformember(
            membership_type, membership_id, filter, group_type, request_options=request_options
        )
        return _response.data

    def getgroupsformember(
        self,
        membership_type: int,
        membership_id: int,
        filter: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2GetGroupsForMemberResponse:
        """
        Get information about the groups that a given member has joined.

        Parameters
        ----------
        membership_type : int
            Membership type of the supplied membership ID.

        membership_id : int
            Membership ID to for which to find founded groups.

        filter : int
            Filter apply to list of joined groups.

        group_type : int
            Type of group the supplied member founded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetGroupsForMemberResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getgroupsformember(
            membership_type=1,
            membership_id=1000000,
            filter=1,
            group_type=1,
        )
        """
        _response = self._raw_client.getgroupsformember(
            membership_type, membership_id, filter, group_type, request_options=request_options
        )
        return _response.data

    def getgroup(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetGroupResponse:
        """
        Get information about a specific group of the given ID.

        Parameters
        ----------
        group_id : int
            Requested group's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetGroupResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getgroup(
            group_id=1000000,
        )
        """
        _response = self._raw_client.getgroup(group_id, request_options=request_options)
        return _response.data

    def abdicatefoundership(
        self,
        group_id: int,
        membership_type: int,
        founder_id_new: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2AbdicateFoundershipResponse:
        """
        An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

        Parameters
        ----------
        group_id : int
            The target group id.

        membership_type : int
            Membership type of the provided founderIdNew.

        founder_id_new : int
            The new founder for this group. Must already be a group admin.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2AbdicateFoundershipResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.abdicatefoundership(
            group_id=1000000,
            membership_type=1,
            founder_id_new=1000000,
        )
        """
        _response = self._raw_client.abdicatefoundership(
            group_id, membership_type, founder_id_new, request_options=request_options
        )
        return _response.data

    def getadminsandfounderofgroup(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetAdminsAndFounderOfGroupResponse:
        """
        Get the list of members in a given group who are of admin level or higher.

        Parameters
        ----------
        group_id : int
            The ID of the group.

        currentpage : int
            Page number (starting with 1). Each page has a fixed size of 50 items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetAdminsAndFounderOfGroupResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getadminsandfounderofgroup(
            group_id=1000000,
            currentpage=1,
        )
        """
        _response = self._raw_client.getadminsandfounderofgroup(
            group_id, currentpage=currentpage, request_options=request_options
        )
        return _response.data

    def getbannedmembersofgroup(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetBannedMembersOfGroupResponse:
        """
        Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.

        Parameters
        ----------
        group_id : int
            Group ID whose banned members you are fetching

        currentpage : int
            Page number (starting with 1). Each page has a fixed size of 50 entries.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetBannedMembersOfGroupResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getbannedmembersofgroup(
            group_id=1000000,
            currentpage=1,
        )
        """
        _response = self._raw_client.getbannedmembersofgroup(
            group_id, currentpage=currentpage, request_options=request_options
        )
        return _response.data

    def editgroup(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2EditGroupResponse:
        """
        Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.

        Parameters
        ----------
        group_id : int
            Group ID of the group to edit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2EditGroupResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.editgroup(
            group_id=1000000,
        )
        """
        _response = self._raw_client.editgroup(group_id, request_options=request_options)
        return _response.data

    def editclanbanner(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2EditClanBannerResponse:
        """
        Edit an existing group's clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.

        Parameters
        ----------
        group_id : int
            Group ID of the group to edit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2EditClanBannerResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.editclanbanner(
            group_id=1000000,
        )
        """
        _response = self._raw_client.editclanbanner(group_id, request_options=request_options)
        return _response.data

    def editfounderoptions(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2EditFounderOptionsResponse:
        """
        Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.

        Parameters
        ----------
        group_id : int
            Group ID of the group to edit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2EditFounderOptionsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.editfounderoptions(
            group_id=1000000,
        )
        """
        _response = self._raw_client.editfounderoptions(group_id, request_options=request_options)
        return _response.data

    def getmembersofgroup(
        self,
        group_id: int,
        *,
        currentpage: int,
        member_type: typing.Optional[int] = None,
        name_search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2GetMembersOfGroupResponse:
        """
        Get the list of members in a given group.

        Parameters
        ----------
        group_id : int
            The ID of the group.

        currentpage : int
            Page number (starting with 1). Each page has a fixed size of 50 items per page.

        member_type : typing.Optional[int]
            Filter out other member types. Use None for all members.

        name_search : typing.Optional[str]
            The name fragment upon which a search should be executed for members with matching display or unique names.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetMembersOfGroupResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getmembersofgroup(
            group_id=1000000,
            currentpage=1,
        )
        """
        _response = self._raw_client.getmembersofgroup(
            group_id,
            currentpage=currentpage,
            member_type=member_type,
            name_search=name_search,
            request_options=request_options,
        )
        return _response.data

    def approvepending(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2ApprovePendingResponse:
        """
        Approve the given membershipId to join the group/clan as long as they have applied.

        Parameters
        ----------
        group_id : int
            ID of the group.

        membership_type : int
            Membership type of the supplied membership ID.

        membership_id : int
            The membership id being approved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2ApprovePendingResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.approvepending(
            group_id=1000000,
            membership_type=1,
            membership_id=1000000,
        )
        """
        _response = self._raw_client.approvepending(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    def approveallpending(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2ApproveAllPendingResponse:
        """
        Approve all of the pending users for the given group.

        Parameters
        ----------
        group_id : int
            ID of the group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2ApproveAllPendingResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.approveallpending(
            group_id=1000000,
        )
        """
        _response = self._raw_client.approveallpending(group_id, request_options=request_options)
        return _response.data

    def approvependingforlist(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2ApprovePendingForListResponse:
        """
        Approve all of the pending users for the given group.

        Parameters
        ----------
        group_id : int
            ID of the group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2ApprovePendingForListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.approvependingforlist(
            group_id=1000000,
        )
        """
        _response = self._raw_client.approvependingforlist(group_id, request_options=request_options)
        return _response.data

    def denyallpending(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2DenyAllPendingResponse:
        """
        Deny all of the pending users for the given group.

        Parameters
        ----------
        group_id : int
            ID of the group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2DenyAllPendingResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.denyallpending(
            group_id=1000000,
        )
        """
        _response = self._raw_client.denyallpending(group_id, request_options=request_options)
        return _response.data

    def denypendingforlist(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2DenyPendingForListResponse:
        """
        Deny all of the pending users for the given group that match the passed-in .

        Parameters
        ----------
        group_id : int
            ID of the group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2DenyPendingForListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.denypendingforlist(
            group_id=1000000,
        )
        """
        _response = self._raw_client.denypendingforlist(group_id, request_options=request_options)
        return _response.data

    def individualgroupinvite(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2IndividualGroupInviteResponse:
        """
        Invite a user to join this group.

        Parameters
        ----------
        group_id : int
            ID of the group you would like to join.

        membership_type : int
            MembershipType of the account being invited.

        membership_id : int
            Membership id of the account being invited.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2IndividualGroupInviteResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.individualgroupinvite(
            group_id=1000000,
            membership_type=1,
            membership_id=1000000,
        )
        """
        _response = self._raw_client.individualgroupinvite(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    def individualgroupinvitecancel(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2IndividualGroupInviteCancelResponse:
        """
        Cancels a pending invitation to join a group.

        Parameters
        ----------
        group_id : int
            ID of the group you would like to join.

        membership_type : int
            MembershipType of the account being cancelled.

        membership_id : int
            Membership id of the account being cancelled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2IndividualGroupInviteCancelResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.individualgroupinvitecancel(
            group_id=1000000,
            membership_type=1,
            membership_id=1000000,
        )
        """
        _response = self._raw_client.individualgroupinvitecancel(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    def getinvitedindividuals(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetInvitedIndividualsResponse:
        """
        Get the list of users who have been invited into the group.

        Parameters
        ----------
        group_id : int
            ID of the group.

        currentpage : int
            Page number (starting with 1). Each page has a fixed size of 50 items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetInvitedIndividualsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getinvitedindividuals(
            group_id=1000000,
            currentpage=1,
        )
        """
        _response = self._raw_client.getinvitedindividuals(
            group_id, currentpage=currentpage, request_options=request_options
        )
        return _response.data

    def getpendingmemberships(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetPendingMembershipsResponse:
        """
        Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.

        Parameters
        ----------
        group_id : int
            ID of the group.

        currentpage : int
            Page number (starting with 1). Each page has a fixed size of 50 items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetPendingMembershipsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getpendingmemberships(
            group_id=1000000,
            currentpage=1,
        )
        """
        _response = self._raw_client.getpendingmemberships(
            group_id, currentpage=currentpage, request_options=request_options
        )
        return _response.data

    def banmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2BanMemberResponse:
        """
        Bans the requested member from the requested group for the specified period of time.

        Parameters
        ----------
        group_id : int
            Group ID that has the member to ban.

        membership_type : int
            Membership type of the provided membership ID.

        membership_id : int
            Membership ID of the member to ban from the group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2BanMemberResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.banmember(
            group_id=1000000,
            membership_type=1,
            membership_id=1000000,
        )
        """
        _response = self._raw_client.banmember(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    def kickmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2KickMemberResponse:
        """
        Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.

        Parameters
        ----------
        group_id : int
            Group ID to kick the user from.

        membership_type : int
            Membership type of the provided membership ID.

        membership_id : int
            Membership ID to kick.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2KickMemberResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.kickmember(
            group_id=1000000,
            membership_type=1,
            membership_id=1000000,
        )
        """
        _response = self._raw_client.kickmember(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    def editgroupmembership(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        member_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2EditGroupMembershipResponse:
        """
        Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.

        Parameters
        ----------
        group_id : int
            ID of the group to which the member belongs.

        membership_type : int
            Membership type of the provide membership ID.

        membership_id : int
            Membership ID to modify.

        member_type : int
            New membertype for the specified member.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2EditGroupMembershipResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.editgroupmembership(
            group_id=1000000,
            membership_type=1,
            membership_id=1000000,
            member_type=1,
        )
        """
        _response = self._raw_client.editgroupmembership(
            group_id, membership_type, membership_id, member_type, request_options=request_options
        )
        return _response.data

    def unbanmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2UnbanMemberResponse:
        """
        Unbans the requested member, allowing them to re-apply for membership.

        Parameters
        ----------
        group_id : int


        membership_type : int
            Membership type of the provided membership ID.

        membership_id : int
            Membership ID of the member to unban from the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2UnbanMemberResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.unbanmember(
            group_id=1000000,
            membership_type=1,
            membership_id=1000000,
        )
        """
        _response = self._raw_client.unbanmember(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    def getgroupoptionalconversations(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetGroupOptionalConversationsResponse:
        """
        Gets a list of available optional conversation channels and their settings.

        Parameters
        ----------
        group_id : int
            Requested group's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetGroupOptionalConversationsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.getgroupoptionalconversations(
            group_id=1000000,
        )
        """
        _response = self._raw_client.getgroupoptionalconversations(group_id, request_options=request_options)
        return _response.data

    def addoptionalconversation(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2AddOptionalConversationResponse:
        """
        Add a new optional conversation/chat channel. Requires admin permissions to the group.

        Parameters
        ----------
        group_id : int
            Group ID of the group to edit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2AddOptionalConversationResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.addoptionalconversation(
            group_id=1000000,
        )
        """
        _response = self._raw_client.addoptionalconversation(group_id, request_options=request_options)
        return _response.data

    def editoptionalconversation(
        self, group_id: int, conversation_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2EditOptionalConversationResponse:
        """
        Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.

        Parameters
        ----------
        group_id : int
            Group ID of the group to edit.

        conversation_id : int
            Conversation Id of the channel being edited.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2EditOptionalConversationResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.groupv2.editoptionalconversation(
            group_id=1000000,
            conversation_id=1000000,
        )
        """
        _response = self._raw_client.editoptionalconversation(
            group_id, conversation_id, request_options=request_options
        )
        return _response.data


class AsyncGroupv2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGroupv2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGroupv2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGroupv2Client
        """
        return self._raw_client

    async def getavailableavatars(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetAvailableAvatarsResponse:
        """
        Returns a list of all available group avatars for the signed-in user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetAvailableAvatarsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getavailableavatars()


        asyncio.run(main())
        """
        _response = await self._raw_client.getavailableavatars(request_options=request_options)
        return _response.data

    async def getavailablethemes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetAvailableThemesResponse:
        """
        Returns a list of all available group themes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetAvailableThemesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getavailablethemes()


        asyncio.run(main())
        """
        _response = await self._raw_client.getavailablethemes(request_options=request_options)
        return _response.data

    async def getuserclaninvitesetting(
        self, m_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetUserClanInviteSettingResponse:
        """
        Gets the state of the user's clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.

        Parameters
        ----------
        m_type : int
            The Destiny membership type of the account we wish to access settings.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetUserClanInviteSettingResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getuserclaninvitesetting(
                m_type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getuserclaninvitesetting(m_type, request_options=request_options)
        return _response.data

    async def getgroupbyname(
        self, group_name: str, group_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetGroupByNameResponse:
        """
        Get information about a specific group with the given name and type.

        Parameters
        ----------
        group_name : str
            Exact name of the group to find.

        group_type : int
            Type of group to find.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetGroupByNameResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getgroupbyname(
                group_name="groupName",
                group_type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getgroupbyname(group_name, group_type, request_options=request_options)
        return _response.data

    async def getgroupbynamev2(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetGroupByNameV2Response:
        """
        Get information about a specific group with the given name and type. The POST version.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetGroupByNameV2Response
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getgroupbynamev2()


        asyncio.run(main())
        """
        _response = await self._raw_client.getgroupbynamev2(request_options=request_options)
        return _response.data

    async def getrecommendedgroups(
        self, group_type: int, create_date_range: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetRecommendedGroupsResponse:
        """
        Gets groups recommended for you based on the groups to whom those you follow belong.

        Parameters
        ----------
        group_type : int
            Type of groups requested

        create_date_range : int
            Requested range in which to pull recommended groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetRecommendedGroupsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getrecommendedgroups(
                group_type=1,
                create_date_range=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getrecommendedgroups(
            group_type, create_date_range, request_options=request_options
        )
        return _response.data

    async def recovergroupforfounder(
        self,
        membership_type: int,
        membership_id: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2RecoverGroupForFounderResponse:
        """
        Allows a founder to manually recover a group they can see in game but not on bungie.net

        Parameters
        ----------
        membership_type : int
            Membership type of the supplied membership ID.

        membership_id : int
            Membership ID to for which to find founded groups.

        group_type : int
            Type of group the supplied member founded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2RecoverGroupForFounderResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.recovergroupforfounder(
                membership_type=1,
                membership_id=1000000,
                group_type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.recovergroupforfounder(
            membership_type, membership_id, group_type, request_options=request_options
        )
        return _response.data

    async def groupsearch(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GroupSearchResponse:
        """
        Search for Groups.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GroupSearchResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.groupsearch()


        asyncio.run(main())
        """
        _response = await self._raw_client.groupsearch(request_options=request_options)
        return _response.data

    async def getpotentialgroupsformember(
        self,
        membership_type: int,
        membership_id: int,
        filter: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2GetPotentialGroupsForMemberResponse:
        """
        Get information about the groups that a given member has applied to or been invited to.

        Parameters
        ----------
        membership_type : int
            Membership type of the supplied membership ID.

        membership_id : int
            Membership ID to for which to find applied groups.

        filter : int
            Filter apply to list of potential joined groups.

        group_type : int
            Type of group the supplied member applied.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetPotentialGroupsForMemberResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getpotentialgroupsformember(
                membership_type=1,
                membership_id=1000000,
                filter=1,
                group_type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpotentialgroupsformember(
            membership_type, membership_id, filter, group_type, request_options=request_options
        )
        return _response.data

    async def getgroupsformember(
        self,
        membership_type: int,
        membership_id: int,
        filter: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2GetGroupsForMemberResponse:
        """
        Get information about the groups that a given member has joined.

        Parameters
        ----------
        membership_type : int
            Membership type of the supplied membership ID.

        membership_id : int
            Membership ID to for which to find founded groups.

        filter : int
            Filter apply to list of joined groups.

        group_type : int
            Type of group the supplied member founded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetGroupsForMemberResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getgroupsformember(
                membership_type=1,
                membership_id=1000000,
                filter=1,
                group_type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getgroupsformember(
            membership_type, membership_id, filter, group_type, request_options=request_options
        )
        return _response.data

    async def getgroup(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetGroupResponse:
        """
        Get information about a specific group of the given ID.

        Parameters
        ----------
        group_id : int
            Requested group's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetGroupResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getgroup(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getgroup(group_id, request_options=request_options)
        return _response.data

    async def abdicatefoundership(
        self,
        group_id: int,
        membership_type: int,
        founder_id_new: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2AbdicateFoundershipResponse:
        """
        An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

        Parameters
        ----------
        group_id : int
            The target group id.

        membership_type : int
            Membership type of the provided founderIdNew.

        founder_id_new : int
            The new founder for this group. Must already be a group admin.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2AbdicateFoundershipResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.abdicatefoundership(
                group_id=1000000,
                membership_type=1,
                founder_id_new=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.abdicatefoundership(
            group_id, membership_type, founder_id_new, request_options=request_options
        )
        return _response.data

    async def getadminsandfounderofgroup(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetAdminsAndFounderOfGroupResponse:
        """
        Get the list of members in a given group who are of admin level or higher.

        Parameters
        ----------
        group_id : int
            The ID of the group.

        currentpage : int
            Page number (starting with 1). Each page has a fixed size of 50 items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetAdminsAndFounderOfGroupResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getadminsandfounderofgroup(
                group_id=1000000,
                currentpage=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getadminsandfounderofgroup(
            group_id, currentpage=currentpage, request_options=request_options
        )
        return _response.data

    async def getbannedmembersofgroup(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetBannedMembersOfGroupResponse:
        """
        Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.

        Parameters
        ----------
        group_id : int
            Group ID whose banned members you are fetching

        currentpage : int
            Page number (starting with 1). Each page has a fixed size of 50 entries.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetBannedMembersOfGroupResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getbannedmembersofgroup(
                group_id=1000000,
                currentpage=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getbannedmembersofgroup(
            group_id, currentpage=currentpage, request_options=request_options
        )
        return _response.data

    async def editgroup(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2EditGroupResponse:
        """
        Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.

        Parameters
        ----------
        group_id : int
            Group ID of the group to edit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2EditGroupResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.editgroup(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.editgroup(group_id, request_options=request_options)
        return _response.data

    async def editclanbanner(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2EditClanBannerResponse:
        """
        Edit an existing group's clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.

        Parameters
        ----------
        group_id : int
            Group ID of the group to edit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2EditClanBannerResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.editclanbanner(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.editclanbanner(group_id, request_options=request_options)
        return _response.data

    async def editfounderoptions(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2EditFounderOptionsResponse:
        """
        Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.

        Parameters
        ----------
        group_id : int
            Group ID of the group to edit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2EditFounderOptionsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.editfounderoptions(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.editfounderoptions(group_id, request_options=request_options)
        return _response.data

    async def getmembersofgroup(
        self,
        group_id: int,
        *,
        currentpage: int,
        member_type: typing.Optional[int] = None,
        name_search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2GetMembersOfGroupResponse:
        """
        Get the list of members in a given group.

        Parameters
        ----------
        group_id : int
            The ID of the group.

        currentpage : int
            Page number (starting with 1). Each page has a fixed size of 50 items per page.

        member_type : typing.Optional[int]
            Filter out other member types. Use None for all members.

        name_search : typing.Optional[str]
            The name fragment upon which a search should be executed for members with matching display or unique names.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetMembersOfGroupResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getmembersofgroup(
                group_id=1000000,
                currentpage=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getmembersofgroup(
            group_id,
            currentpage=currentpage,
            member_type=member_type,
            name_search=name_search,
            request_options=request_options,
        )
        return _response.data

    async def approvepending(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2ApprovePendingResponse:
        """
        Approve the given membershipId to join the group/clan as long as they have applied.

        Parameters
        ----------
        group_id : int
            ID of the group.

        membership_type : int
            Membership type of the supplied membership ID.

        membership_id : int
            The membership id being approved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2ApprovePendingResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.approvepending(
                group_id=1000000,
                membership_type=1,
                membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approvepending(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    async def approveallpending(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2ApproveAllPendingResponse:
        """
        Approve all of the pending users for the given group.

        Parameters
        ----------
        group_id : int
            ID of the group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2ApproveAllPendingResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.approveallpending(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approveallpending(group_id, request_options=request_options)
        return _response.data

    async def approvependingforlist(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2ApprovePendingForListResponse:
        """
        Approve all of the pending users for the given group.

        Parameters
        ----------
        group_id : int
            ID of the group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2ApprovePendingForListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.approvependingforlist(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approvependingforlist(group_id, request_options=request_options)
        return _response.data

    async def denyallpending(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2DenyAllPendingResponse:
        """
        Deny all of the pending users for the given group.

        Parameters
        ----------
        group_id : int
            ID of the group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2DenyAllPendingResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.denyallpending(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.denyallpending(group_id, request_options=request_options)
        return _response.data

    async def denypendingforlist(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2DenyPendingForListResponse:
        """
        Deny all of the pending users for the given group that match the passed-in .

        Parameters
        ----------
        group_id : int
            ID of the group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2DenyPendingForListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.denypendingforlist(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.denypendingforlist(group_id, request_options=request_options)
        return _response.data

    async def individualgroupinvite(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2IndividualGroupInviteResponse:
        """
        Invite a user to join this group.

        Parameters
        ----------
        group_id : int
            ID of the group you would like to join.

        membership_type : int
            MembershipType of the account being invited.

        membership_id : int
            Membership id of the account being invited.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2IndividualGroupInviteResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.individualgroupinvite(
                group_id=1000000,
                membership_type=1,
                membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.individualgroupinvite(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    async def individualgroupinvitecancel(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2IndividualGroupInviteCancelResponse:
        """
        Cancels a pending invitation to join a group.

        Parameters
        ----------
        group_id : int
            ID of the group you would like to join.

        membership_type : int
            MembershipType of the account being cancelled.

        membership_id : int
            Membership id of the account being cancelled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2IndividualGroupInviteCancelResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.individualgroupinvitecancel(
                group_id=1000000,
                membership_type=1,
                membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.individualgroupinvitecancel(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    async def getinvitedindividuals(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetInvitedIndividualsResponse:
        """
        Get the list of users who have been invited into the group.

        Parameters
        ----------
        group_id : int
            ID of the group.

        currentpage : int
            Page number (starting with 1). Each page has a fixed size of 50 items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetInvitedIndividualsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getinvitedindividuals(
                group_id=1000000,
                currentpage=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getinvitedindividuals(
            group_id, currentpage=currentpage, request_options=request_options
        )
        return _response.data

    async def getpendingmemberships(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetPendingMembershipsResponse:
        """
        Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.

        Parameters
        ----------
        group_id : int
            ID of the group.

        currentpage : int
            Page number (starting with 1). Each page has a fixed size of 50 items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetPendingMembershipsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getpendingmemberships(
                group_id=1000000,
                currentpage=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpendingmemberships(
            group_id, currentpage=currentpage, request_options=request_options
        )
        return _response.data

    async def banmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2BanMemberResponse:
        """
        Bans the requested member from the requested group for the specified period of time.

        Parameters
        ----------
        group_id : int
            Group ID that has the member to ban.

        membership_type : int
            Membership type of the provided membership ID.

        membership_id : int
            Membership ID of the member to ban from the group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2BanMemberResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.banmember(
                group_id=1000000,
                membership_type=1,
                membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.banmember(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    async def kickmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2KickMemberResponse:
        """
        Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.

        Parameters
        ----------
        group_id : int
            Group ID to kick the user from.

        membership_type : int
            Membership type of the provided membership ID.

        membership_id : int
            Membership ID to kick.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2KickMemberResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.kickmember(
                group_id=1000000,
                membership_type=1,
                membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.kickmember(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    async def editgroupmembership(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        member_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2EditGroupMembershipResponse:
        """
        Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.

        Parameters
        ----------
        group_id : int
            ID of the group to which the member belongs.

        membership_type : int
            Membership type of the provide membership ID.

        membership_id : int
            Membership ID to modify.

        member_type : int
            New membertype for the specified member.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2EditGroupMembershipResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.editgroupmembership(
                group_id=1000000,
                membership_type=1,
                membership_id=1000000,
                member_type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.editgroupmembership(
            group_id, membership_type, membership_id, member_type, request_options=request_options
        )
        return _response.data

    async def unbanmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupV2UnbanMemberResponse:
        """
        Unbans the requested member, allowing them to re-apply for membership.

        Parameters
        ----------
        group_id : int


        membership_type : int
            Membership type of the provided membership ID.

        membership_id : int
            Membership ID of the member to unban from the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2UnbanMemberResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.unbanmember(
                group_id=1000000,
                membership_type=1,
                membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unbanmember(
            group_id, membership_type, membership_id, request_options=request_options
        )
        return _response.data

    async def getgroupoptionalconversations(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2GetGroupOptionalConversationsResponse:
        """
        Gets a list of available optional conversation channels and their settings.

        Parameters
        ----------
        group_id : int
            Requested group's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2GetGroupOptionalConversationsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.getgroupoptionalconversations(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getgroupoptionalconversations(group_id, request_options=request_options)
        return _response.data

    async def addoptionalconversation(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2AddOptionalConversationResponse:
        """
        Add a new optional conversation/chat channel. Requires admin permissions to the group.

        Parameters
        ----------
        group_id : int
            Group ID of the group to edit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2AddOptionalConversationResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.addoptionalconversation(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addoptionalconversation(group_id, request_options=request_options)
        return _response.data

    async def editoptionalconversation(
        self, group_id: int, conversation_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupV2EditOptionalConversationResponse:
        """
        Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.

        Parameters
        ----------
        group_id : int
            Group ID of the group to edit.

        conversation_id : int
            Conversation Id of the channel being edited.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupV2EditOptionalConversationResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.groupv2.editoptionalconversation(
                group_id=1000000,
                conversation_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.editoptionalconversation(
            group_id, conversation_id, request_options=request_options
        )
        return _response.data
