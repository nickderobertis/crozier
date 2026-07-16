

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.group import Group
from ..types.ip_network import IpNetwork
from ..types.object_permission import ObjectPermission
from ..types.token import Token
from ..types.user import User
from .types.users_groups_list_response import UsersGroupsListResponse
from .types.users_permissions_list_response import UsersPermissionsListResponse
from .types.users_tokens_list_response import UsersTokensListResponse
from .types.users_users_list_response import UsersUsersListResponse


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def config_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Return the UserConfig for the currently authenticated User.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/config/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def groups_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsersGroupsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        q : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsersGroupsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/groups/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "q": q,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersGroupsListResponse,
                    parse_obj_as(
                        type_=UsersGroupsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def groups_create(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Group]:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/groups/",
            method="POST",
            json={
                "display": display,
                "id": id,
                "name": name,
                "url": url,
                "user_count": user_count,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def groups_bulk_update(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Group]:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/groups/",
            method="PUT",
            json={
                "display": display,
                "id": id,
                "name": name,
                "url": url,
                "user_count": user_count,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/groups/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def groups_bulk_partial_update(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Group]:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/groups/",
            method="PATCH",
            json={
                "display": display,
                "id": id,
                "name": name,
                "url": url,
                "user_count": user_count,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def groups_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Group]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/groups/{jsonable_encoder(id)}/",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def groups_update(
        self,
        id_: int,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Group]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this group.

        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/groups/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "display": display,
                "id": id,
                "name": name,
                "url": url,
                "user_count": user_count,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/groups/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Group]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this group.

        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/groups/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "display": display,
                "id": id,
                "name": name,
                "url": url,
                "user_count": user_count,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permissions_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        object_types: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        object_types_n: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsersPermissionsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        enabled : typing.Optional[str]


        object_types : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        user_id : typing.Optional[str]


        user : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        object_types_n : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        user_id_n : typing.Optional[str]


        user_n : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsersPermissionsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/permissions/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "enabled": enabled,
                "object_types": object_types,
                "description": description,
                "q": q,
                "user_id": user_id,
                "user": user,
                "group_id": group_id,
                "group": group,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "object_types__n": object_types_n,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "user_id__n": user_id_n,
                "user__n": user_n,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersPermissionsListResponse,
                    parse_obj_as(
                        type_=UsersPermissionsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permissions_create(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ObjectPermission]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/permissions/",
            method="POST",
            json={
                "actions": actions,
                "constraints": constraints,
                "description": description,
                "display": display,
                "enabled": enabled,
                "groups": groups,
                "id": id,
                "name": name,
                "object_types": object_types,
                "url": url,
                "users": users,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permissions_bulk_update(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ObjectPermission]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/permissions/",
            method="PUT",
            json={
                "actions": actions,
                "constraints": constraints,
                "description": description,
                "display": display,
                "enabled": enabled,
                "groups": groups,
                "id": id,
                "name": name,
                "object_types": object_types,
                "url": url,
                "users": users,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permissions_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/permissions/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permissions_bulk_partial_update(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ObjectPermission]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/permissions/",
            method="PATCH",
            json={
                "actions": actions,
                "constraints": constraints,
                "description": description,
                "display": display,
                "enabled": enabled,
                "groups": groups,
                "id": id,
                "name": name,
                "object_types": object_types,
                "url": url,
                "users": users,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permissions_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ObjectPermission]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/permissions/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permissions_update(
        self,
        id_: int,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this permission.

        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ObjectPermission]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/permissions/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "actions": actions,
                "constraints": constraints,
                "description": description,
                "display": display,
                "enabled": enabled,
                "groups": groups,
                "id": id,
                "name": name,
                "object_types": object_types,
                "url": url,
                "users": users,
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
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permissions_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/permissions/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permissions_partial_update(
        self,
        id_: int,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this permission.

        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ObjectPermission]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/permissions/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "actions": actions,
                "constraints": constraints,
                "description": description,
                "display": display,
                "enabled": enabled,
                "groups": groups,
                "id": id,
                "name": name,
                "object_types": object_types,
                "url": url,
                "users": users,
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
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tokens_list(
        self,
        *,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        write_enabled: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        expires_gte: typing.Optional[str] = None,
        expires_lte: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        key_n: typing.Optional[str] = None,
        key_ic: typing.Optional[str] = None,
        key_nic: typing.Optional[str] = None,
        key_iew: typing.Optional[str] = None,
        key_niew: typing.Optional[str] = None,
        key_isw: typing.Optional[str] = None,
        key_nisw: typing.Optional[str] = None,
        key_ie: typing.Optional[str] = None,
        key_nie: typing.Optional[str] = None,
        key_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsersTokensListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        key : typing.Optional[str]


        write_enabled : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        user_id : typing.Optional[str]


        user : typing.Optional[str]


        created : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_lte : typing.Optional[str]


        expires : typing.Optional[str]


        expires_gte : typing.Optional[str]


        expires_lte : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        key_n : typing.Optional[str]


        key_ic : typing.Optional[str]


        key_nic : typing.Optional[str]


        key_iew : typing.Optional[str]


        key_niew : typing.Optional[str]


        key_isw : typing.Optional[str]


        key_nisw : typing.Optional[str]


        key_ie : typing.Optional[str]


        key_nie : typing.Optional[str]


        key_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        user_id_n : typing.Optional[str]


        user_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsersTokensListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/tokens/",
            method="GET",
            params={
                "id": id,
                "key": key,
                "write_enabled": write_enabled,
                "description": description,
                "q": q,
                "user_id": user_id,
                "user": user,
                "created": created,
                "created__gte": created_gte,
                "created__lte": created_lte,
                "expires": expires,
                "expires__gte": expires_gte,
                "expires__lte": expires_lte,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "key__n": key_n,
                "key__ic": key_ic,
                "key__nic": key_nic,
                "key__iew": key_iew,
                "key__niew": key_niew,
                "key__isw": key_isw,
                "key__nisw": key_nisw,
                "key__ie": key_ie,
                "key__nie": key_nie,
                "key__empty": key_empty,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "user_id__n": user_id_n,
                "user__n": user_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersTokensListResponse,
                    parse_obj_as(
                        type_=UsersTokensListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tokens_create(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Token]:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Token]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/tokens/",
            method="POST",
            json={
                "allowed_ips": convert_and_respect_annotation_metadata(
                    object_=allowed_ips, annotation=typing.Sequence[IpNetwork], direction="write"
                ),
                "created": created,
                "description": description,
                "display": display,
                "expires": expires,
                "id": id,
                "key": key,
                "last_used": last_used,
                "url": url,
                "user": user,
                "write_enabled": write_enabled,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tokens_bulk_update(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Token]:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Token]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/tokens/",
            method="PUT",
            json={
                "allowed_ips": convert_and_respect_annotation_metadata(
                    object_=allowed_ips, annotation=typing.Sequence[IpNetwork], direction="write"
                ),
                "created": created,
                "description": description,
                "display": display,
                "expires": expires,
                "id": id,
                "key": key,
                "last_used": last_used,
                "url": url,
                "user": user,
                "write_enabled": write_enabled,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tokens_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/tokens/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tokens_bulk_partial_update(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Token]:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Token]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/tokens/",
            method="PATCH",
            json={
                "allowed_ips": convert_and_respect_annotation_metadata(
                    object_=allowed_ips, annotation=typing.Sequence[IpNetwork], direction="write"
                ),
                "created": created,
                "description": description,
                "display": display,
                "expires": expires,
                "id": id,
                "key": key,
                "last_used": last_used,
                "url": url,
                "user": user,
                "write_enabled": write_enabled,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tokens_provision_create(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Non-authenticated REST API endpoint via which a user may create a Token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/tokens/provision/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tokens_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Token]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Token]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/tokens/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tokens_update(
        self,
        id_: int,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Token]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this token.

        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Token]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/tokens/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "allowed_ips": convert_and_respect_annotation_metadata(
                    object_=allowed_ips, annotation=typing.Sequence[IpNetwork], direction="write"
                ),
                "created": created,
                "description": description,
                "display": display,
                "expires": expires,
                "id": id,
                "key": key,
                "last_used": last_used,
                "url": url,
                "user": user,
                "write_enabled": write_enabled,
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
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tokens_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/tokens/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tokens_partial_update(
        self,
        id_: int,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Token]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this token.

        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Token]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/tokens/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "allowed_ips": convert_and_respect_annotation_metadata(
                    object_=allowed_ips, annotation=typing.Sequence[IpNetwork], direction="write"
                ),
                "created": created,
                "description": description,
                "display": display,
                "expires": expires,
                "id": id,
                "key": key,
                "last_used": last_used,
                "url": url,
                "user": user,
                "write_enabled": write_enabled,
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
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def users_list(
        self,
        *,
        id: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        is_staff: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        username_n: typing.Optional[str] = None,
        username_ic: typing.Optional[str] = None,
        username_nic: typing.Optional[str] = None,
        username_iew: typing.Optional[str] = None,
        username_niew: typing.Optional[str] = None,
        username_isw: typing.Optional[str] = None,
        username_nisw: typing.Optional[str] = None,
        username_ie: typing.Optional[str] = None,
        username_nie: typing.Optional[str] = None,
        username_empty: typing.Optional[str] = None,
        first_name_n: typing.Optional[str] = None,
        first_name_ic: typing.Optional[str] = None,
        first_name_nic: typing.Optional[str] = None,
        first_name_iew: typing.Optional[str] = None,
        first_name_niew: typing.Optional[str] = None,
        first_name_isw: typing.Optional[str] = None,
        first_name_nisw: typing.Optional[str] = None,
        first_name_ie: typing.Optional[str] = None,
        first_name_nie: typing.Optional[str] = None,
        first_name_empty: typing.Optional[str] = None,
        last_name_n: typing.Optional[str] = None,
        last_name_ic: typing.Optional[str] = None,
        last_name_nic: typing.Optional[str] = None,
        last_name_iew: typing.Optional[str] = None,
        last_name_niew: typing.Optional[str] = None,
        last_name_isw: typing.Optional[str] = None,
        last_name_nisw: typing.Optional[str] = None,
        last_name_ie: typing.Optional[str] = None,
        last_name_nie: typing.Optional[str] = None,
        last_name_empty: typing.Optional[str] = None,
        email_n: typing.Optional[str] = None,
        email_ic: typing.Optional[str] = None,
        email_nic: typing.Optional[str] = None,
        email_iew: typing.Optional[str] = None,
        email_niew: typing.Optional[str] = None,
        email_isw: typing.Optional[str] = None,
        email_nisw: typing.Optional[str] = None,
        email_ie: typing.Optional[str] = None,
        email_nie: typing.Optional[str] = None,
        email_empty: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsersUsersListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        username : typing.Optional[str]


        first_name : typing.Optional[str]


        last_name : typing.Optional[str]


        email : typing.Optional[str]


        is_staff : typing.Optional[str]


        is_active : typing.Optional[str]


        q : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        username_n : typing.Optional[str]


        username_ic : typing.Optional[str]


        username_nic : typing.Optional[str]


        username_iew : typing.Optional[str]


        username_niew : typing.Optional[str]


        username_isw : typing.Optional[str]


        username_nisw : typing.Optional[str]


        username_ie : typing.Optional[str]


        username_nie : typing.Optional[str]


        username_empty : typing.Optional[str]


        first_name_n : typing.Optional[str]


        first_name_ic : typing.Optional[str]


        first_name_nic : typing.Optional[str]


        first_name_iew : typing.Optional[str]


        first_name_niew : typing.Optional[str]


        first_name_isw : typing.Optional[str]


        first_name_nisw : typing.Optional[str]


        first_name_ie : typing.Optional[str]


        first_name_nie : typing.Optional[str]


        first_name_empty : typing.Optional[str]


        last_name_n : typing.Optional[str]


        last_name_ic : typing.Optional[str]


        last_name_nic : typing.Optional[str]


        last_name_iew : typing.Optional[str]


        last_name_niew : typing.Optional[str]


        last_name_isw : typing.Optional[str]


        last_name_nisw : typing.Optional[str]


        last_name_ie : typing.Optional[str]


        last_name_nie : typing.Optional[str]


        last_name_empty : typing.Optional[str]


        email_n : typing.Optional[str]


        email_ic : typing.Optional[str]


        email_nic : typing.Optional[str]


        email_iew : typing.Optional[str]


        email_niew : typing.Optional[str]


        email_isw : typing.Optional[str]


        email_nisw : typing.Optional[str]


        email_ie : typing.Optional[str]


        email_nie : typing.Optional[str]


        email_empty : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsersUsersListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/users/",
            method="GET",
            params={
                "id": id,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "is_staff": is_staff,
                "is_active": is_active,
                "q": q,
                "group_id": group_id,
                "group": group,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "username__n": username_n,
                "username__ic": username_ic,
                "username__nic": username_nic,
                "username__iew": username_iew,
                "username__niew": username_niew,
                "username__isw": username_isw,
                "username__nisw": username_nisw,
                "username__ie": username_ie,
                "username__nie": username_nie,
                "username__empty": username_empty,
                "first_name__n": first_name_n,
                "first_name__ic": first_name_ic,
                "first_name__nic": first_name_nic,
                "first_name__iew": first_name_iew,
                "first_name__niew": first_name_niew,
                "first_name__isw": first_name_isw,
                "first_name__nisw": first_name_nisw,
                "first_name__ie": first_name_ie,
                "first_name__nie": first_name_nie,
                "first_name__empty": first_name_empty,
                "last_name__n": last_name_n,
                "last_name__ic": last_name_ic,
                "last_name__nic": last_name_nic,
                "last_name__iew": last_name_iew,
                "last_name__niew": last_name_niew,
                "last_name__isw": last_name_isw,
                "last_name__nisw": last_name_nisw,
                "last_name__ie": last_name_ie,
                "last_name__nie": last_name_nie,
                "last_name__empty": last_name_empty,
                "email__n": email_n,
                "email__ic": email_ic,
                "email__nic": email_nic,
                "email__iew": email_iew,
                "email__niew": email_niew,
                "email__isw": email_isw,
                "email__nisw": email_nisw,
                "email__ie": email_ie,
                "email__nie": email_nie,
                "email__empty": email_empty,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersUsersListResponse,
                    parse_obj_as(
                        type_=UsersUsersListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def users_create(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[User]:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/users/",
            method="POST",
            json={
                "date_joined": date_joined,
                "display": display,
                "email": email,
                "first_name": first_name,
                "groups": groups,
                "id": id,
                "is_active": is_active,
                "is_staff": is_staff,
                "last_name": last_name,
                "password": password,
                "url": url,
                "username": username,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def users_bulk_update(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[User]:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/users/",
            method="PUT",
            json={
                "date_joined": date_joined,
                "display": display,
                "email": email,
                "first_name": first_name,
                "groups": groups,
                "id": id,
                "is_active": is_active,
                "is_staff": is_staff,
                "last_name": last_name,
                "password": password,
                "url": url,
                "username": username,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def users_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/users/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def users_bulk_partial_update(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[User]:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]

        """
        _response = self._client_wrapper.httpx_client.request(
            "users/users/",
            method="PATCH",
            json={
                "date_joined": date_joined,
                "display": display,
                "email": email,
                "first_name": first_name,
                "groups": groups,
                "id": id,
                "is_active": is_active,
                "is_staff": is_staff,
                "last_name": last_name,
                "password": password,
                "url": url,
                "username": username,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def users_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[User]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/users/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def users_update(
        self,
        id_: int,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[User]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this user.

        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/users/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "date_joined": date_joined,
                "display": display,
                "email": email,
                "first_name": first_name,
                "groups": groups,
                "id": id,
                "is_active": is_active,
                "is_staff": is_staff,
                "last_name": last_name,
                "password": password,
                "url": url,
                "username": username,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def users_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/users/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def users_partial_update(
        self,
        id_: int,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[User]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this user.

        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/users/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "date_joined": date_joined,
                "display": display,
                "email": email,
                "first_name": first_name,
                "groups": groups,
                "id": id,
                "is_active": is_active,
                "is_staff": is_staff,
                "last_name": last_name,
                "password": password,
                "url": url,
                "username": username,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def config_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        Return the UserConfig for the currently authenticated User.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/config/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def groups_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsersGroupsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        q : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsersGroupsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/groups/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "q": q,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersGroupsListResponse,
                    parse_obj_as(
                        type_=UsersGroupsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def groups_create(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Group]:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/groups/",
            method="POST",
            json={
                "display": display,
                "id": id,
                "name": name,
                "url": url,
                "user_count": user_count,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def groups_bulk_update(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Group]:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/groups/",
            method="PUT",
            json={
                "display": display,
                "id": id,
                "name": name,
                "url": url,
                "user_count": user_count,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def groups_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/groups/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def groups_bulk_partial_update(
        self,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Group]:
        """


        Parameters
        ----------
        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/groups/",
            method="PATCH",
            json={
                "display": display,
                "id": id,
                "name": name,
                "url": url,
                "user_count": user_count,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Group]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/groups/{jsonable_encoder(id)}/",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def groups_update(
        self,
        id_: int,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Group]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this group.

        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/groups/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "display": display,
                "id": id,
                "name": name,
                "url": url,
                "user_count": user_count,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def groups_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/groups/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        user_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Group]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this group.

        name : str

        display : typing.Optional[str]

        id : typing.Optional[int]

        url : typing.Optional[str]

        user_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/groups/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "display": display,
                "id": id,
                "name": name,
                "url": url,
                "user_count": user_count,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permissions_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        object_types: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        object_types_n: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsersPermissionsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        enabled : typing.Optional[str]


        object_types : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        user_id : typing.Optional[str]


        user : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        object_types_n : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        user_id_n : typing.Optional[str]


        user_n : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsersPermissionsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/permissions/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "enabled": enabled,
                "object_types": object_types,
                "description": description,
                "q": q,
                "user_id": user_id,
                "user": user,
                "group_id": group_id,
                "group": group,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "object_types__n": object_types_n,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "user_id__n": user_id_n,
                "user__n": user_n,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersPermissionsListResponse,
                    parse_obj_as(
                        type_=UsersPermissionsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permissions_create(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ObjectPermission]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/permissions/",
            method="POST",
            json={
                "actions": actions,
                "constraints": constraints,
                "description": description,
                "display": display,
                "enabled": enabled,
                "groups": groups,
                "id": id,
                "name": name,
                "object_types": object_types,
                "url": url,
                "users": users,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permissions_bulk_update(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ObjectPermission]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/permissions/",
            method="PUT",
            json={
                "actions": actions,
                "constraints": constraints,
                "description": description,
                "display": display,
                "enabled": enabled,
                "groups": groups,
                "id": id,
                "name": name,
                "object_types": object_types,
                "url": url,
                "users": users,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permissions_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/permissions/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permissions_bulk_partial_update(
        self,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ObjectPermission]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/permissions/",
            method="PATCH",
            json={
                "actions": actions,
                "constraints": constraints,
                "description": description,
                "display": display,
                "enabled": enabled,
                "groups": groups,
                "id": id,
                "name": name,
                "object_types": object_types,
                "url": url,
                "users": users,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permissions_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ObjectPermission]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/permissions/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permissions_update(
        self,
        id_: int,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this permission.

        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ObjectPermission]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/permissions/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "actions": actions,
                "constraints": constraints,
                "description": description,
                "display": display,
                "enabled": enabled,
                "groups": groups,
                "id": id,
                "name": name,
                "object_types": object_types,
                "url": url,
                "users": users,
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
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permissions_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/permissions/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permissions_partial_update(
        self,
        id_: int,
        *,
        actions: typing.Sequence[str],
        name: str,
        object_types: typing.Sequence[str],
        constraints: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        users: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ObjectPermission]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this permission.

        actions : typing.Sequence[str]
            The list of actions granted by this permission

        name : str

        object_types : typing.Sequence[str]

        constraints : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Queryset filter matching the applicable objects of the selected type(s)

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        groups : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        url : typing.Optional[str]

        users : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ObjectPermission]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/permissions/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "actions": actions,
                "constraints": constraints,
                "description": description,
                "display": display,
                "enabled": enabled,
                "groups": groups,
                "id": id,
                "name": name,
                "object_types": object_types,
                "url": url,
                "users": users,
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
                    ObjectPermission,
                    parse_obj_as(
                        type_=ObjectPermission,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tokens_list(
        self,
        *,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        write_enabled: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        expires_gte: typing.Optional[str] = None,
        expires_lte: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        key_n: typing.Optional[str] = None,
        key_ic: typing.Optional[str] = None,
        key_nic: typing.Optional[str] = None,
        key_iew: typing.Optional[str] = None,
        key_niew: typing.Optional[str] = None,
        key_isw: typing.Optional[str] = None,
        key_nisw: typing.Optional[str] = None,
        key_ie: typing.Optional[str] = None,
        key_nie: typing.Optional[str] = None,
        key_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsersTokensListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        key : typing.Optional[str]


        write_enabled : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        user_id : typing.Optional[str]


        user : typing.Optional[str]


        created : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_lte : typing.Optional[str]


        expires : typing.Optional[str]


        expires_gte : typing.Optional[str]


        expires_lte : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        key_n : typing.Optional[str]


        key_ic : typing.Optional[str]


        key_nic : typing.Optional[str]


        key_iew : typing.Optional[str]


        key_niew : typing.Optional[str]


        key_isw : typing.Optional[str]


        key_nisw : typing.Optional[str]


        key_ie : typing.Optional[str]


        key_nie : typing.Optional[str]


        key_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        user_id_n : typing.Optional[str]


        user_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsersTokensListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/tokens/",
            method="GET",
            params={
                "id": id,
                "key": key,
                "write_enabled": write_enabled,
                "description": description,
                "q": q,
                "user_id": user_id,
                "user": user,
                "created": created,
                "created__gte": created_gte,
                "created__lte": created_lte,
                "expires": expires,
                "expires__gte": expires_gte,
                "expires__lte": expires_lte,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "key__n": key_n,
                "key__ic": key_ic,
                "key__nic": key_nic,
                "key__iew": key_iew,
                "key__niew": key_niew,
                "key__isw": key_isw,
                "key__nisw": key_nisw,
                "key__ie": key_ie,
                "key__nie": key_nie,
                "key__empty": key_empty,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "user_id__n": user_id_n,
                "user__n": user_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersTokensListResponse,
                    parse_obj_as(
                        type_=UsersTokensListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tokens_create(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Token]:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Token]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/tokens/",
            method="POST",
            json={
                "allowed_ips": convert_and_respect_annotation_metadata(
                    object_=allowed_ips, annotation=typing.Sequence[IpNetwork], direction="write"
                ),
                "created": created,
                "description": description,
                "display": display,
                "expires": expires,
                "id": id,
                "key": key,
                "last_used": last_used,
                "url": url,
                "user": user,
                "write_enabled": write_enabled,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tokens_bulk_update(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Token]:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Token]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/tokens/",
            method="PUT",
            json={
                "allowed_ips": convert_and_respect_annotation_metadata(
                    object_=allowed_ips, annotation=typing.Sequence[IpNetwork], direction="write"
                ),
                "created": created,
                "description": description,
                "display": display,
                "expires": expires,
                "id": id,
                "key": key,
                "last_used": last_used,
                "url": url,
                "user": user,
                "write_enabled": write_enabled,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tokens_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/tokens/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tokens_bulk_partial_update(
        self,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Token]:
        """


        Parameters
        ----------
        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Token]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/tokens/",
            method="PATCH",
            json={
                "allowed_ips": convert_and_respect_annotation_metadata(
                    object_=allowed_ips, annotation=typing.Sequence[IpNetwork], direction="write"
                ),
                "created": created,
                "description": description,
                "display": display,
                "expires": expires,
                "id": id,
                "key": key,
                "last_used": last_used,
                "url": url,
                "user": user,
                "write_enabled": write_enabled,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tokens_provision_create(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Non-authenticated REST API endpoint via which a user may create a Token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/tokens/provision/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tokens_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Token]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Token]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/tokens/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tokens_update(
        self,
        id_: int,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Token]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this token.

        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Token]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/tokens/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "allowed_ips": convert_and_respect_annotation_metadata(
                    object_=allowed_ips, annotation=typing.Sequence[IpNetwork], direction="write"
                ),
                "created": created,
                "description": description,
                "display": display,
                "expires": expires,
                "id": id,
                "key": key,
                "last_used": last_used,
                "url": url,
                "user": user,
                "write_enabled": write_enabled,
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
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tokens_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/tokens/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tokens_partial_update(
        self,
        id_: int,
        *,
        user: int,
        allowed_ips: typing.Optional[typing.Sequence[IpNetwork]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        expires: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        key: typing.Optional[str] = OMIT,
        last_used: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        write_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Token]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this token.

        user : int

        allowed_ips : typing.Optional[typing.Sequence[IpNetwork]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        expires : typing.Optional[dt.datetime]

        id : typing.Optional[int]

        key : typing.Optional[str]

        last_used : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        write_enabled : typing.Optional[bool]
            Permit create/update/delete operations using this key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Token]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/tokens/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "allowed_ips": convert_and_respect_annotation_metadata(
                    object_=allowed_ips, annotation=typing.Sequence[IpNetwork], direction="write"
                ),
                "created": created,
                "description": description,
                "display": display,
                "expires": expires,
                "id": id,
                "key": key,
                "last_used": last_used,
                "url": url,
                "user": user,
                "write_enabled": write_enabled,
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
                    Token,
                    parse_obj_as(
                        type_=Token,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def users_list(
        self,
        *,
        id: typing.Optional[str] = None,
        username: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        is_staff: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        username_n: typing.Optional[str] = None,
        username_ic: typing.Optional[str] = None,
        username_nic: typing.Optional[str] = None,
        username_iew: typing.Optional[str] = None,
        username_niew: typing.Optional[str] = None,
        username_isw: typing.Optional[str] = None,
        username_nisw: typing.Optional[str] = None,
        username_ie: typing.Optional[str] = None,
        username_nie: typing.Optional[str] = None,
        username_empty: typing.Optional[str] = None,
        first_name_n: typing.Optional[str] = None,
        first_name_ic: typing.Optional[str] = None,
        first_name_nic: typing.Optional[str] = None,
        first_name_iew: typing.Optional[str] = None,
        first_name_niew: typing.Optional[str] = None,
        first_name_isw: typing.Optional[str] = None,
        first_name_nisw: typing.Optional[str] = None,
        first_name_ie: typing.Optional[str] = None,
        first_name_nie: typing.Optional[str] = None,
        first_name_empty: typing.Optional[str] = None,
        last_name_n: typing.Optional[str] = None,
        last_name_ic: typing.Optional[str] = None,
        last_name_nic: typing.Optional[str] = None,
        last_name_iew: typing.Optional[str] = None,
        last_name_niew: typing.Optional[str] = None,
        last_name_isw: typing.Optional[str] = None,
        last_name_nisw: typing.Optional[str] = None,
        last_name_ie: typing.Optional[str] = None,
        last_name_nie: typing.Optional[str] = None,
        last_name_empty: typing.Optional[str] = None,
        email_n: typing.Optional[str] = None,
        email_ic: typing.Optional[str] = None,
        email_nic: typing.Optional[str] = None,
        email_iew: typing.Optional[str] = None,
        email_niew: typing.Optional[str] = None,
        email_isw: typing.Optional[str] = None,
        email_nisw: typing.Optional[str] = None,
        email_ie: typing.Optional[str] = None,
        email_nie: typing.Optional[str] = None,
        email_empty: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsersUsersListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        username : typing.Optional[str]


        first_name : typing.Optional[str]


        last_name : typing.Optional[str]


        email : typing.Optional[str]


        is_staff : typing.Optional[str]


        is_active : typing.Optional[str]


        q : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        username_n : typing.Optional[str]


        username_ic : typing.Optional[str]


        username_nic : typing.Optional[str]


        username_iew : typing.Optional[str]


        username_niew : typing.Optional[str]


        username_isw : typing.Optional[str]


        username_nisw : typing.Optional[str]


        username_ie : typing.Optional[str]


        username_nie : typing.Optional[str]


        username_empty : typing.Optional[str]


        first_name_n : typing.Optional[str]


        first_name_ic : typing.Optional[str]


        first_name_nic : typing.Optional[str]


        first_name_iew : typing.Optional[str]


        first_name_niew : typing.Optional[str]


        first_name_isw : typing.Optional[str]


        first_name_nisw : typing.Optional[str]


        first_name_ie : typing.Optional[str]


        first_name_nie : typing.Optional[str]


        first_name_empty : typing.Optional[str]


        last_name_n : typing.Optional[str]


        last_name_ic : typing.Optional[str]


        last_name_nic : typing.Optional[str]


        last_name_iew : typing.Optional[str]


        last_name_niew : typing.Optional[str]


        last_name_isw : typing.Optional[str]


        last_name_nisw : typing.Optional[str]


        last_name_ie : typing.Optional[str]


        last_name_nie : typing.Optional[str]


        last_name_empty : typing.Optional[str]


        email_n : typing.Optional[str]


        email_ic : typing.Optional[str]


        email_nic : typing.Optional[str]


        email_iew : typing.Optional[str]


        email_niew : typing.Optional[str]


        email_isw : typing.Optional[str]


        email_nisw : typing.Optional[str]


        email_ie : typing.Optional[str]


        email_nie : typing.Optional[str]


        email_empty : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsersUsersListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/users/",
            method="GET",
            params={
                "id": id,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "is_staff": is_staff,
                "is_active": is_active,
                "q": q,
                "group_id": group_id,
                "group": group,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "username__n": username_n,
                "username__ic": username_ic,
                "username__nic": username_nic,
                "username__iew": username_iew,
                "username__niew": username_niew,
                "username__isw": username_isw,
                "username__nisw": username_nisw,
                "username__ie": username_ie,
                "username__nie": username_nie,
                "username__empty": username_empty,
                "first_name__n": first_name_n,
                "first_name__ic": first_name_ic,
                "first_name__nic": first_name_nic,
                "first_name__iew": first_name_iew,
                "first_name__niew": first_name_niew,
                "first_name__isw": first_name_isw,
                "first_name__nisw": first_name_nisw,
                "first_name__ie": first_name_ie,
                "first_name__nie": first_name_nie,
                "first_name__empty": first_name_empty,
                "last_name__n": last_name_n,
                "last_name__ic": last_name_ic,
                "last_name__nic": last_name_nic,
                "last_name__iew": last_name_iew,
                "last_name__niew": last_name_niew,
                "last_name__isw": last_name_isw,
                "last_name__nisw": last_name_nisw,
                "last_name__ie": last_name_ie,
                "last_name__nie": last_name_nie,
                "last_name__empty": last_name_empty,
                "email__n": email_n,
                "email__ic": email_ic,
                "email__nic": email_nic,
                "email__iew": email_iew,
                "email__niew": email_niew,
                "email__isw": email_isw,
                "email__nisw": email_nisw,
                "email__ie": email_ie,
                "email__nie": email_nie,
                "email__empty": email_empty,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersUsersListResponse,
                    parse_obj_as(
                        type_=UsersUsersListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def users_create(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[User]:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/users/",
            method="POST",
            json={
                "date_joined": date_joined,
                "display": display,
                "email": email,
                "first_name": first_name,
                "groups": groups,
                "id": id,
                "is_active": is_active,
                "is_staff": is_staff,
                "last_name": last_name,
                "password": password,
                "url": url,
                "username": username,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def users_bulk_update(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[User]:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/users/",
            method="PUT",
            json={
                "date_joined": date_joined,
                "display": display,
                "email": email,
                "first_name": first_name,
                "groups": groups,
                "id": id,
                "is_active": is_active,
                "is_staff": is_staff,
                "last_name": last_name,
                "password": password,
                "url": url,
                "username": username,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def users_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/users/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def users_bulk_partial_update(
        self,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[User]:
        """


        Parameters
        ----------
        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/users/",
            method="PATCH",
            json={
                "date_joined": date_joined,
                "display": display,
                "email": email,
                "first_name": first_name,
                "groups": groups,
                "id": id,
                "is_active": is_active,
                "is_staff": is_staff,
                "last_name": last_name,
                "password": password,
                "url": url,
                "username": username,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def users_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/users/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def users_update(
        self,
        id_: int,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[User]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this user.

        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/users/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "date_joined": date_joined,
                "display": display,
                "email": email,
                "first_name": first_name,
                "groups": groups,
                "id": id,
                "is_active": is_active,
                "is_staff": is_staff,
                "last_name": last_name,
                "password": password,
                "url": url,
                "username": username,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def users_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/users/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def users_partial_update(
        self,
        id_: int,
        *,
        password: str,
        username: str,
        date_joined: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_staff: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[User]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this user.

        password : str

        username : str
            Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

        date_joined : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        email : typing.Optional[str]

        first_name : typing.Optional[str]

        groups : typing.Optional[typing.Sequence[int]]
            The groups this user belongs to. A user will get all permissions granted to each of their groups.

        id : typing.Optional[int]

        is_active : typing.Optional[bool]
            Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        is_staff : typing.Optional[bool]
            Designates whether the user can log into this admin site.

        last_name : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/users/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "date_joined": date_joined,
                "display": display,
                "email": email,
                "first_name": first_name,
                "groups": groups,
                "id": id,
                "is_active": is_active,
                "is_staff": is_staff,
                "last_name": last_name,
                "password": password,
                "url": url,
                "username": username,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
