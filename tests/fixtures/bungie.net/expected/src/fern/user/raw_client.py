

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.user_get_available_themes_response import UserGetAvailableThemesResponse
from .types.user_get_bungie_net_user_by_id_response import UserGetBungieNetUserByIdResponse
from .types.user_get_credential_types_for_target_account_response import UserGetCredentialTypesForTargetAccountResponse
from .types.user_get_membership_data_by_id_response import UserGetMembershipDataByIdResponse
from .types.user_get_membership_data_for_current_user_response import UserGetMembershipDataForCurrentUserResponse
from .types.user_get_membership_from_hard_linked_credential_response import (
    UserGetMembershipFromHardLinkedCredentialResponse,
)
from .types.user_get_sanitized_platform_display_names_response import UserGetSanitizedPlatformDisplayNamesResponse
from .types.user_search_by_global_name_post_response import UserSearchByGlobalNamePostResponse
from .types.user_search_by_global_name_prefix_response import UserSearchByGlobalNamePrefixResponse


class RawUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getavailablethemes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserGetAvailableThemesResponse]:
        """
        Returns a list of all available user themes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserGetAvailableThemesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "User/GetAvailableThemes/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetAvailableThemesResponse,
                    parse_obj_as(
                        type_=UserGetAvailableThemesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getbungienetuserbyid(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserGetBungieNetUserByIdResponse]:
        """
        Loads a bungienet user by membership id.

        Parameters
        ----------
        id : int
            The requested Bungie.net membership id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserGetBungieNetUserByIdResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"User/GetBungieNetUserById/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetBungieNetUserByIdResponse,
                    parse_obj_as(
                        type_=UserGetBungieNetUserByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getcredentialtypesfortargetaccount(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserGetCredentialTypesForTargetAccountResponse]:
        """
        Returns a list of credential types attached to the requested account

        Parameters
        ----------
        membership_id : int
            The user's membership id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserGetCredentialTypesForTargetAccountResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"User/GetCredentialTypesForTargetAccount/{jsonable_encoder(membership_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetCredentialTypesForTargetAccountResponse,
                    parse_obj_as(
                        type_=UserGetCredentialTypesForTargetAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getmembershipfromhardlinkedcredential(
        self, cr_type: int, credential: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserGetMembershipFromHardLinkedCredentialResponse]:
        """
        Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.

        Parameters
        ----------
        cr_type : int
            The credential type. 'SteamId' is the only valid value at present.

        credential : str
            The credential to look up. Must be a valid SteamID64.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserGetMembershipFromHardLinkedCredentialResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"User/GetMembershipFromHardLinkedCredential/{jsonable_encoder(cr_type)}/{jsonable_encoder(credential)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetMembershipFromHardLinkedCredentialResponse,
                    parse_obj_as(
                        type_=UserGetMembershipFromHardLinkedCredentialResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getmembershipdatabyid(
        self, membership_id: int, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserGetMembershipDataByIdResponse]:
        """
        Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

        Parameters
        ----------
        membership_id : int
            The membership ID of the target user.

        membership_type : int
            Type of the supplied membership ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserGetMembershipDataByIdResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"User/GetMembershipsById/{jsonable_encoder(membership_id)}/{jsonable_encoder(membership_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetMembershipDataByIdResponse,
                    parse_obj_as(
                        type_=UserGetMembershipDataByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getmembershipdataforcurrentuser(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserGetMembershipDataForCurrentUserResponse]:
        """
        Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserGetMembershipDataForCurrentUserResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "User/GetMembershipsForCurrentUser/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetMembershipDataForCurrentUserResponse,
                    parse_obj_as(
                        type_=UserGetMembershipDataForCurrentUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getsanitizedplatformdisplaynames(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserGetSanitizedPlatformDisplayNamesResponse]:
        """
        Gets a list of all display names linked to this membership id but sanitized (profanity filtered). Obeys all visibility rules of calling user and is heavily cached.

        Parameters
        ----------
        membership_id : int
            The requested membership id to load.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserGetSanitizedPlatformDisplayNamesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"User/GetSanitizedPlatformDisplayNames/{jsonable_encoder(membership_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetSanitizedPlatformDisplayNamesResponse,
                    parse_obj_as(
                        type_=UserGetSanitizedPlatformDisplayNamesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def searchbyglobalnamepost(
        self, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserSearchByGlobalNamePostResponse]:
        """
        Given the prefix of a global display name, returns all users who share that name.

        Parameters
        ----------
        page : int
            The zero-based page of results you desire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserSearchByGlobalNamePostResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"User/Search/GlobalName/{jsonable_encoder(page)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserSearchByGlobalNamePostResponse,
                    parse_obj_as(
                        type_=UserSearchByGlobalNamePostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def searchbyglobalnameprefix(
        self, display_name_prefix: str, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserSearchByGlobalNamePrefixResponse]:
        """
        [OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.

        Parameters
        ----------
        display_name_prefix : str
            The display name prefix you're looking for.

        page : int
            The zero-based page of results you desire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserSearchByGlobalNamePrefixResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"User/Search/Prefix/{jsonable_encoder(display_name_prefix)}/{jsonable_encoder(page)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserSearchByGlobalNamePrefixResponse,
                    parse_obj_as(
                        type_=UserSearchByGlobalNamePrefixResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getavailablethemes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserGetAvailableThemesResponse]:
        """
        Returns a list of all available user themes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserGetAvailableThemesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "User/GetAvailableThemes/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetAvailableThemesResponse,
                    parse_obj_as(
                        type_=UserGetAvailableThemesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getbungienetuserbyid(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserGetBungieNetUserByIdResponse]:
        """
        Loads a bungienet user by membership id.

        Parameters
        ----------
        id : int
            The requested Bungie.net membership id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserGetBungieNetUserByIdResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"User/GetBungieNetUserById/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetBungieNetUserByIdResponse,
                    parse_obj_as(
                        type_=UserGetBungieNetUserByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getcredentialtypesfortargetaccount(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserGetCredentialTypesForTargetAccountResponse]:
        """
        Returns a list of credential types attached to the requested account

        Parameters
        ----------
        membership_id : int
            The user's membership id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserGetCredentialTypesForTargetAccountResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"User/GetCredentialTypesForTargetAccount/{jsonable_encoder(membership_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetCredentialTypesForTargetAccountResponse,
                    parse_obj_as(
                        type_=UserGetCredentialTypesForTargetAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getmembershipfromhardlinkedcredential(
        self, cr_type: int, credential: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserGetMembershipFromHardLinkedCredentialResponse]:
        """
        Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.

        Parameters
        ----------
        cr_type : int
            The credential type. 'SteamId' is the only valid value at present.

        credential : str
            The credential to look up. Must be a valid SteamID64.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserGetMembershipFromHardLinkedCredentialResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"User/GetMembershipFromHardLinkedCredential/{jsonable_encoder(cr_type)}/{jsonable_encoder(credential)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetMembershipFromHardLinkedCredentialResponse,
                    parse_obj_as(
                        type_=UserGetMembershipFromHardLinkedCredentialResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getmembershipdatabyid(
        self, membership_id: int, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserGetMembershipDataByIdResponse]:
        """
        Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

        Parameters
        ----------
        membership_id : int
            The membership ID of the target user.

        membership_type : int
            Type of the supplied membership ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserGetMembershipDataByIdResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"User/GetMembershipsById/{jsonable_encoder(membership_id)}/{jsonable_encoder(membership_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetMembershipDataByIdResponse,
                    parse_obj_as(
                        type_=UserGetMembershipDataByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getmembershipdataforcurrentuser(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserGetMembershipDataForCurrentUserResponse]:
        """
        Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserGetMembershipDataForCurrentUserResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "User/GetMembershipsForCurrentUser/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetMembershipDataForCurrentUserResponse,
                    parse_obj_as(
                        type_=UserGetMembershipDataForCurrentUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getsanitizedplatformdisplaynames(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserGetSanitizedPlatformDisplayNamesResponse]:
        """
        Gets a list of all display names linked to this membership id but sanitized (profanity filtered). Obeys all visibility rules of calling user and is heavily cached.

        Parameters
        ----------
        membership_id : int
            The requested membership id to load.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserGetSanitizedPlatformDisplayNamesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"User/GetSanitizedPlatformDisplayNames/{jsonable_encoder(membership_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetSanitizedPlatformDisplayNamesResponse,
                    parse_obj_as(
                        type_=UserGetSanitizedPlatformDisplayNamesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def searchbyglobalnamepost(
        self, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserSearchByGlobalNamePostResponse]:
        """
        Given the prefix of a global display name, returns all users who share that name.

        Parameters
        ----------
        page : int
            The zero-based page of results you desire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserSearchByGlobalNamePostResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"User/Search/GlobalName/{jsonable_encoder(page)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserSearchByGlobalNamePostResponse,
                    parse_obj_as(
                        type_=UserSearchByGlobalNamePostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def searchbyglobalnameprefix(
        self, display_name_prefix: str, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserSearchByGlobalNamePrefixResponse]:
        """
        [OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.

        Parameters
        ----------
        display_name_prefix : str
            The display name prefix you're looking for.

        page : int
            The zero-based page of results you desire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserSearchByGlobalNamePrefixResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"User/Search/Prefix/{jsonable_encoder(display_name_prefix)}/{jsonable_encoder(page)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserSearchByGlobalNamePrefixResponse,
                    parse_obj_as(
                        type_=UserSearchByGlobalNamePrefixResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
