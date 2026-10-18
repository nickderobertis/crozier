

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCollectionsClient, RawCollectionsClient


class CollectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionsClient
        """
        return self._raw_client

    def get_collection(
        self, *, filter_url_slug: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get collection

        Parameters
        ----------
        filter_url_slug : typing.Optional[str]

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
        client.collections.get_collection(
            filter_url_slug="mechanical-keyboards",
        )
        """
        _response = self._raw_client.get_collection(filter_url_slug=filter_url_slug, request_options=request_options)
        return _response.data

    def list_collections(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List collections

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
        client.collections.list_collections()
        """
        _response = self._raw_client.list_collections(request_options=request_options)
        return _response.data

    def get_collection_default_url(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get collection default url

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
        client.collections.get_collection_default_url()
        """
        _response = self._raw_client.get_collection_default_url(request_options=request_options)
        return _response.data

    def get_collection_default_url_relation(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get collection default url relation

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
        client.collections.get_collection_default_url_relation()
        """
        _response = self._raw_client.get_collection_default_url_relation(request_options=request_options)
        return _response.data

    def list_collection_products(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List collection products

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
        client.collections.list_collection_products()
        """
        _response = self._raw_client.list_collection_products(request_options=request_options)
        return _response.data

    def list_collection_products_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List collection products relationships

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
        client.collections.list_collection_products_relationships()
        """
        _response = self._raw_client.list_collection_products_relationships(request_options=request_options)
        return _response.data


class AsyncCollectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionsClient
        """
        return self._raw_client

    async def get_collection(
        self, *, filter_url_slug: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get collection

        Parameters
        ----------
        filter_url_slug : typing.Optional[str]

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
            await client.collections.get_collection(
                filter_url_slug="mechanical-keyboards",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection(
            filter_url_slug=filter_url_slug, request_options=request_options
        )
        return _response.data

    async def list_collections(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List collections

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
            await client.collections.list_collections()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_collections(request_options=request_options)
        return _response.data

    async def get_collection_default_url(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get collection default url

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
            await client.collections.get_collection_default_url()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection_default_url(request_options=request_options)
        return _response.data

    async def get_collection_default_url_relation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get collection default url relation

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
            await client.collections.get_collection_default_url_relation()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection_default_url_relation(request_options=request_options)
        return _response.data

    async def list_collection_products(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List collection products

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
            await client.collections.list_collection_products()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_collection_products(request_options=request_options)
        return _response.data

    async def list_collection_products_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List collection products relationships

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
            await client.collections.list_collection_products_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_collection_products_relationships(request_options=request_options)
        return _response.data
