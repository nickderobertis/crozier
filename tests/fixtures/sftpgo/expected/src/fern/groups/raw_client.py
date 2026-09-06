

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
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.api_response import ApiResponse
from ..types.group import Group
from ..types.group_user_settings import GroupUserSettings
from ..types.virtual_folder import VirtualFolder
from .types.get_groups_request_order import GetGroupsRequestOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_groups(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Group]]:
        """
        Returns an array with one or more groups

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetGroupsRequestOrder]
            Ordering groups by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Group]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Group],
                    parse_obj_as(
                        type_=typing.List[Group],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_group(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        user_settings: typing.Optional[GroupUserSettings] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Group]:
        """
        Adds a new group

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        user_settings : typing.Optional[GroupUserSettings]

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and folders

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups",
            method="POST",
            params={
                "confidential_data": confidential_data,
            },
            json={
                "id": id,
                "name": name,
                "description": description,
                "created_at": created_at,
                "updated_at": updated_at,
                "user_settings": convert_and_respect_annotation_metadata(
                    object_=user_settings, annotation=GroupUserSettings, direction="write"
                ),
                "virtual_folders": convert_and_respect_annotation_metadata(
                    object_=virtual_folders, annotation=typing.Sequence[VirtualFolder], direction="write"
                ),
                "users": users,
                "admins": admins,
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
                    Group,
                    parse_obj_as(
                        type_=Group,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_group_by_name(
        self,
        name: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Group]:
        """
        Returns the group with the given name if it exists.

        Parameters
        ----------
        name : str
            group name

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(name)}",
            method="GET",
            params={
                "confidential_data": confidential_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Group,
                    parse_obj_as(
                        type_=Group,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_group(
        self,
        name_: str,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        user_settings: typing.Optional[GroupUserSettings] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiResponse]:
        """
        Updates an existing group

        Parameters
        ----------
        name_ : str
            group name

        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        user_settings : typing.Optional[GroupUserSettings]

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and folders

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(name_)}",
            method="PUT",
            json={
                "id": id,
                "name": name,
                "description": description,
                "created_at": created_at,
                "updated_at": updated_at,
                "user_settings": convert_and_respect_annotation_metadata(
                    object_=user_settings, annotation=GroupUserSettings, direction="write"
                ),
                "virtual_folders": convert_and_respect_annotation_metadata(
                    object_=virtual_folders, annotation=typing.Sequence[VirtualFolder], direction="write"
                ),
                "users": users,
                "admins": admins,
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
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_group(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiResponse]:
        """
        Deletes an existing group. A group referenced by users or admins cannot be deleted, remove the references first

        Parameters
        ----------
        name : str
            group name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_groups(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Group]]:
        """
        Returns an array with one or more groups

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetGroupsRequestOrder]
            Ordering groups by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Group]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Group],
                    parse_obj_as(
                        type_=typing.List[Group],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_group(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        user_settings: typing.Optional[GroupUserSettings] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Group]:
        """
        Adds a new group

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        user_settings : typing.Optional[GroupUserSettings]

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and folders

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups",
            method="POST",
            params={
                "confidential_data": confidential_data,
            },
            json={
                "id": id,
                "name": name,
                "description": description,
                "created_at": created_at,
                "updated_at": updated_at,
                "user_settings": convert_and_respect_annotation_metadata(
                    object_=user_settings, annotation=GroupUserSettings, direction="write"
                ),
                "virtual_folders": convert_and_respect_annotation_metadata(
                    object_=virtual_folders, annotation=typing.Sequence[VirtualFolder], direction="write"
                ),
                "users": users,
                "admins": admins,
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
                    Group,
                    parse_obj_as(
                        type_=Group,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_group_by_name(
        self,
        name: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Group]:
        """
        Returns the group with the given name if it exists.

        Parameters
        ----------
        name : str
            group name

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(name)}",
            method="GET",
            params={
                "confidential_data": confidential_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Group,
                    parse_obj_as(
                        type_=Group,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_group(
        self,
        name_: str,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        user_settings: typing.Optional[GroupUserSettings] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiResponse]:
        """
        Updates an existing group

        Parameters
        ----------
        name_ : str
            group name

        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        user_settings : typing.Optional[GroupUserSettings]

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and folders

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(name_)}",
            method="PUT",
            json={
                "id": id,
                "name": name,
                "description": description,
                "created_at": created_at,
                "updated_at": updated_at,
                "user_settings": convert_and_respect_annotation_metadata(
                    object_=user_settings, annotation=GroupUserSettings, direction="write"
                ),
                "virtual_folders": convert_and_respect_annotation_metadata(
                    object_=virtual_folders, annotation=typing.Sequence[VirtualFolder], direction="write"
                ),
                "users": users,
                "admins": admins,
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
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_group(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiResponse]:
        """
        Deletes an existing group. A group referenced by users or admins cannot be deleted, remove the references first

        Parameters
        ----------
        name : str
            group name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
