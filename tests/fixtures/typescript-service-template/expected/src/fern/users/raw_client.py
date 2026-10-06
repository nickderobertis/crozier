

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.user import User
from ..types.user_id import UserId
from .types.users_get_response import UsersGetResponse
from .types.users_patch_response import UsersPatchResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        q: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]] = None,
        count: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsersGetResponse]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Search for users by name

        id : typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]]
            Fetch users by ID

        count : typing.Optional[int]

        page : typing.Optional[str]
            Fetch users before this cursor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsersGetResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "q": q,
                "id": id,
                "count": count,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersGetResponse,
                    parse_obj_as(
                        type_=UsersGetResponse,
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

    def post(
        self, *, name: str, age: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[User]:
        """
        Parameters
        ----------
        name : str
            Name of the user

        age : int
            Age of user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            json={
                "name": name,
                "age": age,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
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

    def patch(
        self,
        *,
        id: typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]] = None,
        name: typing.Optional[str] = OMIT,
        age: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsersPatchResponse]:
        """
        Parameters
        ----------
        id : typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]]
            Edit these specific users

        name : typing.Optional[str]
            Name of the user

        age : typing.Optional[int]
            Age of user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsersPatchResponse]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="PATCH",
            params={
                "id": id,
            },
            json={
                "name": name,
                "age": age,
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
                    UsersPatchResponse,
                    parse_obj_as(
                        type_=UsersPatchResponse,
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


class AsyncRawUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        q: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]] = None,
        count: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsersGetResponse]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Search for users by name

        id : typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]]
            Fetch users by ID

        count : typing.Optional[int]

        page : typing.Optional[str]
            Fetch users before this cursor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsersGetResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "q": q,
                "id": id,
                "count": count,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersGetResponse,
                    parse_obj_as(
                        type_=UsersGetResponse,
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

    async def post(
        self, *, name: str, age: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """
        Parameters
        ----------
        name : str
            Name of the user

        age : int
            Age of user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            json={
                "name": name,
                "age": age,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
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

    async def patch(
        self,
        *,
        id: typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]] = None,
        name: typing.Optional[str] = OMIT,
        age: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsersPatchResponse]:
        """
        Parameters
        ----------
        id : typing.Optional[typing.Union[UserId, typing.Sequence[UserId]]]
            Edit these specific users

        name : typing.Optional[str]
            Name of the user

        age : typing.Optional[int]
            Age of user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsersPatchResponse]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="PATCH",
            params={
                "id": id,
            },
            json={
                "name": name,
                "age": age,
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
                    UsersPatchResponse,
                    parse_obj_as(
                        type_=UsersPatchResponse,
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
