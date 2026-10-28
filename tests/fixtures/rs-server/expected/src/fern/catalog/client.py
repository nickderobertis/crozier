

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collections import Collections
from ..types.conformance import Conformance
from ..types.item_collection_output import ItemCollectionOutput
from ..types.landing_page import LandingPage
from ..types.post_fields_extension import PostFieldsExtension
from ..types.search_post_request_filter_lang import SearchPostRequestFilterLang
from ..types.search_post_request_intersects import SearchPostRequestIntersects
from ..types.sort_extension import SortExtension
from ..types.stac_pydantic_api_collection_collection import StacPydanticApiCollectionCollection
from ..types.stac_pydantic_api_item_item import StacPydanticApiItemItem
from .raw_client import AsyncRawCatalogClient, RawCatalogClient
from .types.get_collections_catalog_collections_get_request_filter_lang import (
    GetCollectionsCatalogCollectionsGetRequestFilterLang,
)
from .types.get_item_collection_catalog_collections_collection_id_items_get_request_filter_lang import (
    GetItemCollectionCatalogCollectionsCollectionIdItemsGetRequestFilterLang,
)


OMIT = typing.cast(typing.Any, ...)


class CatalogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCatalogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogClient
        """
        return self._raw_client

    def landing_page(self, *, request_options: typing.Optional[RequestOptions] = None) -> LandingPage:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LandingPage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog.landing_page()
        """
        _response = self._raw_client.landing_page(request_options=request_options)
        return _response.data

    def conformance_classes(self, *, request_options: typing.Optional[RequestOptions] = None) -> Conformance:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conformance
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog.conformance_classes()
        """
        _response = self._raw_client.conformance_classes(request_options=request_options)
        return _response.data

    def get_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StacPydanticApiItemItem:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticApiItemItem
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog.get_item(
            collection_id="collection_id",
            item_id="item_id",
        )
        """
        _response = self._raw_client.get_item(collection_id, item_id, request_options=request_options)
        return _response.data

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
    ) -> ItemCollectionOutput:
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
        ItemCollectionOutput
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog.search()
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

    def get_collections(
        self,
        *,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        sortby: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_crs: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetCollectionsCatalogCollectionsGetRequestFilterLang] = None,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collections:
        """
        Endpoint.

        Parameters
        ----------
        bbox : typing.Optional[str]
            Only return items intersecting this bounding box. Mutually exclusive with **intersects**.

        datetime : typing.Optional[str]
            Only return items that have a temporal property that intersects this value.

            Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response.

        query : typing.Optional[str]
            Allows additional filtering based on the properties of Item objects

        sortby : typing.Optional[str]
            An array of property names, prefixed by either '+' for ascending or '-' for descending. If no prefix is provided, '+' is assumed.

        fields : typing.Optional[str]
            Include or exclude fields from items body.

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2-JSON` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.htmln
            Remember to URL encode the CQL2-JSON if using GET

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[GetCollectionsCatalogCollectionsGetRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        q : typing.Optional[str]
            Parameter to perform free-text queries against STAC metadata

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collections
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog.get_collections()
        """
        _response = self._raw_client.get_collections(
            bbox=bbox,
            datetime=datetime,
            limit=limit,
            query=query,
            sortby=sortby,
            fields=fields,
            filter=filter,
            filter_crs=filter_crs,
            filter_lang=filter_lang,
            q=q,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def get_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StacPydanticApiCollectionCollection:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticApiCollectionCollection
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog.get_collection(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.get_collection(collection_id, request_options=request_options)
        return _response.data

    def get_item_collection(
        self,
        collection_id: str,
        *,
        limit: typing.Optional[int] = None,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        sortby: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_crs: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetItemCollectionCatalogCollectionsCollectionIdItemsGetRequestFilterLang] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemCollectionOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (capped to 10_000).

        bbox : typing.Optional[str]
            Only return items intersecting this bounding box. Mutually exclusive with **intersects**.

        datetime : typing.Optional[str]
            Only return items that have a temporal property that intersects this value.

            Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.

        query : typing.Optional[str]
            Allows additional filtering based on the properties of Item objects

        sortby : typing.Optional[str]
            An array of property names, prefixed by either '+' for ascending or '-' for descending. If no prefix is provided, '+' is assumed.

        fields : typing.Optional[str]
            Include or exclude fields from items body.

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2-JSON` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.htmln
            Remember to URL encode the CQL2-JSON if using GET

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[GetItemCollectionCatalogCollectionsCollectionIdItemsGetRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemCollectionOutput
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog.get_item_collection(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.get_item_collection(
            collection_id,
            limit=limit,
            bbox=bbox,
            datetime=datetime,
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


class AsyncCatalogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCatalogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogClient
        """
        return self._raw_client

    async def landing_page(self, *, request_options: typing.Optional[RequestOptions] = None) -> LandingPage:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LandingPage
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
            await client.catalog.landing_page()


        asyncio.run(main())
        """
        _response = await self._raw_client.landing_page(request_options=request_options)
        return _response.data

    async def conformance_classes(self, *, request_options: typing.Optional[RequestOptions] = None) -> Conformance:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conformance
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
            await client.catalog.conformance_classes()


        asyncio.run(main())
        """
        _response = await self._raw_client.conformance_classes(request_options=request_options)
        return _response.data

    async def get_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StacPydanticApiItemItem:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticApiItemItem
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
            await client.catalog.get_item(
                collection_id="collection_id",
                item_id="item_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_item(collection_id, item_id, request_options=request_options)
        return _response.data

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
    ) -> ItemCollectionOutput:
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
        ItemCollectionOutput
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
            await client.catalog.search()


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

    async def get_collections(
        self,
        *,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        sortby: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_crs: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetCollectionsCatalogCollectionsGetRequestFilterLang] = None,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collections:
        """
        Endpoint.

        Parameters
        ----------
        bbox : typing.Optional[str]
            Only return items intersecting this bounding box. Mutually exclusive with **intersects**.

        datetime : typing.Optional[str]
            Only return items that have a temporal property that intersects this value.

            Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response.

        query : typing.Optional[str]
            Allows additional filtering based on the properties of Item objects

        sortby : typing.Optional[str]
            An array of property names, prefixed by either '+' for ascending or '-' for descending. If no prefix is provided, '+' is assumed.

        fields : typing.Optional[str]
            Include or exclude fields from items body.

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2-JSON` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.htmln
            Remember to URL encode the CQL2-JSON if using GET

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[GetCollectionsCatalogCollectionsGetRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        q : typing.Optional[str]
            Parameter to perform free-text queries against STAC metadata

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collections
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
            await client.catalog.get_collections()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collections(
            bbox=bbox,
            datetime=datetime,
            limit=limit,
            query=query,
            sortby=sortby,
            fields=fields,
            filter=filter,
            filter_crs=filter_crs,
            filter_lang=filter_lang,
            q=q,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def get_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StacPydanticApiCollectionCollection:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticApiCollectionCollection
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
            await client.catalog.get_collection(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection(collection_id, request_options=request_options)
        return _response.data

    async def get_item_collection(
        self,
        collection_id: str,
        *,
        limit: typing.Optional[int] = None,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        sortby: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_crs: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetItemCollectionCatalogCollectionsCollectionIdItemsGetRequestFilterLang] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemCollectionOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (capped to 10_000).

        bbox : typing.Optional[str]
            Only return items intersecting this bounding box. Mutually exclusive with **intersects**.

        datetime : typing.Optional[str]
            Only return items that have a temporal property that intersects this value.

            Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.

        query : typing.Optional[str]
            Allows additional filtering based on the properties of Item objects

        sortby : typing.Optional[str]
            An array of property names, prefixed by either '+' for ascending or '-' for descending. If no prefix is provided, '+' is assumed.

        fields : typing.Optional[str]
            Include or exclude fields from items body.

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2-JSON` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.htmln
            Remember to URL encode the CQL2-JSON if using GET

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[GetItemCollectionCatalogCollectionsCollectionIdItemsGetRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemCollectionOutput
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
            await client.catalog.get_item_collection(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_item_collection(
            collection_id,
            limit=limit,
            bbox=bbox,
            datetime=datetime,
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
