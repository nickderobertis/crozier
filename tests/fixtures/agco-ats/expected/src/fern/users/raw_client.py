

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_models_user import ApiModelsUser
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ApiModelsUser]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiModelsUser]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiModelsUser,
                    parse_obj_as(
                        type_=ApiModelsUser,
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
        self,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiModelsUser]:
        """
        No Documentation Found.

        Parameters
        ----------
        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiModelsUser]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Users",
            method="POST",
            json={
                "ChangePassword": change_password,
                "Email": email,
                "Name": name,
                "Password": password,
                "UserID": user_id,
                "Username": username,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiModelsUser,
                    parse_obj_as(
                        type_=ApiModelsUser,
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

    def getcurrentuser(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ApiModelsUser]:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiModelsUser]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Users/Current",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiModelsUser,
                    parse_obj_as(
                        type_=ApiModelsUser,
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

    def putcurrentuser(
        self,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Users/Current",
            method="PUT",
            json={
                "ChangePassword": change_password,
                "Email": email,
                "Name": name,
                "Password": password,
                "UserID": user_id,
                "Username": username,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put(
        self,
        id: int,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user id

        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}",
            method="PUT",
            json={
                "ChangePassword": change_password,
                "Email": email,
                "Name": name,
                "Password": password,
                "UserID": user_id,
                "Username": username,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiModelsUser]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiModelsUser]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiModelsUser,
                    parse_obj_as(
                        type_=ApiModelsUser,
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
        self,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiModelsUser]:
        """
        No Documentation Found.

        Parameters
        ----------
        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiModelsUser]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Users",
            method="POST",
            json={
                "ChangePassword": change_password,
                "Email": email,
                "Name": name,
                "Password": password,
                "UserID": user_id,
                "Username": username,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiModelsUser,
                    parse_obj_as(
                        type_=ApiModelsUser,
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

    async def getcurrentuser(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiModelsUser]:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiModelsUser]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Users/Current",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiModelsUser,
                    parse_obj_as(
                        type_=ApiModelsUser,
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

    async def putcurrentuser(
        self,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Users/Current",
            method="PUT",
            json={
                "ChangePassword": change_password,
                "Email": email,
                "Name": name,
                "Password": password,
                "UserID": user_id,
                "Username": username,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put(
        self,
        id: int,
        *,
        change_password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user id

        change_password : typing.Optional[str]
            Never Returned.  When changing a user's password, this field must contain the new password.

        email : typing.Optional[str]
            The user's email address

        name : typing.Optional[str]
            The user's name

        password : typing.Optional[str]
            Never Returned.  Required when creating a new user or updating a user.  When changing a user's password this field must contain the current password.

        user_id : typing.Optional[int]
            The user ID

        username : typing.Optional[str]
            The username used for authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}",
            method="PUT",
            json={
                "ChangePassword": change_password,
                "Email": email,
                "Name": name,
                "Password": password,
                "UserID": user_id,
                "Username": username,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The user id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
