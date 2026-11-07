

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawQueryClient, RawQueryClient


OMIT = typing.cast(typing.Any, ...)


class QueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueryClient
        """
        return self._raw_client

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
    ) -> SearchResultObject:
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
        SearchResultObject
            Results found, returns the SearchResultObject

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.query.index_get(
            index_id=1000000,
            query="hello",
            offset=1000000,
            length=1000000,
            realtime=True,
            enable_empty_query=True,
        )
        """
        _response = self._raw_client.index_get(
            index_id,
            query=query,
            offset=offset,
            length=length,
            realtime=realtime,
            enable_empty_query=enable_empty_query,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SearchResultObject:
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
        SearchResultObject
            Results found, returns the SearchResultObject

        Examples
        --------
        from fern import (
            AnnModeNprobe,
            FernApi,
            Highlight,
            SearchModeHybrid,
            SearchModeHybridHybrid,
        )

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.query.index_post(
            index_id=1000000,
            query="detroit",
            enable_empty_query=False,
            offset=0,
            length=10,
            result_type="TopkCount",
            realtime=True,
            highlights=[
                Highlight(
                    field="",
                    name="",
                    fragment_number=0,
                    fragment_size=0,
                    highlight_markup=True,
                    pre_tags="",
                    post_tags="",
                )
            ],
            field_filter=["title"],
            fields=["fields"],
            query_type_default="Intersection",
            query_rewriting="SearchOnly",
            search_mode=SearchModeHybrid(
                hybrid=SearchModeHybridHybrid(
                    similarity_threshold=0.7,
                    ann_mode=AnnModeNprobe(
                        nprobe=55,
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.index_post(
            index_id,
            query=query,
            query_vector=query_vector,
            enable_empty_query=enable_empty_query,
            offset=offset,
            length=length,
            result_type=result_type,
            realtime=realtime,
            highlights=highlights,
            field_filter=field_filter,
            fields=fields,
            distance_fields=distance_fields,
            query_facets=query_facets,
            facet_filter=facet_filter,
            result_sort=result_sort,
            query_type_default=query_type_default,
            query_rewriting=query_rewriting,
            search_mode=search_mode,
            request_options=request_options,
        )
        return _response.data


class AsyncQueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueryClient
        """
        return self._raw_client

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
    ) -> SearchResultObject:
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
        SearchResultObject
            Results found, returns the SearchResultObject

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.query.index_get(
                index_id=1000000,
                query="hello",
                offset=1000000,
                length=1000000,
                realtime=True,
                enable_empty_query=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.index_get(
            index_id,
            query=query,
            offset=offset,
            length=length,
            realtime=realtime,
            enable_empty_query=enable_empty_query,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SearchResultObject:
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
        SearchResultObject
            Results found, returns the SearchResultObject

        Examples
        --------
        import asyncio

        from fern import (
            AnnModeNprobe,
            AsyncFernApi,
            Highlight,
            SearchModeHybrid,
            SearchModeHybridHybrid,
        )

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.query.index_post(
                index_id=1000000,
                query="detroit",
                enable_empty_query=False,
                offset=0,
                length=10,
                result_type="TopkCount",
                realtime=True,
                highlights=[
                    Highlight(
                        field="",
                        name="",
                        fragment_number=0,
                        fragment_size=0,
                        highlight_markup=True,
                        pre_tags="",
                        post_tags="",
                    )
                ],
                field_filter=["title"],
                fields=["fields"],
                query_type_default="Intersection",
                query_rewriting="SearchOnly",
                search_mode=SearchModeHybrid(
                    hybrid=SearchModeHybridHybrid(
                        similarity_threshold=0.7,
                        ann_mode=AnnModeNprobe(
                            nprobe=55,
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.index_post(
            index_id,
            query=query,
            query_vector=query_vector,
            enable_empty_query=enable_empty_query,
            offset=offset,
            length=length,
            result_type=result_type,
            realtime=realtime,
            highlights=highlights,
            field_filter=field_filter,
            fields=fields,
            distance_fields=distance_fields,
            query_facets=query_facets,
            facet_filter=facet_filter,
            result_sort=result_sort,
            query_type_default=query_type_default,
            query_rewriting=query_rewriting,
            search_mode=search_mode,
            request_options=request_options,
        )
        return _response.data
