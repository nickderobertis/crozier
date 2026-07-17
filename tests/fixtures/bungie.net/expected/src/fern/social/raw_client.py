

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.social_accept_friend_request_response import SocialAcceptFriendRequestResponse
from .types.social_decline_friend_request_response import SocialDeclineFriendRequestResponse
from .types.social_get_friend_list_response import SocialGetFriendListResponse
from .types.social_get_friend_request_list_response import SocialGetFriendRequestListResponse
from .types.social_get_platform_friend_list_response import SocialGetPlatformFriendListResponse
from .types.social_issue_friend_request_response import SocialIssueFriendRequestResponse
from .types.social_remove_friend_request_response import SocialRemoveFriendRequestResponse
from .types.social_remove_friend_response import SocialRemoveFriendResponse
from pydantic import ValidationError


class RawSocialClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getfriendlist(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SocialGetFriendListResponse]:
        """
        Returns your Bungie Friend list

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SocialGetFriendListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Social/Friends/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialGetFriendListResponse,
                    parse_obj_as(
                        type_=SocialGetFriendListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def issuefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SocialIssueFriendRequestResponse]:
        """
        Requests a friend relationship with the target user. Any of the target user's linked membership ids are valid inputs.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to add.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SocialIssueFriendRequestResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Social/Friends/Add/{encode_path_param(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialIssueFriendRequestResponse,
                    parse_obj_as(
                        type_=SocialIssueFriendRequestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def removefriend(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SocialRemoveFriendResponse]:
        """
        Remove a friend relationship with the target user. The user must be on your friend list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SocialRemoveFriendResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Social/Friends/Remove/{encode_path_param(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialRemoveFriendResponse,
                    parse_obj_as(
                        type_=SocialRemoveFriendResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getfriendrequestlist(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SocialGetFriendRequestListResponse]:
        """
        Returns your friend request queue.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SocialGetFriendRequestListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Social/Friends/Requests/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialGetFriendRequestListResponse,
                    parse_obj_as(
                        type_=SocialGetFriendRequestListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def acceptfriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SocialAcceptFriendRequestResponse]:
        """
        Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SocialAcceptFriendRequestResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Social/Friends/Requests/Accept/{encode_path_param(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialAcceptFriendRequestResponse,
                    parse_obj_as(
                        type_=SocialAcceptFriendRequestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def declinefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SocialDeclineFriendRequestResponse]:
        """
        Declines a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to decline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SocialDeclineFriendRequestResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Social/Friends/Requests/Decline/{encode_path_param(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialDeclineFriendRequestResponse,
                    parse_obj_as(
                        type_=SocialDeclineFriendRequestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def removefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SocialRemoveFriendRequestResponse]:
        """
        Remove a friend relationship with the target user. The user must be on your outgoing request friend list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SocialRemoveFriendRequestResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Social/Friends/Requests/Remove/{encode_path_param(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialRemoveFriendRequestResponse,
                    parse_obj_as(
                        type_=SocialRemoveFriendRequestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getplatformfriendlist(
        self, friend_platform: int, page: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SocialGetPlatformFriendListResponse]:
        """
        Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.

        Parameters
        ----------
        friend_platform : int
            The platform friend type.

        page : str
            The zero based page to return. Page size is 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SocialGetPlatformFriendListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Social/PlatformFriends/{encode_path_param(friend_platform)}/{encode_path_param(page)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialGetPlatformFriendListResponse,
                    parse_obj_as(
                        type_=SocialGetPlatformFriendListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSocialClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getfriendlist(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SocialGetFriendListResponse]:
        """
        Returns your Bungie Friend list

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SocialGetFriendListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Social/Friends/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialGetFriendListResponse,
                    parse_obj_as(
                        type_=SocialGetFriendListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def issuefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SocialIssueFriendRequestResponse]:
        """
        Requests a friend relationship with the target user. Any of the target user's linked membership ids are valid inputs.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to add.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SocialIssueFriendRequestResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Social/Friends/Add/{encode_path_param(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialIssueFriendRequestResponse,
                    parse_obj_as(
                        type_=SocialIssueFriendRequestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def removefriend(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SocialRemoveFriendResponse]:
        """
        Remove a friend relationship with the target user. The user must be on your friend list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SocialRemoveFriendResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Social/Friends/Remove/{encode_path_param(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialRemoveFriendResponse,
                    parse_obj_as(
                        type_=SocialRemoveFriendResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getfriendrequestlist(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SocialGetFriendRequestListResponse]:
        """
        Returns your friend request queue.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SocialGetFriendRequestListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Social/Friends/Requests/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialGetFriendRequestListResponse,
                    parse_obj_as(
                        type_=SocialGetFriendRequestListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def acceptfriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SocialAcceptFriendRequestResponse]:
        """
        Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SocialAcceptFriendRequestResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Social/Friends/Requests/Accept/{encode_path_param(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialAcceptFriendRequestResponse,
                    parse_obj_as(
                        type_=SocialAcceptFriendRequestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def declinefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SocialDeclineFriendRequestResponse]:
        """
        Declines a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to decline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SocialDeclineFriendRequestResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Social/Friends/Requests/Decline/{encode_path_param(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialDeclineFriendRequestResponse,
                    parse_obj_as(
                        type_=SocialDeclineFriendRequestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def removefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SocialRemoveFriendRequestResponse]:
        """
        Remove a friend relationship with the target user. The user must be on your outgoing request friend list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SocialRemoveFriendRequestResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Social/Friends/Requests/Remove/{encode_path_param(membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialRemoveFriendRequestResponse,
                    parse_obj_as(
                        type_=SocialRemoveFriendRequestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getplatformfriendlist(
        self, friend_platform: int, page: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SocialGetPlatformFriendListResponse]:
        """
        Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.

        Parameters
        ----------
        friend_platform : int
            The platform friend type.

        page : str
            The zero based page to return. Page size is 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SocialGetPlatformFriendListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Social/PlatformFriends/{encode_path_param(friend_platform)}/{encode_path_param(page)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SocialGetPlatformFriendListResponse,
                    parse_obj_as(
                        type_=SocialGetPlatformFriendListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
