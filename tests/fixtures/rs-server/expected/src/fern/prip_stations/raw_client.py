

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.item_collection import ItemCollection
from ..types.post_fields_extension import PostFieldsExtension
from ..types.search_post_request_filter_lang import SearchPostRequestFilterLang
from ..types.search_post_request_intersects import SearchPostRequestIntersects
from ..types.sort_extension import SortExtension
from .types.get_prip_collection_items_prip_collections_collection_id_items_get_request_filter_lang import (
    GetPripCollectionItemsPripCollectionsCollectionIdItemsGetRequestFilterLang,
)
from .types.get_prip_collection_items_prip_collections_collection_id_items_get_response import (
    GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse,
)
from .types.get_prip_collection_prip_collections_collection_id_get_response import (
    GetPripCollectionPripCollectionsCollectionIdGetResponse,
)
from .types.get_prip_collection_specific_item_prip_collections_collection_id_items_item_id_get_response import (
    GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPripStationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search(
        self,
        *,
        collections: typing.Optional[typing.Sequence[str]] = OMIT,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bbox: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        intersects: typing.Optional[SearchPostRequestIntersects] = OMIT,
        datetime: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        conf: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        query: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        sortby: typing.Optional[typing.Sequence[SortExtension]] = OMIT,
        fields: typing.Optional[PostFieldsExtension] = OMIT,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        filter_crs: typing.Optional[str] = OMIT,
        filter_lang: typing.Optional[SearchPostRequestFilterLang] = OMIT,
        token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ItemCollection]:
        """
        Endpoint.

        Parameters
        ----------
        collections : typing.Optional[typing.Sequence[str]]

        ids : typing.Optional[typing.Sequence[str]]

        bbox : typing.Optional[typing.Sequence[typing.Any]]

        intersects : typing.Optional[SearchPostRequestIntersects]

        datetime : typing.Optional[str]

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (capped to 10_000).

        conf : typing.Optional[typing.Dict[str, typing.Any]]

        query : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]

        sortby : typing.Optional[typing.Sequence[SortExtension]]
            An array of property (field) names, and direction in form of '{'field': '<property_name>', 'direction':'<direction>'}'

        fields : typing.Optional[PostFieldsExtension]
            Include or exclude fields from items body.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            A CQL filter expression for filtering items.

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[SearchPostRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ItemCollection]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "prip/search",
            method="POST",
            json={
                "collections": collections,
                "ids": ids,
                "bbox": bbox,
                "intersects": convert_and_respect_annotation_metadata(
                    object_=intersects, annotation=typing.Optional[SearchPostRequestIntersects], direction="write"
                ),
                "datetime": datetime,
                "limit": limit,
                "conf": conf,
                "query": query,
                "sortby": convert_and_respect_annotation_metadata(
                    object_=sortby, annotation=typing.Optional[typing.Sequence[SortExtension]], direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Optional[PostFieldsExtension], direction="write"
                ),
                "filter": filter,
                "filter-crs": filter_crs,
                "filter-lang": filter_lang,
                "token": token,
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
                    ItemCollection,
                    parse_obj_as(
                        type_=ItemCollection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_root_catalog(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
        """
        Redirect to the landing page.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "prip",
            method="GET",
            request_options=request_options,
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

    def get_conformance(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
        """
        Return the STAC/OGC conformance classes implemented by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "prip/conformance",
            method="GET",
            request_options=request_options,
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

    def get_allowed_prip_collections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Return the PRIP collections to which the user has access to.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "prip/collections",
            method="GET",
            request_options=request_options,
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

    def get_prip_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPripCollectionPripCollectionsCollectionIdGetResponse]:
        """
        Return a specific PRIP collection.

        Parameters
        ----------
        collection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPripCollectionPripCollectionsCollectionIdGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"prip/collections/{encode_path_param(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPripCollectionPripCollectionsCollectionIdGetResponse,
                    parse_obj_as(
                        type_=GetPripCollectionPripCollectionsCollectionIdGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_prip_collection_items(
        self,
        collection_id: str,
        *,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetPripCollectionItemsPripCollectionsCollectionIdItemsGetRequestFilterLang] = None,
        sortby: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse]:
        """
        Retrieve a list of items from a specified PRIP collection.

        This endpoint returns a collection of items associated with the given PRIP
        collection ID. It utilizes the collection ID to validate access and fetches
        the items based on defined query parameters.

        Args:
            request (Request): Incoming HTTP request used for authentication and routing.
            collection_id (str): PRIP collection ID. Must be a valid collection identifier
                                 (e.g., 'ins_s1').
            bbox (BBoxType, optional): Bounding box filter as four or six numbers
                [west, south, east, north] or [west, south, minz, east, north, maxz].
                Defaults to None. If provided, items intersecting the bbox are returned.

            datetime (DateTimeType, optional): Temporal filter. Either a single RFC 3339
                timestamp/interval (e.g., "2024-01-01T00:00:00Z") or a closed/open interval
                (e.g., "2024-01-01T00:00:00Z/2024-01-31T23:59:59Z", "../2024-01-01T00:00:00Z").
                Defaults to None.

            filter_ (FilterType, optional): CQL2 filter expression (text or JSON depending
                on `filter_lang`). Defaults to None.

            filter_lang (FilterLangType, optional): CQL2 language for `filter_`. One of
                "cql2-text" or "cql2-json". Defaults to "cql2-text".

            sortby (SortByType, optional): Sort specification. Single field or list of fields
                with optional direction, e.g., {"field": "published", "direction": "desc"}.
                Defaults to None (implementation default ordering).

            limit (LimitType, optional): Page size (maximum number of items to return).
                Defaults to None (service default / configured max).

            page (PageType, optional): 1-based page index.
                Defaults to None (first page).
        Returns:
            list[dict]: A FeatureCollection of items belonging to the specified collection, or an
                        error message if the collection is not found.

        Raises:
            HTTPException: If the authentication fails, or if there are issues with the
                           collection ID provided.

        Parameters
        ----------
        collection_id : str
            Collection ID

        bbox : typing.Optional[str]
            Bounding box (geospatial footprint or extent, four or six comma-separated numbers).

        datetime : typing.Optional[str]
            Time interval e.g "2024-01-01T00:00:00Z/2024-01-02T23:59:59Z"

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.html

        filter_lang : typing.Optional[GetPripCollectionItemsPripCollectionsCollectionIdItemsGetRequestFilterLang]
            The CQL2 filter encoding that the 'filter' value uses.

        sortby : typing.Optional[str]
            Sort by +/-fieldName (ascending/descending)

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (between 1000 and 10_000)

        page : typing.Optional[str]
            Page number to be displayed, defaults to first one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"prip/collections/{encode_path_param(collection_id)}/items",
            method="GET",
            params={
                "bbox": bbox,
                "datetime": datetime,
                "filter": filter,
                "filter-lang": filter_lang,
                "sortby": sortby,
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse,
                    parse_obj_as(
                        type_=GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_prip_collection_specific_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse]:
        """
        Retrieve a specific item from a specified PRIP collection.

        This endpoint fetches details of a specific item within the given PRIP collection
        by its unique item ID. It utilizes the provided collection ID and item ID to
        validate access and return item information.

        Args:
            request (Request): Incoming HTTP request used for authentication and routing.
            collection_id (str): PRIP collection ID. Must be a valid collection identifier (e.g., 'ins_s1').
            item_id (str): PRIP item ID. Must be a valid item identifier.

        Returns:
        - dict: A JSON object containing details of the specified item, or an error
                message if the item is not found.

        Raises:
        - HTTPException: If the authentication fails, or if the specified item is
                        not found in the collection.

        Example:
        A successful response will return:

            {
                "id": "S1A_OPER_MPL_ORBPRE_20210214T021411_20210221T021411_0001.EOF",
                "type": "Feature",
                "properties": {
                    ...  # Detailed properties of the item
                },
                "geometry": {
                    ...  # Geometry details of the item
                },
                "links": [
                    ...  # Links associated with the item
                ]
            }

        Parameters
        ----------
        collection_id : str
            E.G.

        item_id : str
            E.G. S1A_OPER_MPL_ORBPRE_20210214T021411_20210221T021411_0001.EOF

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"prip/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse,
                    parse_obj_as(
                        type_=GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawPripStationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search(
        self,
        *,
        collections: typing.Optional[typing.Sequence[str]] = OMIT,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bbox: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        intersects: typing.Optional[SearchPostRequestIntersects] = OMIT,
        datetime: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        conf: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        query: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        sortby: typing.Optional[typing.Sequence[SortExtension]] = OMIT,
        fields: typing.Optional[PostFieldsExtension] = OMIT,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        filter_crs: typing.Optional[str] = OMIT,
        filter_lang: typing.Optional[SearchPostRequestFilterLang] = OMIT,
        token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ItemCollection]:
        """
        Endpoint.

        Parameters
        ----------
        collections : typing.Optional[typing.Sequence[str]]

        ids : typing.Optional[typing.Sequence[str]]

        bbox : typing.Optional[typing.Sequence[typing.Any]]

        intersects : typing.Optional[SearchPostRequestIntersects]

        datetime : typing.Optional[str]

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (capped to 10_000).

        conf : typing.Optional[typing.Dict[str, typing.Any]]

        query : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]

        sortby : typing.Optional[typing.Sequence[SortExtension]]
            An array of property (field) names, and direction in form of '{'field': '<property_name>', 'direction':'<direction>'}'

        fields : typing.Optional[PostFieldsExtension]
            Include or exclude fields from items body.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            A CQL filter expression for filtering items.

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[SearchPostRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ItemCollection]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "prip/search",
            method="POST",
            json={
                "collections": collections,
                "ids": ids,
                "bbox": bbox,
                "intersects": convert_and_respect_annotation_metadata(
                    object_=intersects, annotation=typing.Optional[SearchPostRequestIntersects], direction="write"
                ),
                "datetime": datetime,
                "limit": limit,
                "conf": conf,
                "query": query,
                "sortby": convert_and_respect_annotation_metadata(
                    object_=sortby, annotation=typing.Optional[typing.Sequence[SortExtension]], direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Optional[PostFieldsExtension], direction="write"
                ),
                "filter": filter,
                "filter-crs": filter_crs,
                "filter-lang": filter_lang,
                "token": token,
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
                    ItemCollection,
                    parse_obj_as(
                        type_=ItemCollection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_root_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Redirect to the landing page.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "prip",
            method="GET",
            request_options=request_options,
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

    async def get_conformance(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Return the STAC/OGC conformance classes implemented by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "prip/conformance",
            method="GET",
            request_options=request_options,
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

    async def get_allowed_prip_collections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Return the PRIP collections to which the user has access to.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "prip/collections",
            method="GET",
            request_options=request_options,
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

    async def get_prip_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPripCollectionPripCollectionsCollectionIdGetResponse]:
        """
        Return a specific PRIP collection.

        Parameters
        ----------
        collection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPripCollectionPripCollectionsCollectionIdGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"prip/collections/{encode_path_param(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPripCollectionPripCollectionsCollectionIdGetResponse,
                    parse_obj_as(
                        type_=GetPripCollectionPripCollectionsCollectionIdGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_prip_collection_items(
        self,
        collection_id: str,
        *,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetPripCollectionItemsPripCollectionsCollectionIdItemsGetRequestFilterLang] = None,
        sortby: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse]:
        """
        Retrieve a list of items from a specified PRIP collection.

        This endpoint returns a collection of items associated with the given PRIP
        collection ID. It utilizes the collection ID to validate access and fetches
        the items based on defined query parameters.

        Args:
            request (Request): Incoming HTTP request used for authentication and routing.
            collection_id (str): PRIP collection ID. Must be a valid collection identifier
                                 (e.g., 'ins_s1').
            bbox (BBoxType, optional): Bounding box filter as four or six numbers
                [west, south, east, north] or [west, south, minz, east, north, maxz].
                Defaults to None. If provided, items intersecting the bbox are returned.

            datetime (DateTimeType, optional): Temporal filter. Either a single RFC 3339
                timestamp/interval (e.g., "2024-01-01T00:00:00Z") or a closed/open interval
                (e.g., "2024-01-01T00:00:00Z/2024-01-31T23:59:59Z", "../2024-01-01T00:00:00Z").
                Defaults to None.

            filter_ (FilterType, optional): CQL2 filter expression (text or JSON depending
                on `filter_lang`). Defaults to None.

            filter_lang (FilterLangType, optional): CQL2 language for `filter_`. One of
                "cql2-text" or "cql2-json". Defaults to "cql2-text".

            sortby (SortByType, optional): Sort specification. Single field or list of fields
                with optional direction, e.g., {"field": "published", "direction": "desc"}.
                Defaults to None (implementation default ordering).

            limit (LimitType, optional): Page size (maximum number of items to return).
                Defaults to None (service default / configured max).

            page (PageType, optional): 1-based page index.
                Defaults to None (first page).
        Returns:
            list[dict]: A FeatureCollection of items belonging to the specified collection, or an
                        error message if the collection is not found.

        Raises:
            HTTPException: If the authentication fails, or if there are issues with the
                           collection ID provided.

        Parameters
        ----------
        collection_id : str
            Collection ID

        bbox : typing.Optional[str]
            Bounding box (geospatial footprint or extent, four or six comma-separated numbers).

        datetime : typing.Optional[str]
            Time interval e.g "2024-01-01T00:00:00Z/2024-01-02T23:59:59Z"

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.html

        filter_lang : typing.Optional[GetPripCollectionItemsPripCollectionsCollectionIdItemsGetRequestFilterLang]
            The CQL2 filter encoding that the 'filter' value uses.

        sortby : typing.Optional[str]
            Sort by +/-fieldName (ascending/descending)

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (between 1000 and 10_000)

        page : typing.Optional[str]
            Page number to be displayed, defaults to first one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"prip/collections/{encode_path_param(collection_id)}/items",
            method="GET",
            params={
                "bbox": bbox,
                "datetime": datetime,
                "filter": filter,
                "filter-lang": filter_lang,
                "sortby": sortby,
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse,
                    parse_obj_as(
                        type_=GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_prip_collection_specific_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse]:
        """
        Retrieve a specific item from a specified PRIP collection.

        This endpoint fetches details of a specific item within the given PRIP collection
        by its unique item ID. It utilizes the provided collection ID and item ID to
        validate access and return item information.

        Args:
            request (Request): Incoming HTTP request used for authentication and routing.
            collection_id (str): PRIP collection ID. Must be a valid collection identifier (e.g., 'ins_s1').
            item_id (str): PRIP item ID. Must be a valid item identifier.

        Returns:
        - dict: A JSON object containing details of the specified item, or an error
                message if the item is not found.

        Raises:
        - HTTPException: If the authentication fails, or if the specified item is
                        not found in the collection.

        Example:
        A successful response will return:

            {
                "id": "S1A_OPER_MPL_ORBPRE_20210214T021411_20210221T021411_0001.EOF",
                "type": "Feature",
                "properties": {
                    ...  # Detailed properties of the item
                },
                "geometry": {
                    ...  # Geometry details of the item
                },
                "links": [
                    ...  # Links associated with the item
                ]
            }

        Parameters
        ----------
        collection_id : str
            E.G.

        item_id : str
            E.G. S1A_OPER_MPL_ORBPRE_20210214T021411_20210221T021411_0001.EOF

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"prip/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse,
                    parse_obj_as(
                        type_=GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
