

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_price_book_by_id_response import GetPriceBookByIdResponse
from ..types.get_pricebook_item_by_id_response import GetPricebookItemByIdResponse
from ..types.get_pricebook_items_response import GetPricebookItemsResponse
from ..types.get_pricebooks_response import GetPricebooksResponse
from ..types.search_pricebooks_response import SearchPricebooksResponse
from .raw_client import AsyncRawPricebooksClient, RawPricebooksClient
from .types.get_pricebooks_id_pricebook_items_request_sort_order import GetPricebooksIdPricebookItemsRequestSortOrder
from .types.get_pricebooks_request_sort_field import GetPricebooksRequestSortField
from .types.get_pricebooks_request_sort_order import GetPricebooksRequestSortOrder
from .types.post_pricebooks_search_request_sort_order import PostPricebooksSearchRequestSortOrder


OMIT = typing.cast(typing.Any, ...)


class PricebooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPricebooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPricebooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPricebooksClient
        """
        return self._raw_client

    def post_pricebooks_search(
        self,
        *,
        search: str,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[PostPricebooksSearchRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        pricing_tier_id: typing.Optional[float] = OMIT,
        all_suppliers: typing.Optional[bool] = OMIT,
        supplier_ids: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchPricebooksResponse:
        """
        Search for pricebook items across multiple pricebooks

        This endpoint allows you to search for products/items across one or more supplier pricebooks using a text-based search query. The search is performed across item names, product codes, and search values.

        **Search Behavior:**
        - Searches match when the search term appears anywhere within searchable fields (substring matching)
        - Results are ranked by relevance (exact matches and word-start matches ranked higher)
        - Pagination uses cursor-based navigation with encoded ranking information

        **allSuppliers**

        When `allSuppliers` is provided and set to `true`, it will override the list of `supplierIds` array.

        For example the below payload will search across all suppliers for the term "hammer" and apply the pricing tier with id 123:

        ```
        {
          "search": "hammer",
          "pricingTierId": 123,
          "allSuppliers": true,
          "supplierIds": [
            101,
            102,
            103
          ]
        }
        ```

        To narrow search by specific suppliers, set `allSuppliers` to `false` and provide a list of supplier IDs:

        ```
        {
          "search": "hammer",
          "pricingTierId": 123,
          "allSuppliers": false,
          "supplierIds": [
            101,
            102,
            103
          ]
        }
        ```

        Parameters
        ----------
        search : str
            Search term for pricebook items (minimum 3 characters). Searches across:
            - `name` - Product or item name
            - `productCode` - Product identification code
            - `supplierSku` - Supplier SKU/part number

        page_size : typing.Optional[float]

        sort_order : typing.Optional[PostPricebooksSearchRequestSortOrder]

        page_cursor : typing.Optional[str]

        pricing_tier_id : typing.Optional[float]
            Filter results to show prices for a specific pricing tier ID. If not provided, the default pricing tier will be used

        all_suppliers : typing.Optional[bool]
            When true (default), searches across all supplier pricebooks. When false, only searches pricebooks specified in supplierIds

        supplier_ids : typing.Optional[typing.Sequence[float]]
            Array of supplier/pricebook IDs to limit the search scope. Only used when allSuppliers is false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchPricebooksResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pricebooks.post_pricebooks_search(
            search="hammer",
        )
        """
        _response = self._raw_client.post_pricebooks_search(
            search=search,
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            pricing_tier_id=pricing_tier_id,
            all_suppliers=all_suppliers,
            supplier_ids=supplier_ids,
            request_options=request_options,
        )
        return _response.data

    def get_pricebooks(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricebooksRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPricebooksRequestSortField] = None,
        filter_supplier_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPricebooksResponse:
        """
        Schema for Pricebooks

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricebooksRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPricebooksRequestSortField]

        filter_supplier_name : typing.Optional[str]
            Filter pricebooks by supplier name containing this string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricebooksResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pricebooks.get_pricebooks()
        """
        _response = self._raw_client.get_pricebooks(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_supplier_name=filter_supplier_name,
            request_options=request_options,
        )
        return _response.data

    def get_pricebooks_id(
        self, id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPriceBookByIdResponse:
        """
        Schema for a Pricebook by ID

        Parameters
        ----------
        id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPriceBookByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pricebooks.get_pricebooks_id(
            id=1.1,
        )
        """
        _response = self._raw_client.get_pricebooks_id(id, request_options=request_options)
        return _response.data

    def get_pricebooks_id_pricebook_items(
        self,
        id: float,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricebooksIdPricebookItemsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPricebookItemsResponse:
        """
        Schema for Pricebook Items

        Parameters
        ----------
        id : float

        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricebooksIdPricebookItemsRequestSortOrder]

        page_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricebookItemsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pricebooks.get_pricebooks_id_pricebook_items(
            id=1.1,
        )
        """
        _response = self._raw_client.get_pricebooks_id_pricebook_items(
            id, page_size=page_size, sort_order=sort_order, page_cursor=page_cursor, request_options=request_options
        )
        return _response.data

    def get_pricebooks_id_pricebook_items_pricebook_item_id(
        self,
        id: float,
        pricebook_item_id: float,
        *,
        filter_pricing_tier_id: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPricebookItemByIdResponse:
        """
        Schema for a Pricebook Item by ID

        Parameters
        ----------
        id : float

        pricebook_item_id : float

        filter_pricing_tier_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricebookItemByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pricebooks.get_pricebooks_id_pricebook_items_pricebook_item_id(
            id=1.1,
            pricebook_item_id=1.1,
        )
        """
        _response = self._raw_client.get_pricebooks_id_pricebook_items_pricebook_item_id(
            id, pricebook_item_id, filter_pricing_tier_id=filter_pricing_tier_id, request_options=request_options
        )
        return _response.data


class AsyncPricebooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPricebooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPricebooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPricebooksClient
        """
        return self._raw_client

    async def post_pricebooks_search(
        self,
        *,
        search: str,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[PostPricebooksSearchRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        pricing_tier_id: typing.Optional[float] = OMIT,
        all_suppliers: typing.Optional[bool] = OMIT,
        supplier_ids: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchPricebooksResponse:
        """
        Search for pricebook items across multiple pricebooks

        This endpoint allows you to search for products/items across one or more supplier pricebooks using a text-based search query. The search is performed across item names, product codes, and search values.

        **Search Behavior:**
        - Searches match when the search term appears anywhere within searchable fields (substring matching)
        - Results are ranked by relevance (exact matches and word-start matches ranked higher)
        - Pagination uses cursor-based navigation with encoded ranking information

        **allSuppliers**

        When `allSuppliers` is provided and set to `true`, it will override the list of `supplierIds` array.

        For example the below payload will search across all suppliers for the term "hammer" and apply the pricing tier with id 123:

        ```
        {
          "search": "hammer",
          "pricingTierId": 123,
          "allSuppliers": true,
          "supplierIds": [
            101,
            102,
            103
          ]
        }
        ```

        To narrow search by specific suppliers, set `allSuppliers` to `false` and provide a list of supplier IDs:

        ```
        {
          "search": "hammer",
          "pricingTierId": 123,
          "allSuppliers": false,
          "supplierIds": [
            101,
            102,
            103
          ]
        }
        ```

        Parameters
        ----------
        search : str
            Search term for pricebook items (minimum 3 characters). Searches across:
            - `name` - Product or item name
            - `productCode` - Product identification code
            - `supplierSku` - Supplier SKU/part number

        page_size : typing.Optional[float]

        sort_order : typing.Optional[PostPricebooksSearchRequestSortOrder]

        page_cursor : typing.Optional[str]

        pricing_tier_id : typing.Optional[float]
            Filter results to show prices for a specific pricing tier ID. If not provided, the default pricing tier will be used

        all_suppliers : typing.Optional[bool]
            When true (default), searches across all supplier pricebooks. When false, only searches pricebooks specified in supplierIds

        supplier_ids : typing.Optional[typing.Sequence[float]]
            Array of supplier/pricebook IDs to limit the search scope. Only used when allSuppliers is false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchPricebooksResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pricebooks.post_pricebooks_search(
                search="hammer",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_pricebooks_search(
            search=search,
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            pricing_tier_id=pricing_tier_id,
            all_suppliers=all_suppliers,
            supplier_ids=supplier_ids,
            request_options=request_options,
        )
        return _response.data

    async def get_pricebooks(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricebooksRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPricebooksRequestSortField] = None,
        filter_supplier_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPricebooksResponse:
        """
        Schema for Pricebooks

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricebooksRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPricebooksRequestSortField]

        filter_supplier_name : typing.Optional[str]
            Filter pricebooks by supplier name containing this string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricebooksResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pricebooks.get_pricebooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricebooks(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_supplier_name=filter_supplier_name,
            request_options=request_options,
        )
        return _response.data

    async def get_pricebooks_id(
        self, id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPriceBookByIdResponse:
        """
        Schema for a Pricebook by ID

        Parameters
        ----------
        id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPriceBookByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pricebooks.get_pricebooks_id(
                id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricebooks_id(id, request_options=request_options)
        return _response.data

    async def get_pricebooks_id_pricebook_items(
        self,
        id: float,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricebooksIdPricebookItemsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPricebookItemsResponse:
        """
        Schema for Pricebook Items

        Parameters
        ----------
        id : float

        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricebooksIdPricebookItemsRequestSortOrder]

        page_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricebookItemsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pricebooks.get_pricebooks_id_pricebook_items(
                id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricebooks_id_pricebook_items(
            id, page_size=page_size, sort_order=sort_order, page_cursor=page_cursor, request_options=request_options
        )
        return _response.data

    async def get_pricebooks_id_pricebook_items_pricebook_item_id(
        self,
        id: float,
        pricebook_item_id: float,
        *,
        filter_pricing_tier_id: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPricebookItemByIdResponse:
        """
        Schema for a Pricebook Item by ID

        Parameters
        ----------
        id : float

        pricebook_item_id : float

        filter_pricing_tier_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricebookItemByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pricebooks.get_pricebooks_id_pricebook_items_pricebook_item_id(
                id=1.1,
                pricebook_item_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricebooks_id_pricebook_items_pricebook_item_id(
            id, pricebook_item_id, filter_pricing_tier_id=filter_pricing_tier_id, request_options=request_options
        )
        return _response.data
