

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.item_collection import ItemCollection
from ..types.post_fields_extension import PostFieldsExtension
from ..types.search_post_request_filter_lang import SearchPostRequestFilterLang
from ..types.search_post_request_intersects import SearchPostRequestIntersects
from ..types.sort_extension import SortExtension
from .raw_client import AsyncRawPripStationsClient, RawPripStationsClient
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


OMIT = typing.cast(typing.Any, ...)


class PripStationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPripStationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPripStationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPripStationsClient
        """
        return self._raw_client

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
    ) -> ItemCollection:
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
        ItemCollection
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prip_stations.search()
        """
        _response = self._raw_client.search(
            collections=collections,
            ids=ids,
            bbox=bbox,
            intersects=intersects,
            datetime=datetime,
            limit=limit,
            conf=conf,
            query=query,
            sortby=sortby,
            fields=fields,
            filter=filter,
            filter_crs=filter_crs,
            filter_lang=filter_lang,
            token=token,
            request_options=request_options,
        )
        return _response.data

    def get_root_catalog(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Redirect to the landing page.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prip_stations.get_root_catalog()
        """
        _response = self._raw_client.get_root_catalog(request_options=request_options)
        return _response.data

    def get_conformance(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Return the STAC/OGC conformance classes implemented by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prip_stations.get_conformance()
        """
        _response = self._raw_client.get_conformance(request_options=request_options)
        return _response.data

    def get_allowed_prip_collections(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Return the PRIP collections to which the user has access to.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prip_stations.get_allowed_prip_collections()
        """
        _response = self._raw_client.get_allowed_prip_collections(request_options=request_options)
        return _response.data

    def get_prip_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPripCollectionPripCollectionsCollectionIdGetResponse:
        """
        Return a specific PRIP collection.

        Parameters
        ----------
        collection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPripCollectionPripCollectionsCollectionIdGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prip_stations.get_prip_collection(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.get_prip_collection(collection_id, request_options=request_options)
        return _response.data

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
    ) -> GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse:
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
        GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prip_stations.get_prip_collection_items(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.get_prip_collection_items(
            collection_id,
            bbox=bbox,
            datetime=datetime,
            filter=filter,
            filter_lang=filter_lang,
            sortby=sortby,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def get_prip_collection_specific_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse:
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
        GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prip_stations.get_prip_collection_specific_item(
            collection_id="collection_id",
            item_id="item_id",
        )
        """
        _response = self._raw_client.get_prip_collection_specific_item(
            collection_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncPripStationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPripStationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPripStationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPripStationsClient
        """
        return self._raw_client

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
    ) -> ItemCollection:
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
        ItemCollection
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prip_stations.search()


        asyncio.run(main())
        """
        _response = await self._raw_client.search(
            collections=collections,
            ids=ids,
            bbox=bbox,
            intersects=intersects,
            datetime=datetime,
            limit=limit,
            conf=conf,
            query=query,
            sortby=sortby,
            fields=fields,
            filter=filter,
            filter_crs=filter_crs,
            filter_lang=filter_lang,
            token=token,
            request_options=request_options,
        )
        return _response.data

    async def get_root_catalog(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Redirect to the landing page.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prip_stations.get_root_catalog()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_root_catalog(request_options=request_options)
        return _response.data

    async def get_conformance(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Return the STAC/OGC conformance classes implemented by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prip_stations.get_conformance()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conformance(request_options=request_options)
        return _response.data

    async def get_allowed_prip_collections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Return the PRIP collections to which the user has access to.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prip_stations.get_allowed_prip_collections()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_allowed_prip_collections(request_options=request_options)
        return _response.data

    async def get_prip_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPripCollectionPripCollectionsCollectionIdGetResponse:
        """
        Return a specific PRIP collection.

        Parameters
        ----------
        collection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPripCollectionPripCollectionsCollectionIdGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prip_stations.get_prip_collection(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prip_collection(collection_id, request_options=request_options)
        return _response.data

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
    ) -> GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse:
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
        GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prip_stations.get_prip_collection_items(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prip_collection_items(
            collection_id,
            bbox=bbox,
            datetime=datetime,
            filter=filter,
            filter_lang=filter_lang,
            sortby=sortby,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def get_prip_collection_specific_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse:
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
        GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prip_stations.get_prip_collection_specific_item(
                collection_id="collection_id",
                item_id="item_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prip_collection_specific_item(
            collection_id, item_id, request_options=request_options
        )
        return _response.data
