

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.add_group_members_response import AddGroupMembersResponse
from .types.create_group_request_group import CreateGroupRequestGroup
from .types.create_group_response import CreateGroupResponse
from .types.delete_group_response import DeleteGroupResponse
from .types.get_group_response import GetGroupResponse
from .types.list_group_members_response import ListGroupMembersResponse
from .types.list_groups_response import ListGroupsResponse
from .types.remove_group_members_response import RemoveGroupMembersResponse
from .types.update_group_request_group import UpdateGroupRequestGroup
from .types.update_group_response import UpdateGroupResponse


OMIT = typing.cast(typing.Any, ...)


class RawGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_group(
        self, *, group: CreateGroupRequestGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateGroupResponse]:
        """
        Parameters
        ----------
        group : CreateGroupRequestGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateGroupResponse]
            group created
        """
        _response = self._client_wrapper.httpx_client.request(
            "admin/groups.json",
            method="POST",
            json={
                "group": convert_and_respect_annotation_metadata(
                    object_=group, annotation=CreateGroupRequestGroup, direction="write"
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
                    CreateGroupResponse,
                    parse_obj_as(
                        type_=CreateGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_group(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteGroupResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteGroupResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"admin/groups/{jsonable_encoder(id)}.json",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteGroupResponse,
                    parse_obj_as(
                        type_=DeleteGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_groups(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListGroupsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListGroupsResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListGroupsResponse,
                    parse_obj_as(
                        type_=ListGroupsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_group(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetGroupResponse]:
        """
        Parameters
        ----------
        id : str
            Use group name instead of id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetGroupResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(id)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGroupResponse,
                    parse_obj_as(
                        type_=GetGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_group(
        self, id: int, *, group: UpdateGroupRequestGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateGroupResponse]:
        """
        Parameters
        ----------
        id : int

        group : UpdateGroupRequestGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateGroupResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(id)}.json",
            method="PUT",
            json={
                "group": convert_and_respect_annotation_metadata(
                    object_=group, annotation=UpdateGroupRequestGroup, direction="write"
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
                    UpdateGroupResponse,
                    parse_obj_as(
                        type_=UpdateGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_group_members(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListGroupMembersResponse]:
        """
        Parameters
        ----------
        id : str
            Use group name instead of id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListGroupMembersResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(id)}/members.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListGroupMembersResponse,
                    parse_obj_as(
                        type_=ListGroupMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_group_members(
        self,
        id: int,
        *,
        usernames: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AddGroupMembersResponse]:
        """
        Parameters
        ----------
        id : int

        usernames : typing.Optional[str]
            comma separated list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddGroupMembersResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(id)}/members.json",
            method="PUT",
            json={
                "usernames": usernames,
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
                    AddGroupMembersResponse,
                    parse_obj_as(
                        type_=AddGroupMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_group_members(
        self,
        id: int,
        *,
        usernames: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RemoveGroupMembersResponse]:
        """
        Parameters
        ----------
        id : int

        usernames : typing.Optional[str]
            comma separated list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RemoveGroupMembersResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(id)}/members.json",
            method="DELETE",
            json={
                "usernames": usernames,
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
                    RemoveGroupMembersResponse,
                    parse_obj_as(
                        type_=RemoveGroupMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_group(
        self, *, group: CreateGroupRequestGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateGroupResponse]:
        """
        Parameters
        ----------
        group : CreateGroupRequestGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateGroupResponse]
            group created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "admin/groups.json",
            method="POST",
            json={
                "group": convert_and_respect_annotation_metadata(
                    object_=group, annotation=CreateGroupRequestGroup, direction="write"
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
                    CreateGroupResponse,
                    parse_obj_as(
                        type_=CreateGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_group(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteGroupResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteGroupResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"admin/groups/{jsonable_encoder(id)}.json",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteGroupResponse,
                    parse_obj_as(
                        type_=DeleteGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_groups(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListGroupsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListGroupsResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListGroupsResponse,
                    parse_obj_as(
                        type_=ListGroupsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_group(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetGroupResponse]:
        """
        Parameters
        ----------
        id : str
            Use group name instead of id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetGroupResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(id)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGroupResponse,
                    parse_obj_as(
                        type_=GetGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_group(
        self, id: int, *, group: UpdateGroupRequestGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateGroupResponse]:
        """
        Parameters
        ----------
        id : int

        group : UpdateGroupRequestGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateGroupResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(id)}.json",
            method="PUT",
            json={
                "group": convert_and_respect_annotation_metadata(
                    object_=group, annotation=UpdateGroupRequestGroup, direction="write"
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
                    UpdateGroupResponse,
                    parse_obj_as(
                        type_=UpdateGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_group_members(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListGroupMembersResponse]:
        """
        Parameters
        ----------
        id : str
            Use group name instead of id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListGroupMembersResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(id)}/members.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListGroupMembersResponse,
                    parse_obj_as(
                        type_=ListGroupMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_group_members(
        self,
        id: int,
        *,
        usernames: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AddGroupMembersResponse]:
        """
        Parameters
        ----------
        id : int

        usernames : typing.Optional[str]
            comma separated list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddGroupMembersResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(id)}/members.json",
            method="PUT",
            json={
                "usernames": usernames,
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
                    AddGroupMembersResponse,
                    parse_obj_as(
                        type_=AddGroupMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_group_members(
        self,
        id: int,
        *,
        usernames: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RemoveGroupMembersResponse]:
        """
        Parameters
        ----------
        id : int

        usernames : typing.Optional[str]
            comma separated list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RemoveGroupMembersResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(id)}/members.json",
            method="DELETE",
            json={
                "usernames": usernames,
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
                    RemoveGroupMembersResponse,
                    parse_obj_as(
                        type_=RemoveGroupMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
