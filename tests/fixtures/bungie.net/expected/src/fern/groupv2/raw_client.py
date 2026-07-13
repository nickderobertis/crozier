

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
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


class RawGroupv2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getavailableavatars(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetAvailableAvatarsResponse]:
        """
        Returns a list of all available group avatars for the signed-in user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GroupV2GetAvailableAvatarsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "GroupV2/GetAvailableAvatars/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetAvailableAvatarsResponse,
                    parse_obj_as(
                        type_=GroupV2GetAvailableAvatarsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getavailablethemes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetAvailableThemesResponse]:
        """
        Returns a list of all available group themes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GroupV2GetAvailableThemesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "GroupV2/GetAvailableThemes/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetAvailableThemesResponse,
                    parse_obj_as(
                        type_=GroupV2GetAvailableThemesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getuserclaninvitesetting(
        self, m_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetUserClanInviteSettingResponse]:
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
        HttpResponse[GroupV2GetUserClanInviteSettingResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/GetUserClanInviteSetting/{jsonable_encoder(m_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetUserClanInviteSettingResponse,
                    parse_obj_as(
                        type_=GroupV2GetUserClanInviteSettingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getgroupbyname(
        self, group_name: str, group_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetGroupByNameResponse]:
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
        HttpResponse[GroupV2GetGroupByNameResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/Name/{jsonable_encoder(group_name)}/{jsonable_encoder(group_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetGroupByNameResponse,
                    parse_obj_as(
                        type_=GroupV2GetGroupByNameResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getgroupbynamev2(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetGroupByNameV2Response]:
        """
        Get information about a specific group with the given name and type. The POST version.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GroupV2GetGroupByNameV2Response]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "GroupV2/NameV2/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetGroupByNameV2Response,
                    parse_obj_as(
                        type_=GroupV2GetGroupByNameV2Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getrecommendedgroups(
        self, group_type: int, create_date_range: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetRecommendedGroupsResponse]:
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
        HttpResponse[GroupV2GetRecommendedGroupsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/Recommended/{jsonable_encoder(group_type)}/{jsonable_encoder(create_date_range)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetRecommendedGroupsResponse,
                    parse_obj_as(
                        type_=GroupV2GetRecommendedGroupsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def recovergroupforfounder(
        self,
        membership_type: int,
        membership_id: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2RecoverGroupForFounderResponse]:
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
        HttpResponse[GroupV2RecoverGroupForFounderResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/Recover/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/{jsonable_encoder(group_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2RecoverGroupForFounderResponse,
                    parse_obj_as(
                        type_=GroupV2RecoverGroupForFounderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def groupsearch(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GroupSearchResponse]:
        """
        Search for Groups.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GroupV2GroupSearchResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "GroupV2/Search/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GroupSearchResponse,
                    parse_obj_as(
                        type_=GroupV2GroupSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getpotentialgroupsformember(
        self,
        membership_type: int,
        membership_id: int,
        filter: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2GetPotentialGroupsForMemberResponse]:
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
        HttpResponse[GroupV2GetPotentialGroupsForMemberResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/User/Potential/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/{jsonable_encoder(filter)}/{jsonable_encoder(group_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetPotentialGroupsForMemberResponse,
                    parse_obj_as(
                        type_=GroupV2GetPotentialGroupsForMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getgroupsformember(
        self,
        membership_type: int,
        membership_id: int,
        filter: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2GetGroupsForMemberResponse]:
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
        HttpResponse[GroupV2GetGroupsForMemberResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/User/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/{jsonable_encoder(filter)}/{jsonable_encoder(group_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetGroupsForMemberResponse,
                    parse_obj_as(
                        type_=GroupV2GetGroupsForMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getgroup(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetGroupResponse]:
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
        HttpResponse[GroupV2GetGroupResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetGroupResponse,
                    parse_obj_as(
                        type_=GroupV2GetGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def abdicatefoundership(
        self,
        group_id: int,
        membership_type: int,
        founder_id_new: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2AbdicateFoundershipResponse]:
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
        HttpResponse[GroupV2AbdicateFoundershipResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Admin/AbdicateFoundership/{jsonable_encoder(membership_type)}/{jsonable_encoder(founder_id_new)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2AbdicateFoundershipResponse,
                    parse_obj_as(
                        type_=GroupV2AbdicateFoundershipResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getadminsandfounderofgroup(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetAdminsAndFounderOfGroupResponse]:
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
        HttpResponse[GroupV2GetAdminsAndFounderOfGroupResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/AdminsAndFounder/",
            method="GET",
            params={
                "currentpage": currentpage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetAdminsAndFounderOfGroupResponse,
                    parse_obj_as(
                        type_=GroupV2GetAdminsAndFounderOfGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getbannedmembersofgroup(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetBannedMembersOfGroupResponse]:
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
        HttpResponse[GroupV2GetBannedMembersOfGroupResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Banned/",
            method="GET",
            params={
                "currentpage": currentpage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetBannedMembersOfGroupResponse,
                    parse_obj_as(
                        type_=GroupV2GetBannedMembersOfGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def editgroup(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2EditGroupResponse]:
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
        HttpResponse[GroupV2EditGroupResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Edit/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2EditGroupResponse,
                    parse_obj_as(
                        type_=GroupV2EditGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def editclanbanner(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2EditClanBannerResponse]:
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
        HttpResponse[GroupV2EditClanBannerResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/EditClanBanner/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2EditClanBannerResponse,
                    parse_obj_as(
                        type_=GroupV2EditClanBannerResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def editfounderoptions(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2EditFounderOptionsResponse]:
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
        HttpResponse[GroupV2EditFounderOptionsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/EditFounderOptions/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2EditFounderOptionsResponse,
                    parse_obj_as(
                        type_=GroupV2EditFounderOptionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getmembersofgroup(
        self,
        group_id: int,
        *,
        currentpage: int,
        member_type: typing.Optional[int] = None,
        name_search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2GetMembersOfGroupResponse]:
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
        HttpResponse[GroupV2GetMembersOfGroupResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/",
            method="GET",
            params={
                "currentpage": currentpage,
                "memberType": member_type,
                "nameSearch": name_search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetMembersOfGroupResponse,
                    parse_obj_as(
                        type_=GroupV2GetMembersOfGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def approvepending(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2ApprovePendingResponse]:
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
        HttpResponse[GroupV2ApprovePendingResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/Approve/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2ApprovePendingResponse,
                    parse_obj_as(
                        type_=GroupV2ApprovePendingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def approveallpending(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2ApproveAllPendingResponse]:
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
        HttpResponse[GroupV2ApproveAllPendingResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/ApproveAll/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2ApproveAllPendingResponse,
                    parse_obj_as(
                        type_=GroupV2ApproveAllPendingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def approvependingforlist(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2ApprovePendingForListResponse]:
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
        HttpResponse[GroupV2ApprovePendingForListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/ApproveList/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2ApprovePendingForListResponse,
                    parse_obj_as(
                        type_=GroupV2ApprovePendingForListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def denyallpending(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2DenyAllPendingResponse]:
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
        HttpResponse[GroupV2DenyAllPendingResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/DenyAll/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2DenyAllPendingResponse,
                    parse_obj_as(
                        type_=GroupV2DenyAllPendingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def denypendingforlist(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2DenyPendingForListResponse]:
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
        HttpResponse[GroupV2DenyPendingForListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/DenyList/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2DenyPendingForListResponse,
                    parse_obj_as(
                        type_=GroupV2DenyPendingForListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def individualgroupinvite(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2IndividualGroupInviteResponse]:
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
        HttpResponse[GroupV2IndividualGroupInviteResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/IndividualInvite/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2IndividualGroupInviteResponse,
                    parse_obj_as(
                        type_=GroupV2IndividualGroupInviteResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def individualgroupinvitecancel(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2IndividualGroupInviteCancelResponse]:
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
        HttpResponse[GroupV2IndividualGroupInviteCancelResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/IndividualInviteCancel/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2IndividualGroupInviteCancelResponse,
                    parse_obj_as(
                        type_=GroupV2IndividualGroupInviteCancelResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getinvitedindividuals(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetInvitedIndividualsResponse]:
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
        HttpResponse[GroupV2GetInvitedIndividualsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/InvitedIndividuals/",
            method="GET",
            params={
                "currentpage": currentpage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetInvitedIndividualsResponse,
                    parse_obj_as(
                        type_=GroupV2GetInvitedIndividualsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getpendingmemberships(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetPendingMembershipsResponse]:
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
        HttpResponse[GroupV2GetPendingMembershipsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/Pending/",
            method="GET",
            params={
                "currentpage": currentpage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetPendingMembershipsResponse,
                    parse_obj_as(
                        type_=GroupV2GetPendingMembershipsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def banmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2BanMemberResponse]:
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
        HttpResponse[GroupV2BanMemberResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/Ban/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2BanMemberResponse,
                    parse_obj_as(
                        type_=GroupV2BanMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def kickmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2KickMemberResponse]:
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
        HttpResponse[GroupV2KickMemberResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/Kick/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2KickMemberResponse,
                    parse_obj_as(
                        type_=GroupV2KickMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def editgroupmembership(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        member_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2EditGroupMembershipResponse]:
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
        HttpResponse[GroupV2EditGroupMembershipResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/SetMembershipType/{jsonable_encoder(member_type)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2EditGroupMembershipResponse,
                    parse_obj_as(
                        type_=GroupV2EditGroupMembershipResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def unbanmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupV2UnbanMemberResponse]:
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
        HttpResponse[GroupV2UnbanMemberResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/Unban/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2UnbanMemberResponse,
                    parse_obj_as(
                        type_=GroupV2UnbanMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getgroupoptionalconversations(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2GetGroupOptionalConversationsResponse]:
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
        HttpResponse[GroupV2GetGroupOptionalConversationsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/OptionalConversations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetGroupOptionalConversationsResponse,
                    parse_obj_as(
                        type_=GroupV2GetGroupOptionalConversationsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def addoptionalconversation(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2AddOptionalConversationResponse]:
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
        HttpResponse[GroupV2AddOptionalConversationResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/OptionalConversations/Add/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2AddOptionalConversationResponse,
                    parse_obj_as(
                        type_=GroupV2AddOptionalConversationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def editoptionalconversation(
        self, group_id: int, conversation_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupV2EditOptionalConversationResponse]:
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
        HttpResponse[GroupV2EditOptionalConversationResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/OptionalConversations/Edit/{jsonable_encoder(conversation_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2EditOptionalConversationResponse,
                    parse_obj_as(
                        type_=GroupV2EditOptionalConversationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawGroupv2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getavailableavatars(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetAvailableAvatarsResponse]:
        """
        Returns a list of all available group avatars for the signed-in user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GroupV2GetAvailableAvatarsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GroupV2/GetAvailableAvatars/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetAvailableAvatarsResponse,
                    parse_obj_as(
                        type_=GroupV2GetAvailableAvatarsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getavailablethemes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetAvailableThemesResponse]:
        """
        Returns a list of all available group themes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GroupV2GetAvailableThemesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GroupV2/GetAvailableThemes/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetAvailableThemesResponse,
                    parse_obj_as(
                        type_=GroupV2GetAvailableThemesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getuserclaninvitesetting(
        self, m_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetUserClanInviteSettingResponse]:
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
        AsyncHttpResponse[GroupV2GetUserClanInviteSettingResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/GetUserClanInviteSetting/{jsonable_encoder(m_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetUserClanInviteSettingResponse,
                    parse_obj_as(
                        type_=GroupV2GetUserClanInviteSettingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getgroupbyname(
        self, group_name: str, group_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetGroupByNameResponse]:
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
        AsyncHttpResponse[GroupV2GetGroupByNameResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/Name/{jsonable_encoder(group_name)}/{jsonable_encoder(group_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetGroupByNameResponse,
                    parse_obj_as(
                        type_=GroupV2GetGroupByNameResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getgroupbynamev2(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetGroupByNameV2Response]:
        """
        Get information about a specific group with the given name and type. The POST version.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GroupV2GetGroupByNameV2Response]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GroupV2/NameV2/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetGroupByNameV2Response,
                    parse_obj_as(
                        type_=GroupV2GetGroupByNameV2Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getrecommendedgroups(
        self, group_type: int, create_date_range: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetRecommendedGroupsResponse]:
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
        AsyncHttpResponse[GroupV2GetRecommendedGroupsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/Recommended/{jsonable_encoder(group_type)}/{jsonable_encoder(create_date_range)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetRecommendedGroupsResponse,
                    parse_obj_as(
                        type_=GroupV2GetRecommendedGroupsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def recovergroupforfounder(
        self,
        membership_type: int,
        membership_id: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2RecoverGroupForFounderResponse]:
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
        AsyncHttpResponse[GroupV2RecoverGroupForFounderResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/Recover/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/{jsonable_encoder(group_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2RecoverGroupForFounderResponse,
                    parse_obj_as(
                        type_=GroupV2RecoverGroupForFounderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def groupsearch(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GroupSearchResponse]:
        """
        Search for Groups.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GroupV2GroupSearchResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GroupV2/Search/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GroupSearchResponse,
                    parse_obj_as(
                        type_=GroupV2GroupSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getpotentialgroupsformember(
        self,
        membership_type: int,
        membership_id: int,
        filter: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2GetPotentialGroupsForMemberResponse]:
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
        AsyncHttpResponse[GroupV2GetPotentialGroupsForMemberResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/User/Potential/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/{jsonable_encoder(filter)}/{jsonable_encoder(group_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetPotentialGroupsForMemberResponse,
                    parse_obj_as(
                        type_=GroupV2GetPotentialGroupsForMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getgroupsformember(
        self,
        membership_type: int,
        membership_id: int,
        filter: int,
        group_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2GetGroupsForMemberResponse]:
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
        AsyncHttpResponse[GroupV2GetGroupsForMemberResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/User/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/{jsonable_encoder(filter)}/{jsonable_encoder(group_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetGroupsForMemberResponse,
                    parse_obj_as(
                        type_=GroupV2GetGroupsForMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getgroup(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetGroupResponse]:
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
        AsyncHttpResponse[GroupV2GetGroupResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetGroupResponse,
                    parse_obj_as(
                        type_=GroupV2GetGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def abdicatefoundership(
        self,
        group_id: int,
        membership_type: int,
        founder_id_new: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2AbdicateFoundershipResponse]:
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
        AsyncHttpResponse[GroupV2AbdicateFoundershipResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Admin/AbdicateFoundership/{jsonable_encoder(membership_type)}/{jsonable_encoder(founder_id_new)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2AbdicateFoundershipResponse,
                    parse_obj_as(
                        type_=GroupV2AbdicateFoundershipResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getadminsandfounderofgroup(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetAdminsAndFounderOfGroupResponse]:
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
        AsyncHttpResponse[GroupV2GetAdminsAndFounderOfGroupResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/AdminsAndFounder/",
            method="GET",
            params={
                "currentpage": currentpage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetAdminsAndFounderOfGroupResponse,
                    parse_obj_as(
                        type_=GroupV2GetAdminsAndFounderOfGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getbannedmembersofgroup(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetBannedMembersOfGroupResponse]:
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
        AsyncHttpResponse[GroupV2GetBannedMembersOfGroupResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Banned/",
            method="GET",
            params={
                "currentpage": currentpage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetBannedMembersOfGroupResponse,
                    parse_obj_as(
                        type_=GroupV2GetBannedMembersOfGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def editgroup(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2EditGroupResponse]:
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
        AsyncHttpResponse[GroupV2EditGroupResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Edit/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2EditGroupResponse,
                    parse_obj_as(
                        type_=GroupV2EditGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def editclanbanner(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2EditClanBannerResponse]:
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
        AsyncHttpResponse[GroupV2EditClanBannerResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/EditClanBanner/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2EditClanBannerResponse,
                    parse_obj_as(
                        type_=GroupV2EditClanBannerResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def editfounderoptions(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2EditFounderOptionsResponse]:
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
        AsyncHttpResponse[GroupV2EditFounderOptionsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/EditFounderOptions/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2EditFounderOptionsResponse,
                    parse_obj_as(
                        type_=GroupV2EditFounderOptionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getmembersofgroup(
        self,
        group_id: int,
        *,
        currentpage: int,
        member_type: typing.Optional[int] = None,
        name_search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2GetMembersOfGroupResponse]:
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
        AsyncHttpResponse[GroupV2GetMembersOfGroupResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/",
            method="GET",
            params={
                "currentpage": currentpage,
                "memberType": member_type,
                "nameSearch": name_search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetMembersOfGroupResponse,
                    parse_obj_as(
                        type_=GroupV2GetMembersOfGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def approvepending(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2ApprovePendingResponse]:
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
        AsyncHttpResponse[GroupV2ApprovePendingResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/Approve/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2ApprovePendingResponse,
                    parse_obj_as(
                        type_=GroupV2ApprovePendingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def approveallpending(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2ApproveAllPendingResponse]:
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
        AsyncHttpResponse[GroupV2ApproveAllPendingResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/ApproveAll/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2ApproveAllPendingResponse,
                    parse_obj_as(
                        type_=GroupV2ApproveAllPendingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def approvependingforlist(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2ApprovePendingForListResponse]:
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
        AsyncHttpResponse[GroupV2ApprovePendingForListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/ApproveList/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2ApprovePendingForListResponse,
                    parse_obj_as(
                        type_=GroupV2ApprovePendingForListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def denyallpending(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2DenyAllPendingResponse]:
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
        AsyncHttpResponse[GroupV2DenyAllPendingResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/DenyAll/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2DenyAllPendingResponse,
                    parse_obj_as(
                        type_=GroupV2DenyAllPendingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def denypendingforlist(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2DenyPendingForListResponse]:
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
        AsyncHttpResponse[GroupV2DenyPendingForListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/DenyList/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2DenyPendingForListResponse,
                    parse_obj_as(
                        type_=GroupV2DenyPendingForListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def individualgroupinvite(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2IndividualGroupInviteResponse]:
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
        AsyncHttpResponse[GroupV2IndividualGroupInviteResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/IndividualInvite/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2IndividualGroupInviteResponse,
                    parse_obj_as(
                        type_=GroupV2IndividualGroupInviteResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def individualgroupinvitecancel(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2IndividualGroupInviteCancelResponse]:
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
        AsyncHttpResponse[GroupV2IndividualGroupInviteCancelResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/IndividualInviteCancel/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2IndividualGroupInviteCancelResponse,
                    parse_obj_as(
                        type_=GroupV2IndividualGroupInviteCancelResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getinvitedindividuals(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetInvitedIndividualsResponse]:
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
        AsyncHttpResponse[GroupV2GetInvitedIndividualsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/InvitedIndividuals/",
            method="GET",
            params={
                "currentpage": currentpage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetInvitedIndividualsResponse,
                    parse_obj_as(
                        type_=GroupV2GetInvitedIndividualsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getpendingmemberships(
        self, group_id: int, *, currentpage: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetPendingMembershipsResponse]:
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
        AsyncHttpResponse[GroupV2GetPendingMembershipsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/Pending/",
            method="GET",
            params={
                "currentpage": currentpage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetPendingMembershipsResponse,
                    parse_obj_as(
                        type_=GroupV2GetPendingMembershipsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def banmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2BanMemberResponse]:
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
        AsyncHttpResponse[GroupV2BanMemberResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/Ban/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2BanMemberResponse,
                    parse_obj_as(
                        type_=GroupV2BanMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def kickmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2KickMemberResponse]:
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
        AsyncHttpResponse[GroupV2KickMemberResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/Kick/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2KickMemberResponse,
                    parse_obj_as(
                        type_=GroupV2KickMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def editgroupmembership(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        member_type: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2EditGroupMembershipResponse]:
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
        AsyncHttpResponse[GroupV2EditGroupMembershipResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/SetMembershipType/{jsonable_encoder(member_type)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2EditGroupMembershipResponse,
                    parse_obj_as(
                        type_=GroupV2EditGroupMembershipResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def unbanmember(
        self,
        group_id: int,
        membership_type: int,
        membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupV2UnbanMemberResponse]:
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
        AsyncHttpResponse[GroupV2UnbanMemberResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/Members/{jsonable_encoder(membership_type)}/{jsonable_encoder(membership_id)}/Unban/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2UnbanMemberResponse,
                    parse_obj_as(
                        type_=GroupV2UnbanMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getgroupoptionalconversations(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2GetGroupOptionalConversationsResponse]:
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
        AsyncHttpResponse[GroupV2GetGroupOptionalConversationsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/OptionalConversations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2GetGroupOptionalConversationsResponse,
                    parse_obj_as(
                        type_=GroupV2GetGroupOptionalConversationsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def addoptionalconversation(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2AddOptionalConversationResponse]:
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
        AsyncHttpResponse[GroupV2AddOptionalConversationResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/OptionalConversations/Add/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2AddOptionalConversationResponse,
                    parse_obj_as(
                        type_=GroupV2AddOptionalConversationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def editoptionalconversation(
        self, group_id: int, conversation_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupV2EditOptionalConversationResponse]:
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
        AsyncHttpResponse[GroupV2EditOptionalConversationResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"GroupV2/{jsonable_encoder(group_id)}/OptionalConversations/Edit/{jsonable_encoder(conversation_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupV2EditOptionalConversationResponse,
                    parse_obj_as(
                        type_=GroupV2EditOptionalConversationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
