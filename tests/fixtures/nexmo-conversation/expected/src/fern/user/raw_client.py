

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.channel import Channel
from ..types.display_name_user import DisplayNameUser
from ..types.image_url import ImageUrl
from ..types.name_user import NameUser
from .types.create_user_response import CreateUserResponse
from .types.get_user_response import GetUserResponse
from .types.get_users_response_item import GetUsersResponseItem
from .types.getuser_conversations_response_item import GetuserConversationsResponseItem
from .types.update_user_response import UpdateUserResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetUsersResponseItem]]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/users](/api/conversation.v2#get-users).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetUsersResponseItem]]
            List of users
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetUsersResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetUsersResponseItem],
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

    def create_user(
        self,
        *,
        display_name: typing.Optional[DisplayNameUser] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateUserResponse]:
        """
        Note: Users must be created with an admin JWT.

        Parameters
        ----------
        display_name : typing.Optional[DisplayNameUser]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateUserResponse]
            Create a user response
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            json={
                "display_name": display_name,
                "image_url": image_url,
                "name": name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateUserResponse,
                    parse_obj_as(
                        type_=CreateUserResponse,
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

    def get_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetUserResponse]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUserResponse]
            Retrieve a user
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserResponse,
                    parse_obj_as(
                        type_=GetUserResponse,
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

    def update_user(
        self,
        user_id: str,
        *,
        channels: typing.Optional[Channel] = OMIT,
        display_name: typing.Optional[DisplayNameUser] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateUserResponse]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        channels : typing.Optional[Channel]

        display_name : typing.Optional[DisplayNameUser]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateUserResponse]
            Retrieve a user
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "channels": convert_and_respect_annotation_metadata(
                    object_=channels, annotation=Channel, direction="write"
                ),
                "display_name": display_name,
                "image_url": image_url,
                "name": name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateUserResponse,
                    parse_obj_as(
                        type_=UpdateUserResponse,
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

    def delete_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Success response with empty JSON
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def getuser_conversations(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetuserConversationsResponseItem]]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetuserConversationsResponseItem]]
            List user conversations
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/conversations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetuserConversationsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetuserConversationsResponseItem],
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

    async def get_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetUsersResponseItem]]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/users](/api/conversation.v2#get-users).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetUsersResponseItem]]
            List of users
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetUsersResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetUsersResponseItem],
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

    async def create_user(
        self,
        *,
        display_name: typing.Optional[DisplayNameUser] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateUserResponse]:
        """
        Note: Users must be created with an admin JWT.

        Parameters
        ----------
        display_name : typing.Optional[DisplayNameUser]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateUserResponse]
            Create a user response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            json={
                "display_name": display_name,
                "image_url": image_url,
                "name": name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateUserResponse,
                    parse_obj_as(
                        type_=CreateUserResponse,
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

    async def get_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetUserResponse]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUserResponse]
            Retrieve a user
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserResponse,
                    parse_obj_as(
                        type_=GetUserResponse,
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

    async def update_user(
        self,
        user_id: str,
        *,
        channels: typing.Optional[Channel] = OMIT,
        display_name: typing.Optional[DisplayNameUser] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateUserResponse]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        channels : typing.Optional[Channel]

        display_name : typing.Optional[DisplayNameUser]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateUserResponse]
            Retrieve a user
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "channels": convert_and_respect_annotation_metadata(
                    object_=channels, annotation=Channel, direction="write"
                ),
                "display_name": display_name,
                "image_url": image_url,
                "name": name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateUserResponse,
                    parse_obj_as(
                        type_=UpdateUserResponse,
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

    async def delete_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Success response with empty JSON
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def getuser_conversations(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetuserConversationsResponseItem]]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetuserConversationsResponseItem]]
            List user conversations
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/conversations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetuserConversationsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetuserConversationsResponseItem],
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
