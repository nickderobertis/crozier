

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.distance_field import DistanceField
from ..types.facet_filter import FacetFilter
from ..types.highlight import Highlight
from ..types.query_facet import QueryFacet
from ..types.query_rewriting import QueryRewriting
from ..types.query_type import QueryType
from ..types.result_sort import ResultSort
from ..types.result_type import ResultType
from ..types.search_mode import SearchMode
from ..types.search_result_object import SearchResultObject
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawQueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def index_get(
        self,
        index_id: int,
        *,
        query: str,
        offset: int,
        length: int,
        realtime: bool,
        enable_empty_query: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchResultObject]:
        """
        Query results from index with index_id.
        Query index via GET is a convenience function, that **offers only a limited set of parameters compared to Query Index via POST**.
        Always use Query Index via POST for the full set of parameters and maximum flexibility.
        Query Index via GET is provided for simple queries and quick testing, and to be easily callable from browser address bar, but it is not intended for production use.

        Parameters
        ----------
        index_id : int
            index id

        query : str
            query string

        offset : int
            result offset

        length : int
            result length

        realtime : bool
            include uncommitted documents

        enable_empty_query : bool
            allow empty query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchResultObject]
            Results found, returns the SearchResultObject
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/query",
            method="GET",
            params={
                "query": query,
                "offset": offset,
                "length": length,
                "realtime": realtime,
                "enable_empty_query": enable_empty_query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchResultObject,
                    parse_obj_as(
                        type_=SearchResultObject,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def index_post(
        self,
        index_id: int,
        *,
        query: str,
        query_vector: typing.Optional[typing.Any] = OMIT,
        enable_empty_query: typing.Optional[bool] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        result_type: typing.Optional[ResultType] = OMIT,
        realtime: typing.Optional[bool] = OMIT,
        highlights: typing.Optional[typing.Sequence[Highlight]] = OMIT,
        field_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        distance_fields: typing.Optional[typing.Sequence[DistanceField]] = OMIT,
        query_facets: typing.Optional[typing.Sequence[QueryFacet]] = OMIT,
        facet_filter: typing.Optional[typing.Sequence[FacetFilter]] = OMIT,
        result_sort: typing.Optional[typing.Sequence[ResultSort]] = OMIT,
        query_type_default: typing.Optional[QueryType] = OMIT,
        query_rewriting: typing.Optional[QueryRewriting] = OMIT,
        search_mode: typing.Optional[SearchMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchResultObject]:
        """
        Query results from index with index_id
        The following parameters are supported:
        - Result type
        - Result sorting
        - Realtime search
        - Field filter
        - Fields to include in search results
        - Distance fields: derived fields from distance calculations
        - Highlights: keyword-in-context snippets and term highlighting
        - Query facets: which facets fields to calculate and return at query time
        - Facet filter: filter facets by field and value
        - Result sort: sort results by field and direction
        - Query type default: default query type, if not specified in query

        Parameters
        ----------
        index_id : int
            index id

        query : str
            Query string, search operators + - "" are recognized.

        query_vector : typing.Optional[typing.Any]
            Optional query vector: If None, then the query vector is derived from the query string using the specified model. If Some, then the query vector is used for semantic search and the query string is only used for lexical search and highlighting.

        enable_empty_query : typing.Optional[bool]
            Enable empty query: if true, an empty query string iterates through all indexed documents, supporting the query parameters: offset, length, query_facets, facet_filter, result_sort,
            otherwise an empty query string returns no results.
            Typical use cases include index browsing, index export, conversion, analytics, audits, and inspection.

        offset : typing.Optional[int]
            Offset of search results to return.

        length : typing.Optional[int]
            Number of search results to return.

        result_type : typing.Optional[ResultType]
            Specify the type of search result.

        realtime : typing.Optional[bool]
            True realtime search: include indexed, but uncommitted documents into search results.

        highlights : typing.Optional[typing.Sequence[Highlight]]
            Specify field names where to create keyword-in-context fragments and highlight query terms.

        field_filter : typing.Optional[typing.Sequence[str]]
            Specify field names where to search at querytime, whereas SchemaField.indexed is set at indextime. If empty then all indexed fields are searched.

        fields : typing.Optional[typing.Sequence[str]]
            Specify names of fields to return in the search results, where SchemaField.store is set at indextime. If empty then all stored fields are returned.

        distance_fields : typing.Optional[typing.Sequence[DistanceField]]
            Specify distance fields to derive at query time and return in the search results.

        query_facets : typing.Optional[typing.Sequence[QueryFacet]]
            Facets to return with search results: if empty then no facets are returned. Facets are only enabled on facet fields that are defined in schema at create_index!

        facet_filter : typing.Optional[typing.Sequence[FacetFilter]]
            Facet filters to filter search results by facet values: if empty then no facet filters are applied. Facet filters are only enabled on facet fields that are defined in schema at create_index!

        result_sort : typing.Optional[typing.Sequence[ResultSort]]
            Sort field and order:
            Search results are sorted by the specified facet field, either in ascending or descending order.
            If no sort field is specified, then the search results are sorted by rank in descending order per default.
            Multiple sort fields are combined by a "sort by, then sort by"-method ("tie-breaking"-algorithm).
            The results are sorted by the first field, and only for those results where the first field value is identical (tie) the results are sub-sorted by the second field,
            until the n-th field value is either not equal or the last field is reached.
            A special _score field (BM25x), reflecting how relevant the result is for a given search query (phrase match, match in title etc.) can be combined with any of the other sort fields as primary, secondary or n-th search criterium.
            Sort is only enabled on facet fields that are defined in schema at create_index!
            Examples:
            - result_sort = vec![ResultSort {field: "price".into(), order: SortOrder::Descending, base: FacetValue::None},ResultSort {field: "language".into(), order: SortOrder::Ascending, base: FacetValue::None}];
            - result_sort = vec![ResultSort {field: "location".into(),order: SortOrder::Ascending, base: FacetValue::Point(vec![38.8951, -77.0364])}];

        query_type_default : typing.Optional[QueryType]
            Specify default query type: (default=Intersection). This can be overwritten by search operator within the query string (+-"").

        query_rewriting : typing.Optional[QueryRewriting]
            Specify query rewriting method for search query correction and completion: (default=SearchOnly).

        search_mode : typing.Optional[SearchMode]
            Specify search mode: (default=Lexical).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchResultObject]
            Results found, returns the SearchResultObject
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/query",
            method="POST",
            json={
                "query": query,
                "query_vector": query_vector,
                "enable_empty_query": enable_empty_query,
                "offset": offset,
                "length": length,
                "result_type": result_type,
                "realtime": realtime,
                "highlights": convert_and_respect_annotation_metadata(
                    object_=highlights, annotation=typing.Sequence[Highlight], direction="write"
                ),
                "field_filter": field_filter,
                "fields": fields,
                "distance_fields": convert_and_respect_annotation_metadata(
                    object_=distance_fields, annotation=typing.Sequence[DistanceField], direction="write"
                ),
                "query_facets": convert_and_respect_annotation_metadata(
                    object_=query_facets, annotation=typing.Sequence[QueryFacet], direction="write"
                ),
                "facet_filter": convert_and_respect_annotation_metadata(
                    object_=facet_filter, annotation=typing.Sequence[FacetFilter], direction="write"
                ),
                "result_sort": convert_and_respect_annotation_metadata(
                    object_=result_sort, annotation=typing.Sequence[ResultSort], direction="write"
                ),
                "query_type_default": query_type_default,
                "query_rewriting": convert_and_respect_annotation_metadata(
                    object_=query_rewriting, annotation=QueryRewriting, direction="write"
                ),
                "search_mode": convert_and_respect_annotation_metadata(
                    object_=search_mode, annotation=SearchMode, direction="write"
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
                    SearchResultObject,
                    parse_obj_as(
                        type_=SearchResultObject,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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


class AsyncRawQueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def index_get(
        self,
        index_id: int,
        *,
        query: str,
        offset: int,
        length: int,
        realtime: bool,
        enable_empty_query: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchResultObject]:
        """
        Query results from index with index_id.
        Query index via GET is a convenience function, that **offers only a limited set of parameters compared to Query Index via POST**.
        Always use Query Index via POST for the full set of parameters and maximum flexibility.
        Query Index via GET is provided for simple queries and quick testing, and to be easily callable from browser address bar, but it is not intended for production use.

        Parameters
        ----------
        index_id : int
            index id

        query : str
            query string

        offset : int
            result offset

        length : int
            result length

        realtime : bool
            include uncommitted documents

        enable_empty_query : bool
            allow empty query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchResultObject]
            Results found, returns the SearchResultObject
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/query",
            method="GET",
            params={
                "query": query,
                "offset": offset,
                "length": length,
                "realtime": realtime,
                "enable_empty_query": enable_empty_query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchResultObject,
                    parse_obj_as(
                        type_=SearchResultObject,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def index_post(
        self,
        index_id: int,
        *,
        query: str,
        query_vector: typing.Optional[typing.Any] = OMIT,
        enable_empty_query: typing.Optional[bool] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        result_type: typing.Optional[ResultType] = OMIT,
        realtime: typing.Optional[bool] = OMIT,
        highlights: typing.Optional[typing.Sequence[Highlight]] = OMIT,
        field_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        distance_fields: typing.Optional[typing.Sequence[DistanceField]] = OMIT,
        query_facets: typing.Optional[typing.Sequence[QueryFacet]] = OMIT,
        facet_filter: typing.Optional[typing.Sequence[FacetFilter]] = OMIT,
        result_sort: typing.Optional[typing.Sequence[ResultSort]] = OMIT,
        query_type_default: typing.Optional[QueryType] = OMIT,
        query_rewriting: typing.Optional[QueryRewriting] = OMIT,
        search_mode: typing.Optional[SearchMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchResultObject]:
        """
        Query results from index with index_id
        The following parameters are supported:
        - Result type
        - Result sorting
        - Realtime search
        - Field filter
        - Fields to include in search results
        - Distance fields: derived fields from distance calculations
        - Highlights: keyword-in-context snippets and term highlighting
        - Query facets: which facets fields to calculate and return at query time
        - Facet filter: filter facets by field and value
        - Result sort: sort results by field and direction
        - Query type default: default query type, if not specified in query

        Parameters
        ----------
        index_id : int
            index id

        query : str
            Query string, search operators + - "" are recognized.

        query_vector : typing.Optional[typing.Any]
            Optional query vector: If None, then the query vector is derived from the query string using the specified model. If Some, then the query vector is used for semantic search and the query string is only used for lexical search and highlighting.

        enable_empty_query : typing.Optional[bool]
            Enable empty query: if true, an empty query string iterates through all indexed documents, supporting the query parameters: offset, length, query_facets, facet_filter, result_sort,
            otherwise an empty query string returns no results.
            Typical use cases include index browsing, index export, conversion, analytics, audits, and inspection.

        offset : typing.Optional[int]
            Offset of search results to return.

        length : typing.Optional[int]
            Number of search results to return.

        result_type : typing.Optional[ResultType]
            Specify the type of search result.

        realtime : typing.Optional[bool]
            True realtime search: include indexed, but uncommitted documents into search results.

        highlights : typing.Optional[typing.Sequence[Highlight]]
            Specify field names where to create keyword-in-context fragments and highlight query terms.

        field_filter : typing.Optional[typing.Sequence[str]]
            Specify field names where to search at querytime, whereas SchemaField.indexed is set at indextime. If empty then all indexed fields are searched.

        fields : typing.Optional[typing.Sequence[str]]
            Specify names of fields to return in the search results, where SchemaField.store is set at indextime. If empty then all stored fields are returned.

        distance_fields : typing.Optional[typing.Sequence[DistanceField]]
            Specify distance fields to derive at query time and return in the search results.

        query_facets : typing.Optional[typing.Sequence[QueryFacet]]
            Facets to return with search results: if empty then no facets are returned. Facets are only enabled on facet fields that are defined in schema at create_index!

        facet_filter : typing.Optional[typing.Sequence[FacetFilter]]
            Facet filters to filter search results by facet values: if empty then no facet filters are applied. Facet filters are only enabled on facet fields that are defined in schema at create_index!

        result_sort : typing.Optional[typing.Sequence[ResultSort]]
            Sort field and order:
            Search results are sorted by the specified facet field, either in ascending or descending order.
            If no sort field is specified, then the search results are sorted by rank in descending order per default.
            Multiple sort fields are combined by a "sort by, then sort by"-method ("tie-breaking"-algorithm).
            The results are sorted by the first field, and only for those results where the first field value is identical (tie) the results are sub-sorted by the second field,
            until the n-th field value is either not equal or the last field is reached.
            A special _score field (BM25x), reflecting how relevant the result is for a given search query (phrase match, match in title etc.) can be combined with any of the other sort fields as primary, secondary or n-th search criterium.
            Sort is only enabled on facet fields that are defined in schema at create_index!
            Examples:
            - result_sort = vec![ResultSort {field: "price".into(), order: SortOrder::Descending, base: FacetValue::None},ResultSort {field: "language".into(), order: SortOrder::Ascending, base: FacetValue::None}];
            - result_sort = vec![ResultSort {field: "location".into(),order: SortOrder::Ascending, base: FacetValue::Point(vec![38.8951, -77.0364])}];

        query_type_default : typing.Optional[QueryType]
            Specify default query type: (default=Intersection). This can be overwritten by search operator within the query string (+-"").

        query_rewriting : typing.Optional[QueryRewriting]
            Specify query rewriting method for search query correction and completion: (default=SearchOnly).

        search_mode : typing.Optional[SearchMode]
            Specify search mode: (default=Lexical).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchResultObject]
            Results found, returns the SearchResultObject
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/query",
            method="POST",
            json={
                "query": query,
                "query_vector": query_vector,
                "enable_empty_query": enable_empty_query,
                "offset": offset,
                "length": length,
                "result_type": result_type,
                "realtime": realtime,
                "highlights": convert_and_respect_annotation_metadata(
                    object_=highlights, annotation=typing.Sequence[Highlight], direction="write"
                ),
                "field_filter": field_filter,
                "fields": fields,
                "distance_fields": convert_and_respect_annotation_metadata(
                    object_=distance_fields, annotation=typing.Sequence[DistanceField], direction="write"
                ),
                "query_facets": convert_and_respect_annotation_metadata(
                    object_=query_facets, annotation=typing.Sequence[QueryFacet], direction="write"
                ),
                "facet_filter": convert_and_respect_annotation_metadata(
                    object_=facet_filter, annotation=typing.Sequence[FacetFilter], direction="write"
                ),
                "result_sort": convert_and_respect_annotation_metadata(
                    object_=result_sort, annotation=typing.Sequence[ResultSort], direction="write"
                ),
                "query_type_default": query_type_default,
                "query_rewriting": convert_and_respect_annotation_metadata(
                    object_=query_rewriting, annotation=QueryRewriting, direction="write"
                ),
                "search_mode": convert_and_respect_annotation_metadata(
                    object_=search_mode, annotation=SearchMode, direction="write"
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
                    SearchResultObject,
                    parse_obj_as(
                        type_=SearchResultObject,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
