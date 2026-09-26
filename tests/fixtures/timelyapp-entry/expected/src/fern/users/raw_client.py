

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
from ..types.v1user import V1User
from ..types.v1users_create_user import V1UsersCreateUser
from .types.list_users_request_filter import ListUsersRequestFilter
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_current_user(
        self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1User]:
        """
        Returns the current user information for the authenticated user.

        Parameters
        ----------
        account_id : int
            Workspace id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1User]
            current user
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/current",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1User,
                    parse_obj_as(
                        type_=V1User,
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
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        filter: typing.Optional[ListUsersRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1User]]:
        """
        Lists users in the account. Requires global user read permission or project update permission.

        Parameters
        ----------
        account_id : int
            Workspace id

        limit : typing.Optional[int]
            Maximum number of results to return

        offset : typing.Optional[int]
            Number of results to skip

        order : typing.Optional[str]
            Sort order

        filter : typing.Optional[ListUsersRequestFilter]
            Filter for deleted users

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1User]]
            users list
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "order": order,
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1User],
                    parse_obj_as(
                        type_=typing.List[V1User],
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

    def invite_user(
        self, account_id: int, *, user: V1UsersCreateUser, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1User]:
        """
        Invites user to the account. Requires trial/active subscription as also available seats in the workspace to accommodate additional users.

        Parameters
        ----------
        account_id : int
            Workspace id

        user : V1UsersCreateUser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1User]
            user invited
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users",
            method="POST",
            json={
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=V1UsersCreateUser, direction="write"
                ),
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
                    V1User,
                    parse_obj_as(
                        type_=V1User,
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
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1User]:
        """
        Get specific user details. Requires read permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1User]
            user details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1User,
                    parse_obj_as(
                        type_=V1User,
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
        account_id: int,
        id: int,
        *,
        user: V1UsersCreateUser,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1User]:
        """
        Update user details. Requires update permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        user : V1UsersCreateUser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1User]
            user updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/{encode_path_param(id)}",
            method="PUT",
            json={
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=V1UsersCreateUser, direction="write"
                ),
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
                    V1User,
                    parse_obj_as(
                        type_=V1User,
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
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete/remove user from account. Requires delete permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            user deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/{encode_path_param(id)}",
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

    def search_users(
        self,
        account_id: int,
        *,
        q: str,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1User]]:
        """
        Search users. Requires create or update project permission.

        Parameters
        ----------
        account_id : int
            Workspace id

        q : str
            Search query

        per_page : typing.Optional[int]
            Results per page

        page : typing.Optional[int]
            Page number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1User]]
            search results
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/search",
            method="GET",
            params={
                "q": q,
                "per_page": per_page,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1User],
                    parse_obj_as(
                        type_=typing.List[V1User],
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

    async def get_current_user(
        self, account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1User]:
        """
        Returns the current user information for the authenticated user.

        Parameters
        ----------
        account_id : int
            Workspace id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1User]
            current user
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/current",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1User,
                    parse_obj_as(
                        type_=V1User,
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
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        filter: typing.Optional[ListUsersRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1User]]:
        """
        Lists users in the account. Requires global user read permission or project update permission.

        Parameters
        ----------
        account_id : int
            Workspace id

        limit : typing.Optional[int]
            Maximum number of results to return

        offset : typing.Optional[int]
            Number of results to skip

        order : typing.Optional[str]
            Sort order

        filter : typing.Optional[ListUsersRequestFilter]
            Filter for deleted users

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1User]]
            users list
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "order": order,
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1User],
                    parse_obj_as(
                        type_=typing.List[V1User],
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

    async def invite_user(
        self, account_id: int, *, user: V1UsersCreateUser, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1User]:
        """
        Invites user to the account. Requires trial/active subscription as also available seats in the workspace to accommodate additional users.

        Parameters
        ----------
        account_id : int
            Workspace id

        user : V1UsersCreateUser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1User]
            user invited
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users",
            method="POST",
            json={
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=V1UsersCreateUser, direction="write"
                ),
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
                    V1User,
                    parse_obj_as(
                        type_=V1User,
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
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1User]:
        """
        Get specific user details. Requires read permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1User]
            user details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1User,
                    parse_obj_as(
                        type_=V1User,
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
        account_id: int,
        id: int,
        *,
        user: V1UsersCreateUser,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1User]:
        """
        Update user details. Requires update permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        user : V1UsersCreateUser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1User]
            user updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/{encode_path_param(id)}",
            method="PUT",
            json={
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=V1UsersCreateUser, direction="write"
                ),
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
                    V1User,
                    parse_obj_as(
                        type_=V1User,
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
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete/remove user from account. Requires delete permission for the user.

        Parameters
        ----------
        account_id : int
            Workspace id

        id : int
            User id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            user deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/{encode_path_param(id)}",
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

    async def search_users(
        self,
        account_id: int,
        *,
        q: str,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1User]]:
        """
        Search users. Requires create or update project permission.

        Parameters
        ----------
        account_id : int
            Workspace id

        q : str
            Search query

        per_page : typing.Optional[int]
            Results per page

        page : typing.Optional[int]
            Page number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1User]]
            search results
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/search",
            method="GET",
            params={
                "q": q,
                "per_page": per_page,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1User],
                    parse_obj_as(
                        type_=typing.List[V1User],
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
