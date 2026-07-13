

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTrendingClient, RawTrendingClient
from .types.trending_get_trending_categories_response import TrendingGetTrendingCategoriesResponse
from .types.trending_get_trending_category_response import TrendingGetTrendingCategoryResponse
from .types.trending_get_trending_entry_detail_response import TrendingGetTrendingEntryDetailResponse


class TrendingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTrendingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTrendingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTrendingClient
        """
        return self._raw_client

    def gettrendingcategories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrendingGetTrendingCategoriesResponse:
        """
        Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrendingGetTrendingCategoriesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.trending.gettrendingcategories()
        """
        _response = self._raw_client.gettrendingcategories(request_options=request_options)
        return _response.data

    def gettrendingcategory(
        self, category_id: str, page_number: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrendingGetTrendingCategoryResponse:
        """
        Returns paginated lists of trending items for a category.

        Parameters
        ----------
        category_id : str
            The ID of the category for whom you want additional results.

        page_number : int
            The page # of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrendingGetTrendingCategoryResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.trending.gettrendingcategory(
            category_id="categoryId",
            page_number=1,
        )
        """
        _response = self._raw_client.gettrendingcategory(category_id, page_number, request_options=request_options)
        return _response.data

    def gettrendingentrydetail(
        self, trending_entry_type: int, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrendingGetTrendingEntryDetailResponse:
        """
        Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

        Parameters
        ----------
        trending_entry_type : int
            The type of entity to be returned.

        identifier : str
            The identifier for the entity to be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrendingGetTrendingEntryDetailResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.trending.gettrendingentrydetail(
            trending_entry_type=1,
            identifier="identifier",
        )
        """
        _response = self._raw_client.gettrendingentrydetail(
            trending_entry_type, identifier, request_options=request_options
        )
        return _response.data


class AsyncTrendingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTrendingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTrendingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTrendingClient
        """
        return self._raw_client

    async def gettrendingcategories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrendingGetTrendingCategoriesResponse:
        """
        Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrendingGetTrendingCategoriesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.trending.gettrendingcategories()


        asyncio.run(main())
        """
        _response = await self._raw_client.gettrendingcategories(request_options=request_options)
        return _response.data

    async def gettrendingcategory(
        self, category_id: str, page_number: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrendingGetTrendingCategoryResponse:
        """
        Returns paginated lists of trending items for a category.

        Parameters
        ----------
        category_id : str
            The ID of the category for whom you want additional results.

        page_number : int
            The page # of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrendingGetTrendingCategoryResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.trending.gettrendingcategory(
                category_id="categoryId",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettrendingcategory(
            category_id, page_number, request_options=request_options
        )
        return _response.data

    async def gettrendingentrydetail(
        self, trending_entry_type: int, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrendingGetTrendingEntryDetailResponse:
        """
        Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

        Parameters
        ----------
        trending_entry_type : int
            The type of entity to be returned.

        identifier : str
            The identifier for the entity to be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrendingGetTrendingEntryDetailResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.trending.gettrendingentrydetail(
                trending_entry_type=1,
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettrendingentrydetail(
            trending_entry_type, identifier, request_options=request_options
        )
        return _response.data
