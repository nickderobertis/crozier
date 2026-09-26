

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.post_v2vectordb_users_describe_response import PostV2VectordbUsersDescribeResponse
from .types.post_v2vectordb_users_list_response import PostV2VectordbUsersListResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_user(
        self, *, user_name: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        This operation creates a new user with a corresponding password.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        password : str
            The corresponding password to the new user to create.
            The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/create",
            method="POST",
            json={
                "userName": user_name,
                "password": password,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def update_user_password(
        self,
        *,
        user_name: str,
        password: str,
        new_password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        This operation updates the password for a specific user.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        password : str
            The corresponding password to the new user to create.
            The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        new_password : str
            The new password for the specified user.    The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/update_password",
            method="POST",
            json={
                "userName": user_name,
                "password": password,
                "newPassword": new_password,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def drop_user(
        self, *, user_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        This operation deletes an existing user.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/drop",
            method="POST",
            json={
                "userName": user_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def describe_user(
        self, *, user_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbUsersDescribeResponse]:
        """
        This operation describes the detailed information of a specific user.

        Parameters
        ----------
        user_name : str
              The name of the user to describe.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbUsersDescribeResponse]
            成功
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/describe",
            method="POST",
            json={
                "userName": user_name,
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
                    PostV2VectordbUsersDescribeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbUsersDescribeResponse,
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

    def list_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbUsersListResponse]:
        """
        This operation lists the information of all existing users.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbUsersListResponse]
            An object that contains contains the user information.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/list",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV2VectordbUsersListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbUsersListResponse,
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

    def grant_role_to_user(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        This operation grants a specified role to the current user. Once granted the role, the user gets permissions allowed for the current role and can perform certain operations.

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/grant_role",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def revoker_role_from_user(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        This operation revokes a privilege granted to the current role.
        > Notes
        > To complete this operation, you need to enable authentication on your Milvus instance. For details, refer to [Authenticate User Access](https://milvus.io/docs/authenticate.md).

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/revoke_role",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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


class AsyncRawUserOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_user(
        self, *, user_name: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        This operation creates a new user with a corresponding password.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        password : str
            The corresponding password to the new user to create.
            The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/create",
            method="POST",
            json={
                "userName": user_name,
                "password": password,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def update_user_password(
        self,
        *,
        user_name: str,
        password: str,
        new_password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        This operation updates the password for a specific user.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        password : str
            The corresponding password to the new user to create.
            The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        new_password : str
            The new password for the specified user.    The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/update_password",
            method="POST",
            json={
                "userName": user_name,
                "password": password,
                "newPassword": new_password,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def drop_user(
        self, *, user_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        This operation deletes an existing user.

        Parameters
        ----------
        user_name : str
            The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/drop",
            method="POST",
            json={
                "userName": user_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def describe_user(
        self, *, user_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbUsersDescribeResponse]:
        """
        This operation describes the detailed information of a specific user.

        Parameters
        ----------
        user_name : str
              The name of the user to describe.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbUsersDescribeResponse]
            成功
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/describe",
            method="POST",
            json={
                "userName": user_name,
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
                    PostV2VectordbUsersDescribeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbUsersDescribeResponse,
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

    async def list_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbUsersListResponse]:
        """
        This operation lists the information of all existing users.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbUsersListResponse]
            An object that contains contains the user information.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/list",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV2VectordbUsersListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbUsersListResponse,
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

    async def grant_role_to_user(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        This operation grants a specified role to the current user. Once granted the role, the user gets permissions allowed for the current role and can perform certain operations.

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/grant_role",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def revoker_role_from_user(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        This operation revokes a privilege granted to the current role.
        > Notes
        > To complete this operation, you need to enable authentication on your Milvus instance. For details, refer to [Authenticate User Access](https://milvus.io/docs/authenticate.md).

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/users/revoke_role",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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
