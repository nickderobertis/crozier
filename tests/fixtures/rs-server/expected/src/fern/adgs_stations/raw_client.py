

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
from .types.get_adgs_collection_auxip_collections_collection_id_get_response import (
    GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse,
)
from .types.get_adgs_collection_items_auxip_collections_collection_id_items_get_request_filter_lang import (
    GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang,
)
from .types.get_adgs_collection_items_auxip_collections_collection_id_items_get_response import (
    GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse,
)
from .types.get_adgs_collection_specific_item_auxip_collections_collection_id_items_item_id_get_response import (
    GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAdgsStationsClient:
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
            "auxip/search",
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
        Retrieve the RSPY ADGS Search catalog landing page.

        This endpoint generates a STAC (SpatioTemporal Asset Catalog) Catalog object that serves as the landing
        page for the RSPY ADGS service. The catalog includes basic metadata about the service and links to
        available collections.

        The resulting catalog contains:
        - `id`: A unique identifier for the catalog, generated as a UUID.
        - `description`: A brief description of the catalog.
        - `title`: The title of the catalog.
        - `stac_version`: The version of the STAC specification to which the catalog conforms.
        - `conformsTo`: A list of STAC and OGC API specifications that the catalog conforms to.
        - `links`: A link to the `/adgs/collections` endpoint where users can find available collections.

        The `stac_version` is set to "1.1.0", and the `conformsTo` field lists the relevant STAC and OGC API
        specifications that the catalog adheres to. A link to the collections endpoint is added to the catalog's
        `links` field, allowing users to discover available collections in the ADGS service.

        Parameters:
        - request: The HTTP request object which includes details about the incoming request.

        Returns:
        - dict: A dictionary representation of the STAC catalog, including metadata and links.

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
            "auxip",
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
            "auxip/conformance",
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

    def get_allowed_adgs_collections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Return the ADGS collections to which the user has access to.

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
            "auxip/collections",
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

    def get_adgs_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse]:
        """
        Return a specific ADGS collection.

        Parameters
        ----------
        collection_id : str
            E.G.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"auxip/collections/{encode_path_param(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse,
                    parse_obj_as(
                        type_=GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse,
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

    def get_adgs_collection_items(
        self,
        collection_id: str,
        *,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_lang: typing.Optional[
            GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang
        ] = None,
        sortby: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse]:
        """
        Retrieve a list of items from a specified AUXIP collection.

        This endpoint returns a collection of items associated with the given AUXIP
        collection ID. It utilizes the collection ID to validate access and fetches
        the items based on defined query parameters.

        Args:
            request (Request): The incoming HTTP request used for authentication and routing.
            collection_id (str): AUXIP collection ID. Must be a valid collection identifier
                                 (e.g., 'ins_s1').
            bbox (BBoxType): Bounding box spatial filter, as [west, south, east, north] coordinates.
            datetime (DateTimeType): Temporal filter as an RFC 3339 timestamp or interval.
            filter_ (FilterType): CQL2 filter expression to further restrict results.
            filter_lang (FilterLangType): Language for the CQL2 filter, either "cql2-text" or "cql2-json".
            sortby (SortByType): Field and direction to sort results by.
            limit (LimitType): Maximum number of items to return per page.
            page (PageType): 1-based page index for pagination.

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

        filter_lang : typing.Optional[GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang]
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
        HttpResponse[GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"auxip/collections/{encode_path_param(collection_id)}/items",
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
                    GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse,
                    parse_obj_as(
                        type_=GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse,
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

    def get_adgs_collection_specific_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse]:
        """
        Retrieve a specific item from a specified AUXIP collection.

        This endpoint fetches details of a specific item within the given AUXIP collection
        by its unique item ID. It utilizes the provided collection ID and item ID to
        validate access and return item information.

        Args:
            request (Request): The incoming HTTP request used for authentication and routing.
            collection_id (str): AUXIP collection ID. Must be a valid collection identifier
                (e.g., 'ins_s1').
            item_id (str): AUXIP item ID. Must be a valid item identifier
                (e.g., 'S1A_OPER_MPL_ORBPRE_20210214T021411_20210221T021411_0001.EOF').

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
        HttpResponse[GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"auxip/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse,
                    parse_obj_as(
                        type_=GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse,
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


class AsyncRawAdgsStationsClient:
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
            "auxip/search",
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
        Retrieve the RSPY ADGS Search catalog landing page.

        This endpoint generates a STAC (SpatioTemporal Asset Catalog) Catalog object that serves as the landing
        page for the RSPY ADGS service. The catalog includes basic metadata about the service and links to
        available collections.

        The resulting catalog contains:
        - `id`: A unique identifier for the catalog, generated as a UUID.
        - `description`: A brief description of the catalog.
        - `title`: The title of the catalog.
        - `stac_version`: The version of the STAC specification to which the catalog conforms.
        - `conformsTo`: A list of STAC and OGC API specifications that the catalog conforms to.
        - `links`: A link to the `/adgs/collections` endpoint where users can find available collections.

        The `stac_version` is set to "1.1.0", and the `conformsTo` field lists the relevant STAC and OGC API
        specifications that the catalog adheres to. A link to the collections endpoint is added to the catalog's
        `links` field, allowing users to discover available collections in the ADGS service.

        Parameters:
        - request: The HTTP request object which includes details about the incoming request.

        Returns:
        - dict: A dictionary representation of the STAC catalog, including metadata and links.

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
            "auxip",
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
            "auxip/conformance",
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

    async def get_allowed_adgs_collections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Return the ADGS collections to which the user has access to.

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
            "auxip/collections",
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

    async def get_adgs_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse]:
        """
        Return a specific ADGS collection.

        Parameters
        ----------
        collection_id : str
            E.G.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"auxip/collections/{encode_path_param(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse,
                    parse_obj_as(
                        type_=GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse,
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

    async def get_adgs_collection_items(
        self,
        collection_id: str,
        *,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_lang: typing.Optional[
            GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang
        ] = None,
        sortby: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse]:
        """
        Retrieve a list of items from a specified AUXIP collection.

        This endpoint returns a collection of items associated with the given AUXIP
        collection ID. It utilizes the collection ID to validate access and fetches
        the items based on defined query parameters.

        Args:
            request (Request): The incoming HTTP request used for authentication and routing.
            collection_id (str): AUXIP collection ID. Must be a valid collection identifier
                                 (e.g., 'ins_s1').
            bbox (BBoxType): Bounding box spatial filter, as [west, south, east, north] coordinates.
            datetime (DateTimeType): Temporal filter as an RFC 3339 timestamp or interval.
            filter_ (FilterType): CQL2 filter expression to further restrict results.
            filter_lang (FilterLangType): Language for the CQL2 filter, either "cql2-text" or "cql2-json".
            sortby (SortByType): Field and direction to sort results by.
            limit (LimitType): Maximum number of items to return per page.
            page (PageType): 1-based page index for pagination.

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

        filter_lang : typing.Optional[GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang]
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
        AsyncHttpResponse[GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"auxip/collections/{encode_path_param(collection_id)}/items",
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
                    GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse,
                    parse_obj_as(
                        type_=GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse,
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

    async def get_adgs_collection_specific_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse]:
        """
        Retrieve a specific item from a specified AUXIP collection.

        This endpoint fetches details of a specific item within the given AUXIP collection
        by its unique item ID. It utilizes the provided collection ID and item ID to
        validate access and return item information.

        Args:
            request (Request): The incoming HTTP request used for authentication and routing.
            collection_id (str): AUXIP collection ID. Must be a valid collection identifier
                (e.g., 'ins_s1').
            item_id (str): AUXIP item ID. Must be a valid item identifier
                (e.g., 'S1A_OPER_MPL_ORBPRE_20210214T021411_20210221T021411_0001.EOF').

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
        AsyncHttpResponse[GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"auxip/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse,
                    parse_obj_as(
                        type_=GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse,
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
