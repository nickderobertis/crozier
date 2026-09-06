

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
from ..types.api_models_user_role_change import ApiModelsUserRoleChange
from ..types.api_paged_response_api_models_role import ApiPagedResponseApiModelsRole
from ..types.api_paged_response_api_models_user import ApiPagedResponseApiModelsUser
from ..types.api_paged_response_api_models_user_effective_permission import (
    ApiPagedResponseApiModelsUserEffectivePermission,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserpermissionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getusers(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseApiModelsUser]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The Role's ID

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseApiModelsUser]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Roles/{encode_path_param(id)}/Users",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseApiModelsUser,
                    parse_obj_as(
                        type_=ApiPagedResponseApiModelsUser,
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

    def put(
        self,
        id: int,
        *,
        request: typing.Sequence[ApiModelsUserRoleChange],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        request : typing.Sequence[ApiModelsUserRoleChange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}/Roles",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[ApiModelsUserRoleChange], direction="write"
            ),
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

    def getpermissions(
        self,
        id: int,
        *,
        permission: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseApiModelsUserEffectivePermission]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        permission : typing.Optional[str]
            Filter by permission name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseApiModelsUserEffectivePermission]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}/Permissions",
            method="GET",
            params={
                "Permission": permission,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseApiModelsUserEffectivePermission,
                    parse_obj_as(
                        type_=ApiPagedResponseApiModelsUserEffectivePermission,
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

    def getcurrentuserroles(
        self,
        *,
        role: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseApiModelsRole]:
        """
        No Documentation Found.

        Parameters
        ----------
        role : typing.Optional[str]
            Filter by role name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseApiModelsRole]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Users/Current/Roles",
            method="GET",
            params={
                "Role": role,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseApiModelsRole,
                    parse_obj_as(
                        type_=ApiPagedResponseApiModelsRole,
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

    def getroles(
        self,
        id: int,
        *,
        role: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseApiModelsRole]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        role : typing.Optional[str]
            Filter by role name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseApiModelsRole]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}/Roles",
            method="GET",
            params={
                "Role": role,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseApiModelsRole,
                    parse_obj_as(
                        type_=ApiPagedResponseApiModelsRole,
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


class AsyncRawUserpermissionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getusers(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseApiModelsUser]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The Role's ID

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseApiModelsUser]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Roles/{encode_path_param(id)}/Users",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseApiModelsUser,
                    parse_obj_as(
                        type_=ApiPagedResponseApiModelsUser,
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

    async def put(
        self,
        id: int,
        *,
        request: typing.Sequence[ApiModelsUserRoleChange],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        request : typing.Sequence[ApiModelsUserRoleChange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}/Roles",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[ApiModelsUserRoleChange], direction="write"
            ),
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

    async def getpermissions(
        self,
        id: int,
        *,
        permission: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseApiModelsUserEffectivePermission]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        permission : typing.Optional[str]
            Filter by permission name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseApiModelsUserEffectivePermission]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}/Permissions",
            method="GET",
            params={
                "Permission": permission,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseApiModelsUserEffectivePermission,
                    parse_obj_as(
                        type_=ApiPagedResponseApiModelsUserEffectivePermission,
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

    async def getcurrentuserroles(
        self,
        *,
        role: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseApiModelsRole]:
        """
        No Documentation Found.

        Parameters
        ----------
        role : typing.Optional[str]
            Filter by role name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseApiModelsRole]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Users/Current/Roles",
            method="GET",
            params={
                "Role": role,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseApiModelsRole,
                    parse_obj_as(
                        type_=ApiPagedResponseApiModelsRole,
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

    async def getroles(
        self,
        id: int,
        *,
        role: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseApiModelsRole]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The User's ID

        role : typing.Optional[str]
            Filter by role name. Supports ending wildcard (*). Optional.

        limit : typing.Optional[int]
            The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseApiModelsRole]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Users/{encode_path_param(id)}/Roles",
            method="GET",
            params={
                "Role": role,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseApiModelsRole,
                    parse_obj_as(
                        type_=ApiPagedResponseApiModelsRole,
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
