

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_categories_response import GetCategoriesResponse
from ..types.get_category_response import GetCategoryResponse
from ..types.get_listings_response import GetListingsResponse
from .raw_client import AsyncRawCategoryClient, RawCategoryClient


class CategoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCategoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCategoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCategoryClient
        """
        return self._raw_client

    def categories_all(
        self,
        ecosystem_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCategoriesResponse:
        """
        List categories

        Parameters
        ----------
        ecosystem_id : str

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCategoriesResponse
            Categories

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.category.categories_all(
            ecosystem_id="ecosystem_id",
        )
        """
        _response = self._raw_client.categories_all(
            ecosystem_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    def categories_one(
        self, ecosystem_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCategoryResponse:
        """
        Get category

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCategoryResponse
            Category

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.category.categories_one(
            ecosystem_id="ecosystem_id",
            id="id",
        )
        """
        _response = self._raw_client.categories_one(ecosystem_id, id, request_options=request_options)
        return _response.data

    def listings_all(
        self,
        ecosystem_id: str,
        id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetListingsResponse:
        """
        List category listings

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetListingsResponse
            Listings

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.category.listings_all(
            ecosystem_id="ecosystem_id",
            id="id",
        )
        """
        _response = self._raw_client.listings_all(
            ecosystem_id, id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data


class AsyncCategoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCategoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCategoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCategoryClient
        """
        return self._raw_client

    async def categories_all(
        self,
        ecosystem_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCategoriesResponse:
        """
        List categories

        Parameters
        ----------
        ecosystem_id : str

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCategoriesResponse
            Categories

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.category.categories_all(
                ecosystem_id="ecosystem_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.categories_all(
            ecosystem_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def categories_one(
        self, ecosystem_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCategoryResponse:
        """
        Get category

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCategoryResponse
            Category

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.category.categories_one(
                ecosystem_id="ecosystem_id",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.categories_one(ecosystem_id, id, request_options=request_options)
        return _response.data

    async def listings_all(
        self,
        ecosystem_id: str,
        id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetListingsResponse:
        """
        List category listings

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetListingsResponse
            Listings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.category.listings_all(
                ecosystem_id="ecosystem_id",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listings_all(
            ecosystem_id, id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data
