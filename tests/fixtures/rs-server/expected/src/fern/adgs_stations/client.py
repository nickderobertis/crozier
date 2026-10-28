

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.item_collection import ItemCollection
from ..types.post_fields_extension import PostFieldsExtension
from ..types.search_post_request_filter_lang import SearchPostRequestFilterLang
from ..types.search_post_request_intersects import SearchPostRequestIntersects
from ..types.sort_extension import SortExtension
from .raw_client import AsyncRawAdgsStationsClient, RawAdgsStationsClient
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


OMIT = typing.cast(typing.Any, ...)


class AdgsStationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdgsStationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdgsStationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdgsStationsClient
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
        client.adgs_stations.search()
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.adgs_stations.get_root_catalog()
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
        client.adgs_stations.get_conformance()
        """
        _response = self._raw_client.get_conformance(request_options=request_options)
        return _response.data

    def get_allowed_adgs_collections(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Return the ADGS collections to which the user has access to.

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
        client.adgs_stations.get_allowed_adgs_collections()
        """
        _response = self._raw_client.get_allowed_adgs_collections(request_options=request_options)
        return _response.data

    def get_adgs_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse:
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
        GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.adgs_stations.get_adgs_collection(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.get_adgs_collection(collection_id, request_options=request_options)
        return _response.data

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
    ) -> GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse:
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
        GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.adgs_stations.get_adgs_collection_items(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.get_adgs_collection_items(
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

    def get_adgs_collection_specific_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse:
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
        GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.adgs_stations.get_adgs_collection_specific_item(
            collection_id="collection_id",
            item_id="item_id",
        )
        """
        _response = self._raw_client.get_adgs_collection_specific_item(
            collection_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncAdgsStationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdgsStationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdgsStationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdgsStationsClient
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
            await client.adgs_stations.search()


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
            await client.adgs_stations.get_root_catalog()


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
            await client.adgs_stations.get_conformance()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conformance(request_options=request_options)
        return _response.data

    async def get_allowed_adgs_collections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Return the ADGS collections to which the user has access to.

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
            await client.adgs_stations.get_allowed_adgs_collections()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_allowed_adgs_collections(request_options=request_options)
        return _response.data

    async def get_adgs_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse:
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
        GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse
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
            await client.adgs_stations.get_adgs_collection(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_adgs_collection(collection_id, request_options=request_options)
        return _response.data

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
    ) -> GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse:
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
        GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse
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
            await client.adgs_stations.get_adgs_collection_items(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_adgs_collection_items(
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

    async def get_adgs_collection_specific_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse:
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
        GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse
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
            await client.adgs_stations.get_adgs_collection_specific_item(
                collection_id="collection_id",
                item_id="item_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_adgs_collection_specific_item(
            collection_id, item_id, request_options=request_options
        )
        return _response.data
