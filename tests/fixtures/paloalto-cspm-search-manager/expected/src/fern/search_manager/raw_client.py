

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..types.saved_recent_search import SavedRecentSearch
from ..types.search_model import SearchModel
from ..types.search_model_cloud_type import SearchModelCloudType
from ..types.search_model_search_type import SearchModelSearchType
from ..types.search_model_time_range import SearchModelTimeRange
from ..types.search_response_model_search_model import SearchResponseModelSearchModel
from ..types.ui_filter_model import UiFilterModel
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSearchManagerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_history(
        self,
        *,
        filter: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[SavedRecentSearch]]:
        """
        Lists saved or recent search queries based on your filter.

        Parameters
        ----------
        filter : str
            Available values: recent, saved

        limit : typing.Optional[int]
            Maximum number of searches to be returned. A single API call retrieves a maximum of 1000 searches, which is also the default. Setting the limit to -1 will also return the default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SavedRecentSearch]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "search/history",
            method="GET",
            params={
                "filter": filter,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SavedRecentSearch],
                    parse_obj_as(
                        type_=typing.List[SavedRecentSearch],
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

    def search_history_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SearchModel]:
        """
        Returns a search query. You can access only queries that are either saved or recent searches.

        Parameters
        ----------
        id : str
            Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchModel]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"search/history/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchModel,
                    parse_obj_as(
                        type_=SearchModel,
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

    def search_history_manage(
        self,
        id_: str,
        *,
        query: str,
        time_range: SearchModelTimeRange,
        alert_id: typing.Optional[str] = OMIT,
        async_: typing.Optional[bool] = OMIT,
        async_result_url: typing.Optional[str] = OMIT,
        cloud_type: typing.Optional[SearchModelCloudType] = OMIT,
        cursor: typing.Optional[int] = OMIT,
        default: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        saved: typing.Optional[bool] = OMIT,
        search_type: typing.Optional[SearchModelSearchType] = OMIT,
        time_granularity: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchResponseModelSearchModel]:
        """
        Allows you to manage a search query (save a search query to the **Saved Searches** list under the specified ID, convert a recent search to a saved search, update an existing search). For details on how to manage a saved search, see [Manage Saved Search](/prisma-cloud/docs/cspm/manage-saved-search)

        Required parameters include the search ID, the RQL query, the flag that
        marks this search as saved, and a unique name for the saved search. A best
        practice is to copy data from the results of a search history, update the
        data as necessary, and set the **saved** parameter to **true**.

        This API requires Prisma Cloud system administrator role access if you don't own the search with the given search ID.

        Parameters
        ----------
        id_ : str
            Search ID

        query : str
            RQL Query

        time_range : SearchModelTimeRange
            Time Range

        alert_id : typing.Optional[str]
            Alert ID

        async_ : typing.Optional[bool]
            true = Is Async

        async_result_url : typing.Optional[str]
            Async Result Url

        cloud_type : typing.Optional[SearchModelCloudType]
            Cloud Type

        cursor : typing.Optional[int]
            Cursor

        default : typing.Optional[bool]

        description : typing.Optional[str]
            Search Description

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            View Order

        group_by : typing.Optional[typing.Sequence[str]]
            Group By

        id : typing.Optional[str]
            Search ID

        name : typing.Optional[str]
            Search Name

        read_only : typing.Optional[bool]
            Read Only

        saved : typing.Optional[bool]
            Search Exists

        search_type : typing.Optional[SearchModelSearchType]
            Search Type

        time_granularity : typing.Optional[str]
            Time Granularity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchResponseModelSearchModel]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"search/history/{encode_path_param(id_)}",
            method="POST",
            json={
                "alertId": alert_id,
                "async": async_,
                "asyncResultUrl": async_result_url,
                "cloudType": cloud_type,
                "cursor": cursor,
                "default": default,
                "description": description,
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=typing.Sequence[UiFilterModel], direction="write"
                ),
                "groupBy": group_by,
                "id": id,
                "name": name,
                "query": query,
                "readOnly": read_only,
                "saved": saved,
                "searchType": search_type,
                "timeGranularity": time_granularity,
                "timeRange": convert_and_respect_annotation_metadata(
                    object_=time_range, annotation=SearchModelTimeRange, direction="write"
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
                    SearchResponseModelSearchModel,
                    parse_obj_as(
                        type_=SearchResponseModelSearchModel,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def search_history_delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a saved search query.

        Parameters
        ----------
        id : str
            Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"search/history/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 409:
                raise ConflictError(
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


class AsyncRawSearchManagerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_history(
        self,
        *,
        filter: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[SavedRecentSearch]]:
        """
        Lists saved or recent search queries based on your filter.

        Parameters
        ----------
        filter : str
            Available values: recent, saved

        limit : typing.Optional[int]
            Maximum number of searches to be returned. A single API call retrieves a maximum of 1000 searches, which is also the default. Setting the limit to -1 will also return the default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SavedRecentSearch]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "search/history",
            method="GET",
            params={
                "filter": filter,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SavedRecentSearch],
                    parse_obj_as(
                        type_=typing.List[SavedRecentSearch],
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

    async def search_history_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SearchModel]:
        """
        Returns a search query. You can access only queries that are either saved or recent searches.

        Parameters
        ----------
        id : str
            Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchModel]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"search/history/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchModel,
                    parse_obj_as(
                        type_=SearchModel,
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

    async def search_history_manage(
        self,
        id_: str,
        *,
        query: str,
        time_range: SearchModelTimeRange,
        alert_id: typing.Optional[str] = OMIT,
        async_: typing.Optional[bool] = OMIT,
        async_result_url: typing.Optional[str] = OMIT,
        cloud_type: typing.Optional[SearchModelCloudType] = OMIT,
        cursor: typing.Optional[int] = OMIT,
        default: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        saved: typing.Optional[bool] = OMIT,
        search_type: typing.Optional[SearchModelSearchType] = OMIT,
        time_granularity: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchResponseModelSearchModel]:
        """
        Allows you to manage a search query (save a search query to the **Saved Searches** list under the specified ID, convert a recent search to a saved search, update an existing search). For details on how to manage a saved search, see [Manage Saved Search](/prisma-cloud/docs/cspm/manage-saved-search)

        Required parameters include the search ID, the RQL query, the flag that
        marks this search as saved, and a unique name for the saved search. A best
        practice is to copy data from the results of a search history, update the
        data as necessary, and set the **saved** parameter to **true**.

        This API requires Prisma Cloud system administrator role access if you don't own the search with the given search ID.

        Parameters
        ----------
        id_ : str
            Search ID

        query : str
            RQL Query

        time_range : SearchModelTimeRange
            Time Range

        alert_id : typing.Optional[str]
            Alert ID

        async_ : typing.Optional[bool]
            true = Is Async

        async_result_url : typing.Optional[str]
            Async Result Url

        cloud_type : typing.Optional[SearchModelCloudType]
            Cloud Type

        cursor : typing.Optional[int]
            Cursor

        default : typing.Optional[bool]

        description : typing.Optional[str]
            Search Description

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            View Order

        group_by : typing.Optional[typing.Sequence[str]]
            Group By

        id : typing.Optional[str]
            Search ID

        name : typing.Optional[str]
            Search Name

        read_only : typing.Optional[bool]
            Read Only

        saved : typing.Optional[bool]
            Search Exists

        search_type : typing.Optional[SearchModelSearchType]
            Search Type

        time_granularity : typing.Optional[str]
            Time Granularity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchResponseModelSearchModel]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"search/history/{encode_path_param(id_)}",
            method="POST",
            json={
                "alertId": alert_id,
                "async": async_,
                "asyncResultUrl": async_result_url,
                "cloudType": cloud_type,
                "cursor": cursor,
                "default": default,
                "description": description,
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=typing.Sequence[UiFilterModel], direction="write"
                ),
                "groupBy": group_by,
                "id": id,
                "name": name,
                "query": query,
                "readOnly": read_only,
                "saved": saved,
                "searchType": search_type,
                "timeGranularity": time_granularity,
                "timeRange": convert_and_respect_annotation_metadata(
                    object_=time_range, annotation=SearchModelTimeRange, direction="write"
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
                    SearchResponseModelSearchModel,
                    parse_obj_as(
                        type_=SearchResponseModelSearchModel,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def search_history_delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a saved search query.

        Parameters
        ----------
        id : str
            Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"search/history/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 409:
                raise ConflictError(
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
