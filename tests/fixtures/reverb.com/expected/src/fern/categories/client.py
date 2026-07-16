

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCategoriesClient, RawCategoriesClient


class CategoriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCategoriesClient
        """
        return self._raw_client

    def list_of_supported_product_categories(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List of supported product categories

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
        client.categories.list_of_supported_product_categories()
        """
        _response = self._raw_client.list_of_supported_product_categories(request_options=request_options)
        return _response.data

    def get_categories_flat(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
        client.categories.get_categories_flat()
        """
        _response = self._raw_client.get_categories_flat(request_options=request_options)
        return _response.data

    def full_taxonomy_tree_of_categories_including_middle_categories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Full taxonomy tree of categories including middle categories

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
        client.categories.full_taxonomy_tree_of_categories_including_middle_categories()
        """
        _response = self._raw_client.full_taxonomy_tree_of_categories_including_middle_categories(
            request_options=request_options
        )
        return _response.data

    def get_subcategory_details(
        self, product_type: str, category: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get subcategory details

        Parameters
        ----------
        product_type : str

        category : str

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
        client.categories.get_subcategory_details(
            product_type="product_type",
            category="category",
        )
        """
        _response = self._raw_client.get_subcategory_details(product_type, category, request_options=request_options)
        return _response.data

    def get_category_details(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get category details

        Parameters
        ----------
        uuid_ : str

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
        client.categories.get_category_details(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_category_details(uuid_, request_options=request_options)
        return _response.data


class AsyncCategoriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCategoriesClient
        """
        return self._raw_client

    async def list_of_supported_product_categories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List of supported product categories

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
            await client.categories.list_of_supported_product_categories()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_of_supported_product_categories(request_options=request_options)
        return _response.data

    async def get_categories_flat(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
            await client.categories.get_categories_flat()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_categories_flat(request_options=request_options)
        return _response.data

    async def full_taxonomy_tree_of_categories_including_middle_categories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Full taxonomy tree of categories including middle categories

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
            await client.categories.full_taxonomy_tree_of_categories_including_middle_categories()


        asyncio.run(main())
        """
        _response = await self._raw_client.full_taxonomy_tree_of_categories_including_middle_categories(
            request_options=request_options
        )
        return _response.data

    async def get_subcategory_details(
        self, product_type: str, category: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get subcategory details

        Parameters
        ----------
        product_type : str

        category : str

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
            await client.categories.get_subcategory_details(
                product_type="product_type",
                category="category",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subcategory_details(
            product_type, category, request_options=request_options
        )
        return _response.data

    async def get_category_details(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get category details

        Parameters
        ----------
        uuid_ : str

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
            await client.categories.get_category_details(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_category_details(uuid_, request_options=request_options)
        return _response.data
