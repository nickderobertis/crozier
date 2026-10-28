

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCatalogFilterExtensionClient, RawCatalogFilterExtensionClient


class CatalogFilterExtensionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogFilterExtensionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCatalogFilterExtensionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogFilterExtensionClient
        """
        return self._raw_client

    def queryables(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Endpoint.

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
        client.catalog_filter_extension.queryables()
        """
        _response = self._raw_client.queryables(request_options=request_options)
        return _response.data

    def collection_queryables(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_filter_extension.collection_queryables(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.collection_queryables(collection_id, request_options=request_options)
        return _response.data


class AsyncCatalogFilterExtensionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogFilterExtensionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCatalogFilterExtensionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogFilterExtensionClient
        """
        return self._raw_client

    async def queryables(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Endpoint.

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
            await client.catalog_filter_extension.queryables()


        asyncio.run(main())
        """
        _response = await self._raw_client.queryables(request_options=request_options)
        return _response.data

    async def collection_queryables(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
            await client.catalog_filter_extension.collection_queryables(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_queryables(collection_id, request_options=request_options)
        return _response.data
