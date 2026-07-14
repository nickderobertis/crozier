

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.conflict_error import ConflictError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.error import Error
from ..types.group_id import GroupId
from ..types.group_meta_data import GroupMetaData
from ..types.group_search_results import GroupSearchResults
from ..types.properties import Properties
from ..types.sort_by import SortBy
from ..types.sort_order import SortOrder


OMIT = typing.cast(typing.Any, ...)


class RawGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_groups(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[SortOrder] = None,
        orderby: typing.Optional[SortBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupSearchResults]:
        """
        Returns a list of all groups.  This list is paged.

        Parameters
        ----------
        limit : typing.Optional[int]
            The number of groups to return.  Defaults to 20.

        offset : typing.Optional[int]
            The number of groups to skip before starting the result set.  Defaults to 0.

        order : typing.Optional[SortOrder]
            Sort order, ascending (`asc`) or descending (`desc`).

        orderby : typing.Optional[SortBy]
            The field to sort by.  Can be one of:

            * `name`
            * `createdOn`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GroupSearchResults]
            On a successful response, returns a bounded set of groups.
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "order": order,
                "orderby": orderby,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupSearchResults,
                    parse_obj_as(
                        type_=GroupSearchResults,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_group(
        self,
        *,
        id: str,
        description: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GroupMetaData]:
        """
        Creates a new group.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)
        * The group already exist (HTTP error `409`)

        Parameters
        ----------
        id : str


        description : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GroupMetaData]
            The group has been successfully created.
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups",
            method="POST",
            json={
                "description": description,
                "id": id,
                "properties": properties,
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
                    GroupMetaData,
                    parse_obj_as(
                        type_=GroupMetaData,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_group_by_id(
        self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GroupMetaData]:
        """
        Returns a group using the specified id.

        This operation can fail for the following reasons:

        * No group exists with the specified ID (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GroupMetaData]
            The group's metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupMetaData,
                    parse_obj_as(
                        type_=GroupMetaData,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_group_by_id(
        self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a group by identifier.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)
        * The group does not exist (HTTP error `404`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_groups(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[SortOrder] = None,
        orderby: typing.Optional[SortBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupSearchResults]:
        """
        Returns a list of all groups.  This list is paged.

        Parameters
        ----------
        limit : typing.Optional[int]
            The number of groups to return.  Defaults to 20.

        offset : typing.Optional[int]
            The number of groups to skip before starting the result set.  Defaults to 0.

        order : typing.Optional[SortOrder]
            Sort order, ascending (`asc`) or descending (`desc`).

        orderby : typing.Optional[SortBy]
            The field to sort by.  Can be one of:

            * `name`
            * `createdOn`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GroupSearchResults]
            On a successful response, returns a bounded set of groups.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "order": order,
                "orderby": orderby,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupSearchResults,
                    parse_obj_as(
                        type_=GroupSearchResults,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_group(
        self,
        *,
        id: str,
        description: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GroupMetaData]:
        """
        Creates a new group.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)
        * The group already exist (HTTP error `409`)

        Parameters
        ----------
        id : str


        description : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GroupMetaData]
            The group has been successfully created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups",
            method="POST",
            json={
                "description": description,
                "id": id,
                "properties": properties,
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
                    GroupMetaData,
                    parse_obj_as(
                        type_=GroupMetaData,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_group_by_id(
        self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GroupMetaData]:
        """
        Returns a group using the specified id.

        This operation can fail for the following reasons:

        * No group exists with the specified ID (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GroupMetaData]
            The group's metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupMetaData,
                    parse_obj_as(
                        type_=GroupMetaData,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_group_by_id(
        self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a group by identifier.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)
        * The group does not exist (HTTP error `404`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
