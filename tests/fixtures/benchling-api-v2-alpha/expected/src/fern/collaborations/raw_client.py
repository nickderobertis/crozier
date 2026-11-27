

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.collaboration import Collaboration
from ..types.collaborations_paginated_list import CollaborationsPaginatedList
from .types.list_collaborations_request_item_type import ListCollaborationsRequestItemType
from .types.list_collaborations_request_role import ListCollaborationsRequestRole
from .types.list_collaborations_request_sort import ListCollaborationsRequestSort
from pydantic import ValidationError


class RawCollaborationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_collaborations(
        self,
        *,
        item_ids: typing.Optional[str] = None,
        item_type: typing.Optional[ListCollaborationsRequestItemType] = None,
        user_id: typing.Optional[str] = None,
        app_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        role: typing.Optional[ListCollaborationsRequestRole] = None,
        ids: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListCollaborationsRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CollaborationsPaginatedList]:
        """
        List all collaborations. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Collaborations).

        Parameters
        ----------
        item_ids : typing.Optional[str]
            Comma-separated list of ids of items for which to retrieve collaborations.

        item_type : typing.Optional[ListCollaborationsRequestItemType]
            Type of item for which to retrieve collaborations.

        user_id : typing.Optional[str]
            ID of user for which to retrieve collaborations.

        app_id : typing.Optional[str]
            ID of app for which to retrieve collaborations.

        team_id : typing.Optional[str]
            ID of team for which to retrieve collaborations.

        organization_id : typing.Optional[str]
            ID of organization for which to retrieve collaborations.

        role : typing.Optional[ListCollaborationsRequestRole]
            Organization or team membership role for which to retrieve collaborations.

        ids : typing.Optional[str]
            Comma-separated list of collaboration ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        created_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.

        created_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.

        modified_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.

        modified_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.

        modified_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.

        modified_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.

        page_size : typing.Optional[int]
            Number of collaborations to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListCollaborationsRequestSort]
            Method by which to order search results. Valid sort method is modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order. Default is modifiedAt:desc.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CollaborationsPaginatedList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "collaborations",
            method="GET",
            params={
                "itemIds": item_ids,
                "itemType": item_type,
                "userId": user_id,
                "appId": app_id,
                "teamId": team_id,
                "organizationId": organization_id,
                "role": role,
                "ids": ids,
                "createdAt.lt": created_at_lt,
                "createdAt.gt": created_at_gt,
                "modifiedAt.lt": modified_at_lt,
                "modifiedAt.gt": modified_at_gt,
                "modifiedAt.lte": modified_at_lte,
                "modifiedAt.gte": modified_at_gte,
                "pageSize": page_size,
                "nextToken": next_token,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CollaborationsPaginatedList,
                    parse_obj_as(
                        type_=CollaborationsPaginatedList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_collaboration(
        self, collaboration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Collaboration]:
        """
        Get a collaboration by ID. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Collaborations).

        Parameters
        ----------
        collaboration_id : str
            ID of collaboration to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Collaboration]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"collaborations/{encode_path_param(collaboration_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collaboration,
                    parse_obj_as(
                        type_=Collaboration,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawCollaborationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_collaborations(
        self,
        *,
        item_ids: typing.Optional[str] = None,
        item_type: typing.Optional[ListCollaborationsRequestItemType] = None,
        user_id: typing.Optional[str] = None,
        app_id: typing.Optional[str] = None,
        team_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        role: typing.Optional[ListCollaborationsRequestRole] = None,
        ids: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListCollaborationsRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CollaborationsPaginatedList]:
        """
        List all collaborations. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Collaborations).

        Parameters
        ----------
        item_ids : typing.Optional[str]
            Comma-separated list of ids of items for which to retrieve collaborations.

        item_type : typing.Optional[ListCollaborationsRequestItemType]
            Type of item for which to retrieve collaborations.

        user_id : typing.Optional[str]
            ID of user for which to retrieve collaborations.

        app_id : typing.Optional[str]
            ID of app for which to retrieve collaborations.

        team_id : typing.Optional[str]
            ID of team for which to retrieve collaborations.

        organization_id : typing.Optional[str]
            ID of organization for which to retrieve collaborations.

        role : typing.Optional[ListCollaborationsRequestRole]
            Organization or team membership role for which to retrieve collaborations.

        ids : typing.Optional[str]
            Comma-separated list of collaboration ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        created_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.

        created_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.

        modified_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.

        modified_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.

        modified_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.

        modified_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.

        page_size : typing.Optional[int]
            Number of collaborations to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListCollaborationsRequestSort]
            Method by which to order search results. Valid sort method is modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order. Default is modifiedAt:desc.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CollaborationsPaginatedList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "collaborations",
            method="GET",
            params={
                "itemIds": item_ids,
                "itemType": item_type,
                "userId": user_id,
                "appId": app_id,
                "teamId": team_id,
                "organizationId": organization_id,
                "role": role,
                "ids": ids,
                "createdAt.lt": created_at_lt,
                "createdAt.gt": created_at_gt,
                "modifiedAt.lt": modified_at_lt,
                "modifiedAt.gt": modified_at_gt,
                "modifiedAt.lte": modified_at_lte,
                "modifiedAt.gte": modified_at_gte,
                "pageSize": page_size,
                "nextToken": next_token,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CollaborationsPaginatedList,
                    parse_obj_as(
                        type_=CollaborationsPaginatedList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_collaboration(
        self, collaboration_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Collaboration]:
        """
        Get a collaboration by ID. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Collaborations).

        Parameters
        ----------
        collaboration_id : str
            ID of collaboration to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Collaboration]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"collaborations/{encode_path_param(collaboration_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collaboration,
                    parse_obj_as(
                        type_=Collaboration,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
