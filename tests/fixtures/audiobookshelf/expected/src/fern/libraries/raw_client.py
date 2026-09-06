

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
from ..errors.not_found_error import NotFoundError
from ..types.library import Library
from ..types.library_display_order import LibraryDisplayOrder
from ..types.library_folders import LibraryFolders
from ..types.library_icon import LibraryIcon
from ..types.library_id import LibraryId
from ..types.library_media_type import LibraryMediaType
from ..types.library_name import LibraryName
from ..types.library_provider import LibraryProvider
from ..types.library_settings import LibrarySettings
from ..types.series_id import SeriesId
from ..types.series_with_progress_and_rss import SeriesWithProgressAndRss
from .types.get_libraries_response import GetLibrariesResponse
from .types.get_library_authors_response import GetLibraryAuthorsResponse
from .types.get_library_items_response import GetLibraryItemsResponse
from .types.get_library_series_by_id_request_sort import GetLibrarySeriesByIdRequestSort
from .types.get_library_series_request_sort import GetLibrarySeriesRequestSort
from .types.get_library_series_response import GetLibrarySeriesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLibrariesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_libraries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetLibrariesResponse]:
        """
        Get all libraries on server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLibrariesResponse]
            getLibraries OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/libraries",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLibrariesResponse,
                    parse_obj_as(
                        type_=GetLibrariesResponse,
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

    def create_library(
        self,
        *,
        name: LibraryName,
        folders: LibraryFolders,
        display_order: typing.Optional[LibraryDisplayOrder] = OMIT,
        icon: typing.Optional[LibraryIcon] = OMIT,
        media_type: typing.Optional[LibraryMediaType] = OMIT,
        provider: typing.Optional[LibraryProvider] = OMIT,
        settings: typing.Optional[LibrarySettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Library]:
        """
        Create a new library on server.

        Parameters
        ----------
        name : LibraryName

        folders : LibraryFolders

        display_order : typing.Optional[LibraryDisplayOrder]

        icon : typing.Optional[LibraryIcon]

        media_type : typing.Optional[LibraryMediaType]

        provider : typing.Optional[LibraryProvider]

        settings : typing.Optional[LibrarySettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Library]
            Library found.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/libraries",
            method="POST",
            json={
                "name": name,
                "folders": convert_and_respect_annotation_metadata(
                    object_=folders, annotation=LibraryFolders, direction="write"
                ),
                "displayOrder": display_order,
                "icon": icon,
                "mediaType": media_type,
                "provider": provider,
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=LibrarySettings, direction="write"
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
                    Library,
                    parse_obj_as(
                        type_=Library,
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

    def get_library_by_id(
        self,
        id: LibraryId,
        *,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Library]:
        """
        Get a single library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        include : typing.Optional[str]

        minified : typing.Optional[int]
            Return minified items if true

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Library]
            Library found.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}",
            method="GET",
            params={
                "include": include,
                "minified": minified,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Library,
                    parse_obj_as(
                        type_=Library,
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

    def delete_library_by_id(
        self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Library]:
        """
        Delete a single library by ID on server and return the deleted object.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Library]
            Library found.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Library,
                    parse_obj_as(
                        type_=Library,
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

    def update_library_by_id(
        self,
        id: LibraryId,
        *,
        name: typing.Optional[LibraryName] = OMIT,
        folders: typing.Optional[LibraryFolders] = OMIT,
        display_order: typing.Optional[LibraryDisplayOrder] = OMIT,
        icon: typing.Optional[LibraryIcon] = OMIT,
        media_type: typing.Optional[LibraryMediaType] = OMIT,
        provider: typing.Optional[LibraryProvider] = OMIT,
        settings: typing.Optional[LibrarySettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Library]:
        """
        Update a single library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        name : typing.Optional[LibraryName]

        folders : typing.Optional[LibraryFolders]

        display_order : typing.Optional[LibraryDisplayOrder]

        icon : typing.Optional[LibraryIcon]

        media_type : typing.Optional[LibraryMediaType]

        provider : typing.Optional[LibraryProvider]

        settings : typing.Optional[LibrarySettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Library]
            Library found.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}",
            method="PATCH",
            json={
                "name": name,
                "folders": convert_and_respect_annotation_metadata(
                    object_=folders, annotation=LibraryFolders, direction="write"
                ),
                "displayOrder": display_order,
                "icon": icon,
                "mediaType": media_type,
                "provider": provider,
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=LibrarySettings, direction="write"
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
                    Library,
                    parse_obj_as(
                        type_=Library,
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

    def get_library_authors(
        self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetLibraryAuthorsResponse]:
        """
        Get all authors in a library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLibraryAuthorsResponse]
            getLibraryAuthors OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}/authors",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLibraryAuthorsResponse,
                    parse_obj_as(
                        type_=GetLibraryAuthorsResponse,
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

    def get_library_items(
        self,
        id: LibraryId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        collapse_series: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLibraryItemsResponse]:
        """
        Get items in a library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[str]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        minified : typing.Optional[int]
            Return minified items if true

        collapse_series : typing.Optional[int]
            Whether to collapse series into a single cover

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLibraryItemsResponse]
            getLibraryItems OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}/items",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "sort": sort,
                "desc": desc,
                "filter": filter,
                "include": include,
                "minified": minified,
                "collapseSeries": collapse_series,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLibraryItemsResponse,
                    parse_obj_as(
                        type_=GetLibraryItemsResponse,
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

    def delete_library_issues(
        self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Delete all items with issues in a library by library ID on the server. This only removes the items from the ABS database and does not delete media files.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            deleteLibraryIssues OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}/issues",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def get_library_series(
        self,
        id: LibraryId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[GetLibrarySeriesRequestSort] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLibrarySeriesResponse]:
        """
        Get series in a library. Filtering and sorting can be applied.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[GetLibrarySeriesRequestSort]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        minified : typing.Optional[int]
            Return minified items if true

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLibrarySeriesResponse]
            getLibrarySeries OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}/series",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "sort": sort,
                "desc": desc,
                "filter": filter,
                "include": include,
                "minified": minified,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLibrarySeriesResponse,
                    parse_obj_as(
                        type_=GetLibrarySeriesResponse,
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

    def get_library_series_by_id(
        self,
        id: LibraryId,
        series_id: SeriesId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[GetLibrarySeriesByIdRequestSort] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SeriesWithProgressAndRss]:
        """
        Get a single series in a library by ID on server. This endpoint is deprecated and `/api/series/{id}` should be used instead.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        series_id : SeriesId
            The ID of the series.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[GetLibrarySeriesByIdRequestSort]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        minified : typing.Optional[int]
            Return minified items if true

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeriesWithProgressAndRss]
            getLibrarySeriesById OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}/series/{encode_path_param(series_id)}",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "sort": sort,
                "desc": desc,
                "filter": filter,
                "minified": minified,
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeriesWithProgressAndRss,
                    parse_obj_as(
                        type_=SeriesWithProgressAndRss,
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


class AsyncRawLibrariesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_libraries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetLibrariesResponse]:
        """
        Get all libraries on server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLibrariesResponse]
            getLibraries OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/libraries",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLibrariesResponse,
                    parse_obj_as(
                        type_=GetLibrariesResponse,
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

    async def create_library(
        self,
        *,
        name: LibraryName,
        folders: LibraryFolders,
        display_order: typing.Optional[LibraryDisplayOrder] = OMIT,
        icon: typing.Optional[LibraryIcon] = OMIT,
        media_type: typing.Optional[LibraryMediaType] = OMIT,
        provider: typing.Optional[LibraryProvider] = OMIT,
        settings: typing.Optional[LibrarySettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Library]:
        """
        Create a new library on server.

        Parameters
        ----------
        name : LibraryName

        folders : LibraryFolders

        display_order : typing.Optional[LibraryDisplayOrder]

        icon : typing.Optional[LibraryIcon]

        media_type : typing.Optional[LibraryMediaType]

        provider : typing.Optional[LibraryProvider]

        settings : typing.Optional[LibrarySettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Library]
            Library found.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/libraries",
            method="POST",
            json={
                "name": name,
                "folders": convert_and_respect_annotation_metadata(
                    object_=folders, annotation=LibraryFolders, direction="write"
                ),
                "displayOrder": display_order,
                "icon": icon,
                "mediaType": media_type,
                "provider": provider,
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=LibrarySettings, direction="write"
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
                    Library,
                    parse_obj_as(
                        type_=Library,
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

    async def get_library_by_id(
        self,
        id: LibraryId,
        *,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Library]:
        """
        Get a single library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        include : typing.Optional[str]

        minified : typing.Optional[int]
            Return minified items if true

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Library]
            Library found.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}",
            method="GET",
            params={
                "include": include,
                "minified": minified,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Library,
                    parse_obj_as(
                        type_=Library,
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

    async def delete_library_by_id(
        self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Library]:
        """
        Delete a single library by ID on server and return the deleted object.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Library]
            Library found.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Library,
                    parse_obj_as(
                        type_=Library,
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

    async def update_library_by_id(
        self,
        id: LibraryId,
        *,
        name: typing.Optional[LibraryName] = OMIT,
        folders: typing.Optional[LibraryFolders] = OMIT,
        display_order: typing.Optional[LibraryDisplayOrder] = OMIT,
        icon: typing.Optional[LibraryIcon] = OMIT,
        media_type: typing.Optional[LibraryMediaType] = OMIT,
        provider: typing.Optional[LibraryProvider] = OMIT,
        settings: typing.Optional[LibrarySettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Library]:
        """
        Update a single library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        name : typing.Optional[LibraryName]

        folders : typing.Optional[LibraryFolders]

        display_order : typing.Optional[LibraryDisplayOrder]

        icon : typing.Optional[LibraryIcon]

        media_type : typing.Optional[LibraryMediaType]

        provider : typing.Optional[LibraryProvider]

        settings : typing.Optional[LibrarySettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Library]
            Library found.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}",
            method="PATCH",
            json={
                "name": name,
                "folders": convert_and_respect_annotation_metadata(
                    object_=folders, annotation=LibraryFolders, direction="write"
                ),
                "displayOrder": display_order,
                "icon": icon,
                "mediaType": media_type,
                "provider": provider,
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=LibrarySettings, direction="write"
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
                    Library,
                    parse_obj_as(
                        type_=Library,
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

    async def get_library_authors(
        self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetLibraryAuthorsResponse]:
        """
        Get all authors in a library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLibraryAuthorsResponse]
            getLibraryAuthors OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}/authors",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLibraryAuthorsResponse,
                    parse_obj_as(
                        type_=GetLibraryAuthorsResponse,
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

    async def get_library_items(
        self,
        id: LibraryId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        collapse_series: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetLibraryItemsResponse]:
        """
        Get items in a library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[str]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        minified : typing.Optional[int]
            Return minified items if true

        collapse_series : typing.Optional[int]
            Whether to collapse series into a single cover

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLibraryItemsResponse]
            getLibraryItems OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}/items",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "sort": sort,
                "desc": desc,
                "filter": filter,
                "include": include,
                "minified": minified,
                "collapseSeries": collapse_series,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLibraryItemsResponse,
                    parse_obj_as(
                        type_=GetLibraryItemsResponse,
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

    async def delete_library_issues(
        self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Delete all items with issues in a library by library ID on the server. This only removes the items from the ABS database and does not delete media files.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            deleteLibraryIssues OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}/issues",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def get_library_series(
        self,
        id: LibraryId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[GetLibrarySeriesRequestSort] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetLibrarySeriesResponse]:
        """
        Get series in a library. Filtering and sorting can be applied.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[GetLibrarySeriesRequestSort]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        minified : typing.Optional[int]
            Return minified items if true

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLibrarySeriesResponse]
            getLibrarySeries OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}/series",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "sort": sort,
                "desc": desc,
                "filter": filter,
                "include": include,
                "minified": minified,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLibrarySeriesResponse,
                    parse_obj_as(
                        type_=GetLibrarySeriesResponse,
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

    async def get_library_series_by_id(
        self,
        id: LibraryId,
        series_id: SeriesId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[GetLibrarySeriesByIdRequestSort] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SeriesWithProgressAndRss]:
        """
        Get a single series in a library by ID on server. This endpoint is deprecated and `/api/series/{id}` should be used instead.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        series_id : SeriesId
            The ID of the series.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[GetLibrarySeriesByIdRequestSort]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        minified : typing.Optional[int]
            Return minified items if true

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeriesWithProgressAndRss]
            getLibrarySeriesById OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/libraries/{encode_path_param(id)}/series/{encode_path_param(series_id)}",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "sort": sort,
                "desc": desc,
                "filter": filter,
                "minified": minified,
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeriesWithProgressAndRss,
                    parse_obj_as(
                        type_=SeriesWithProgressAndRss,
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
