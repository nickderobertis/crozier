

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.order import Order
from .raw_client import AsyncRawSearchClient, RawSearchClient
from .types.search_entities_request_bounding_box import SearchEntitiesRequestBoundingBox
from .types.search_entities_request_filters_value import SearchEntitiesRequestFiltersValue
from .types.search_entities_request_search_type import SearchEntitiesRequestSearchType
from .types.search_entities_request_sort import SearchEntitiesRequestSort
from .types.search_entities_response import SearchEntitiesResponse


OMIT = typing.cast(typing.Any, ...)


class SearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSearchClient
        """
        return self._raw_client

    def entities(
        self,
        *,
        query: str,
        search_type: typing.Optional[SearchEntitiesRequestSearchType] = OMIT,
        filters: typing.Optional[typing.Dict[str, SearchEntitiesRequestFiltersValue]] = OMIT,
        bounding_box: typing.Optional[SearchEntitiesRequestBoundingBox] = OMIT,
        geohash_precision: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort: typing.Optional[SearchEntitiesRequestSort] = OMIT,
        order: typing.Optional[Order] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchEntitiesResponse:
        """
        Perform advanced or basic searches across the entire RO-Crate collection. This includes free text queries, as well as filters for specific fields such as `inLanguage` or `mediaType`. The search results can be paginated, sorted, and optionally returned alongside facet counts.

        Parameters
        ----------
        query : str
            The query string used in the search. Behavior depends on `searchType`. For `basic`, this can be free text. For `advanced`, Boolean operators can be used.

            When searchType is `basic` this is a free text field of text to search.

            When searchType is `advanced` this is a boolean search field.
            Examples:
              name: John
              name: John AND description: Engineer
              name: John AND (description: Engineer OR description: developer)

            NOTE: This API is implementation-agnostic. The examples above show basic boolean syntax that most search engines support.
            API implementors may support additional query syntax - refer to your implementation's documentation for details.

        search_type : typing.Optional[SearchEntitiesRequestSearchType]
            Specifies the search method to be used. `basic` searches across common fields, whereas `advanced` can handle Boolean queries or more complex logic.

        filters : typing.Optional[typing.Dict[str, SearchEntitiesRequestFiltersValue]]
            A set of key-value pairs representing additional filters. Keys MUST be filter fields the implementation declares in `/capabilities` under `search.filters`; a request using an undeclared key MUST be rejected with a 400 `ValidationError`.

            Each value is either an array of acceptable values (matched as exact terms, valid for any filter type), a single range object with inclusive `gte`/`lte` bounds, or a non-empty array of range objects matched as an OR of the ranges — an entity matches when any of the ranges matches. Ranges, single or in an array, are valid only for filters declared with type `date` or `number`; a range sent to a `string` or `boolean` filter MUST be rejected with a 400 `ValidationError`. An array MUST NOT mix exact terms and range objects; such a request MUST be rejected with a 400 `ValidationError`.

        bounding_box : typing.Optional[SearchEntitiesRequestBoundingBox]
            Will filter the results to entities that exist inside the bounding box.

        geohash_precision : typing.Optional[int]
            If supplied, returns a geohash grid with this precision. Must be between 1 (lowest precision) and 12 (highest precision).

        limit : typing.Optional[int]
            Maximum number of entities to return per page.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, enabling paging.

        sort : typing.Optional[SearchEntitiesRequestSort]
            The field on which to sort results. Defaults to `relevance`, which orders
            results by search score (highest first). When set to `relevance`, the
            `order` parameter is ignored. Use `id`, `name`, `createdAt`, or
            `updatedAt` to sort by a specific field.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchEntitiesResponse
            OK

        Examples
        --------
        from fern.search import (
            SearchEntitiesRequestBoundingBox,
            SearchEntitiesRequestBoundingBoxBottomLeft,
            SearchEntitiesRequestBoundingBoxTopRight,
        )

        from fern import FernApi, FilterRange

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.search.entities(
            search_type="advanced",
            query="name: West Alor AND description: linguistic",
            filters={
                "inLanguage": ["English"],
                "mediaType": ["audio/mpeg"],
                "createdAt": [
                    FilterRange(
                        gte="1965-01-01",
                        lte="1965-12-31",
                    ),
                    FilterRange(
                        gte="1972-01-01",
                        lte="1972-12-31",
                    ),
                ],
            },
            bounding_box=SearchEntitiesRequestBoundingBox(
                top_right=SearchEntitiesRequestBoundingBoxTopRight(
                    lat=-33.7,
                    lng=151.3,
                ),
                bottom_left=SearchEntitiesRequestBoundingBoxBottomLeft(
                    lat=-34.1,
                    lng=150.9,
                ),
            ),
            limit=20,
            offset=0,
            order="desc",
        )
        """
        _response = self._raw_client.entities(
            query=query,
            search_type=search_type,
            filters=filters,
            bounding_box=bounding_box,
            geohash_precision=geohash_precision,
            limit=limit,
            offset=offset,
            sort=sort,
            order=order,
            request_options=request_options,
        )
        return _response.data


class AsyncSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSearchClient
        """
        return self._raw_client

    async def entities(
        self,
        *,
        query: str,
        search_type: typing.Optional[SearchEntitiesRequestSearchType] = OMIT,
        filters: typing.Optional[typing.Dict[str, SearchEntitiesRequestFiltersValue]] = OMIT,
        bounding_box: typing.Optional[SearchEntitiesRequestBoundingBox] = OMIT,
        geohash_precision: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort: typing.Optional[SearchEntitiesRequestSort] = OMIT,
        order: typing.Optional[Order] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchEntitiesResponse:
        """
        Perform advanced or basic searches across the entire RO-Crate collection. This includes free text queries, as well as filters for specific fields such as `inLanguage` or `mediaType`. The search results can be paginated, sorted, and optionally returned alongside facet counts.

        Parameters
        ----------
        query : str
            The query string used in the search. Behavior depends on `searchType`. For `basic`, this can be free text. For `advanced`, Boolean operators can be used.

            When searchType is `basic` this is a free text field of text to search.

            When searchType is `advanced` this is a boolean search field.
            Examples:
              name: John
              name: John AND description: Engineer
              name: John AND (description: Engineer OR description: developer)

            NOTE: This API is implementation-agnostic. The examples above show basic boolean syntax that most search engines support.
            API implementors may support additional query syntax - refer to your implementation's documentation for details.

        search_type : typing.Optional[SearchEntitiesRequestSearchType]
            Specifies the search method to be used. `basic` searches across common fields, whereas `advanced` can handle Boolean queries or more complex logic.

        filters : typing.Optional[typing.Dict[str, SearchEntitiesRequestFiltersValue]]
            A set of key-value pairs representing additional filters. Keys MUST be filter fields the implementation declares in `/capabilities` under `search.filters`; a request using an undeclared key MUST be rejected with a 400 `ValidationError`.

            Each value is either an array of acceptable values (matched as exact terms, valid for any filter type), a single range object with inclusive `gte`/`lte` bounds, or a non-empty array of range objects matched as an OR of the ranges — an entity matches when any of the ranges matches. Ranges, single or in an array, are valid only for filters declared with type `date` or `number`; a range sent to a `string` or `boolean` filter MUST be rejected with a 400 `ValidationError`. An array MUST NOT mix exact terms and range objects; such a request MUST be rejected with a 400 `ValidationError`.

        bounding_box : typing.Optional[SearchEntitiesRequestBoundingBox]
            Will filter the results to entities that exist inside the bounding box.

        geohash_precision : typing.Optional[int]
            If supplied, returns a geohash grid with this precision. Must be between 1 (lowest precision) and 12 (highest precision).

        limit : typing.Optional[int]
            Maximum number of entities to return per page.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, enabling paging.

        sort : typing.Optional[SearchEntitiesRequestSort]
            The field on which to sort results. Defaults to `relevance`, which orders
            results by search score (highest first). When set to `relevance`, the
            `order` parameter is ignored. Use `id`, `name`, `createdAt`, or
            `updatedAt` to sort by a specific field.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchEntitiesResponse
            OK

        Examples
        --------
        import asyncio

        from fern.search import (
            SearchEntitiesRequestBoundingBox,
            SearchEntitiesRequestBoundingBoxBottomLeft,
            SearchEntitiesRequestBoundingBoxTopRight,
        )

        from fern import AsyncFernApi, FilterRange

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search.entities(
                search_type="advanced",
                query="name: West Alor AND description: linguistic",
                filters={
                    "inLanguage": ["English"],
                    "mediaType": ["audio/mpeg"],
                    "createdAt": [
                        FilterRange(
                            gte="1965-01-01",
                            lte="1965-12-31",
                        ),
                        FilterRange(
                            gte="1972-01-01",
                            lte="1972-12-31",
                        ),
                    ],
                },
                bounding_box=SearchEntitiesRequestBoundingBox(
                    top_right=SearchEntitiesRequestBoundingBoxTopRight(
                        lat=-33.7,
                        lng=151.3,
                    ),
                    bottom_left=SearchEntitiesRequestBoundingBoxBottomLeft(
                        lat=-34.1,
                        lng=150.9,
                    ),
                ),
                limit=20,
                offset=0,
                order="desc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.entities(
            query=query,
            search_type=search_type,
            filters=filters,
            bounding_box=bounding_box,
            geohash_precision=geohash_precision,
            limit=limit,
            offset=offset,
            sort=sort,
            order=order,
            request_options=request_options,
        )
        return _response.data
