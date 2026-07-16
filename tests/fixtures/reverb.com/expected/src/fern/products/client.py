

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawProductsClient, RawProductsClient


OMIT = typing.cast(typing.Any, ...)


class ProductsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProductsClient
        """
        return self._raw_client

    def view_a_review(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        View a review

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
        client.products.view_a_review(
            id="id",
        )
        """
        _response = self._raw_client.view_a_review(id, request_options=request_options)
        return _response.data

    def update_a_review(
        self,
        id: str,
        *,
        body: typing.Optional[str] = OMIT,
        rating: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a review

        Parameters
        ----------
        id : str

        body : typing.Optional[str]
            Content of the review

        rating : typing.Optional[int]
            Rating from 1 to 5

        title : typing.Optional[str]
            Title for the review

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
        client.products.update_a_review(
            id="id",
        )
        """
        _response = self._raw_client.update_a_review(
            id, body=body, rating=rating, title=title, request_options=request_options
        )
        return _response.data

    def view_reviews_of_a_comparison_shopping_page(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        View reviews of a comparison shopping page

        Parameters
        ----------
        slug : str

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
        client.products.view_reviews_of_a_comparison_shopping_page(
            slug="slug",
        )
        """
        _response = self._raw_client.view_reviews_of_a_comparison_shopping_page(slug, request_options=request_options)
        return _response.data

    def create_a_review_for_a_product(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create a review for a product

        Parameters
        ----------
        slug : str

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
        client.products.create_a_review_for_a_product(
            slug="slug",
        )
        """
        _response = self._raw_client.create_a_review_for_a_product(slug, request_options=request_options)
        return _response.data


class AsyncProductsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProductsClient
        """
        return self._raw_client

    async def view_a_review(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        View a review

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
            await client.products.view_a_review(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.view_a_review(id, request_options=request_options)
        return _response.data

    async def update_a_review(
        self,
        id: str,
        *,
        body: typing.Optional[str] = OMIT,
        rating: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a review

        Parameters
        ----------
        id : str

        body : typing.Optional[str]
            Content of the review

        rating : typing.Optional[int]
            Rating from 1 to 5

        title : typing.Optional[str]
            Title for the review

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
            await client.products.update_a_review(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_review(
            id, body=body, rating=rating, title=title, request_options=request_options
        )
        return _response.data

    async def view_reviews_of_a_comparison_shopping_page(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        View reviews of a comparison shopping page

        Parameters
        ----------
        slug : str

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
            await client.products.view_reviews_of_a_comparison_shopping_page(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.view_reviews_of_a_comparison_shopping_page(
            slug, request_options=request_options
        )
        return _response.data

    async def create_a_review_for_a_product(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create a review for a product

        Parameters
        ----------
        slug : str

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
            await client.products.create_a_review_for_a_product(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_review_for_a_product(slug, request_options=request_options)
        return _response.data
