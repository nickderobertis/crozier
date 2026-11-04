

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.user_get_information_response import UserGetInformationResponse
from ..types.user_get_user_information_response import UserGetUserInformationResponse
from ..types.user_list_collaborations_response import UserListCollaborationsResponse
from pydantic import ValidationError


class RawUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getinformation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserGetInformationResponse]:
        """
        Provides information about the user that is currently signed in.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserGetInformationResponse]
            User login information.
        """
        _response = self._client_wrapper.httpx_client.request(
            "me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetInformationResponse,
                    parse_obj_as(
                        type_=UserGetInformationResponse,
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

    def listcollaborations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserListCollaborationsResponse]:
        """
        Provides the set of organizations of which a user is a member or a collaborator.

        The set of organizations that a user can collaborate on is composed of:

        * Organizations that the current user belongs to across VCS types (e.g. BitBucket, GitHub)
        * The parent organization of repository that the user can collaborate on, but is not necessarily a member of
        * The organization of the current user's account

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserListCollaborationsResponse]
            Collaborations
        """
        _response = self._client_wrapper.httpx_client.request(
            "me/collaborations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserListCollaborationsResponse,
                    parse_obj_as(
                        type_=UserListCollaborationsResponse,
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

    def getuserinformation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserGetUserInformationResponse]:
        """
        Provides information about the user with the given ID.

        Parameters
        ----------
        id : str
            The unique ID of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserGetUserInformationResponse]
            User login information.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetUserInformationResponse,
                    parse_obj_as(
                        type_=UserGetUserInformationResponse,
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


class AsyncRawUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getinformation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserGetInformationResponse]:
        """
        Provides information about the user that is currently signed in.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserGetInformationResponse]
            User login information.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetInformationResponse,
                    parse_obj_as(
                        type_=UserGetInformationResponse,
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

    async def listcollaborations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserListCollaborationsResponse]:
        """
        Provides the set of organizations of which a user is a member or a collaborator.

        The set of organizations that a user can collaborate on is composed of:

        * Organizations that the current user belongs to across VCS types (e.g. BitBucket, GitHub)
        * The parent organization of repository that the user can collaborate on, but is not necessarily a member of
        * The organization of the current user's account

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserListCollaborationsResponse]
            Collaborations
        """
        _response = await self._client_wrapper.httpx_client.request(
            "me/collaborations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserListCollaborationsResponse,
                    parse_obj_as(
                        type_=UserListCollaborationsResponse,
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

    async def getuserinformation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserGetUserInformationResponse]:
        """
        Provides information about the user with the given ID.

        Parameters
        ----------
        id : str
            The unique ID of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserGetUserInformationResponse]
            User login information.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGetUserInformationResponse,
                    parse_obj_as(
                        type_=UserGetUserInformationResponse,
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
