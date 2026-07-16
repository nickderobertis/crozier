

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawComparisonShoppingPagesClient, RawComparisonShoppingPagesClient


class ComparisonShoppingPagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawComparisonShoppingPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawComparisonShoppingPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawComparisonShoppingPagesClient
        """
        return self._raw_client

    def returns_a_set_of_comparison_shopping_pages_based_on_the_current_params(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a set of comparison shopping pages based on the current params

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.comparison_shopping_pages.returns_a_set_of_comparison_shopping_pages_based_on_the_current_params()
        """
        _response = self._raw_client.returns_a_set_of_comparison_shopping_pages_based_on_the_current_params(
            request_options=request_options
        )
        return _response.data

    def show_comparison_shopping_page(
        self,
        *,
        id: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Show comparison shopping page

        Parameters
        ----------
        id : typing.Optional[str]
            ID of the comparison shopping page

        slug : typing.Optional[str]
            Slug of the comparison shopping page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.comparison_shopping_pages.show_comparison_shopping_page()
        """
        _response = self._raw_client.show_comparison_shopping_page(id=id, slug=slug, request_options=request_options)
        return _response.data

    def get_comparison_shopping_pages_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.comparison_shopping_pages.get_comparison_shopping_pages_id(
            id="id",
        )
        """
        _response = self._raw_client.get_comparison_shopping_pages_id(id, request_options=request_options)
        return _response.data

    def return_new_or_used_listings_for_a_comparison_shopping_page(
        self,
        id: str,
        *,
        condition: str,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Return new or used listings for a comparison shopping page

        Parameters
        ----------
        id : str

        condition : str
            Condition of the listing

        page : typing.Optional[int]

        per_page : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.comparison_shopping_pages.return_new_or_used_listings_for_a_comparison_shopping_page(
            id="id",
            condition="condition",
        )
        """
        _response = self._raw_client.return_new_or_used_listings_for_a_comparison_shopping_page(
            id, condition=condition, page=page, per_page=per_page, offset=offset, request_options=request_options
        )
        return _response.data

    def view_reviews_of_a_comparison_shopping_page(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        View reviews of a comparison shopping page

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.comparison_shopping_pages.view_reviews_of_a_comparison_shopping_page(
            id="id",
        )
        """
        _response = self._raw_client.view_reviews_of_a_comparison_shopping_page(id, request_options=request_options)
        return _response.data


class AsyncComparisonShoppingPagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawComparisonShoppingPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawComparisonShoppingPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawComparisonShoppingPagesClient
        """
        return self._raw_client

    async def returns_a_set_of_comparison_shopping_pages_based_on_the_current_params(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a set of comparison shopping pages based on the current params

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.comparison_shopping_pages.returns_a_set_of_comparison_shopping_pages_based_on_the_current_params()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_set_of_comparison_shopping_pages_based_on_the_current_params(
            request_options=request_options
        )
        return _response.data

    async def show_comparison_shopping_page(
        self,
        *,
        id: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Show comparison shopping page

        Parameters
        ----------
        id : typing.Optional[str]
            ID of the comparison shopping page

        slug : typing.Optional[str]
            Slug of the comparison shopping page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.comparison_shopping_pages.show_comparison_shopping_page()


        asyncio.run(main())
        """
        _response = await self._raw_client.show_comparison_shopping_page(
            id=id, slug=slug, request_options=request_options
        )
        return _response.data

    async def get_comparison_shopping_pages_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.comparison_shopping_pages.get_comparison_shopping_pages_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_comparison_shopping_pages_id(id, request_options=request_options)
        return _response.data

    async def return_new_or_used_listings_for_a_comparison_shopping_page(
        self,
        id: str,
        *,
        condition: str,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Return new or used listings for a comparison shopping page

        Parameters
        ----------
        id : str

        condition : str
            Condition of the listing

        page : typing.Optional[int]

        per_page : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.comparison_shopping_pages.return_new_or_used_listings_for_a_comparison_shopping_page(
                id="id",
                condition="condition",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_new_or_used_listings_for_a_comparison_shopping_page(
            id, condition=condition, page=page, per_page=per_page, offset=offset, request_options=request_options
        )
        return _response.data

    async def view_reviews_of_a_comparison_shopping_page(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        View reviews of a comparison shopping page

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.comparison_shopping_pages.view_reviews_of_a_comparison_shopping_page(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.view_reviews_of_a_comparison_shopping_page(
            id, request_options=request_options
        )
        return _response.data
