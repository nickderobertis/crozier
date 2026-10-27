

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sortables_schema import SortablesSchema
from .raw_client import AsyncRawSortExtensionClient, RawSortExtensionClient


class SortExtensionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSortExtensionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSortExtensionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSortExtensionClient
        """
        return self._raw_client

    def sortables(self, *, request_options: typing.Optional[RequestOptions] = None) -> SortablesSchema:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SortablesSchema
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.sort_extension.sortables()
        """
        _response = self._raw_client.sortables(request_options=request_options)
        return _response.data

    def collection_sortables(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SortablesSchema:
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
        SortablesSchema
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.sort_extension.collection_sortables(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.collection_sortables(collection_id, request_options=request_options)
        return _response.data

    def collections_catalog_sortables(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SortablesSchema:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SortablesSchema
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.sort_extension.collections_catalog_sortables()
        """
        _response = self._raw_client.collections_catalog_sortables(request_options=request_options)
        return _response.data


class AsyncSortExtensionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSortExtensionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSortExtensionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSortExtensionClient
        """
        return self._raw_client

    async def sortables(self, *, request_options: typing.Optional[RequestOptions] = None) -> SortablesSchema:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SortablesSchema
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
            await client.sort_extension.sortables()


        asyncio.run(main())
        """
        _response = await self._raw_client.sortables(request_options=request_options)
        return _response.data

    async def collection_sortables(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SortablesSchema:
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
        SortablesSchema
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
            await client.sort_extension.collection_sortables(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_sortables(collection_id, request_options=request_options)
        return _response.data

    async def collections_catalog_sortables(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SortablesSchema:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SortablesSchema
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
            await client.sort_extension.collections_catalog_sortables()


        asyncio.run(main())
        """
        _response = await self._raw_client.collections_catalog_sortables(request_options=request_options)
        return _response.data
