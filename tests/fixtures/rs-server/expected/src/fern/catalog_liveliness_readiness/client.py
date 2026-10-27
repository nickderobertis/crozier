

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.health_check import HealthCheck
from .raw_client import AsyncRawCatalogLivelinessReadinessClient, RawCatalogLivelinessReadinessClient


class CatalogLivelinessReadinessClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogLivelinessReadinessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCatalogLivelinessReadinessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogLivelinessReadinessClient
        """
        return self._raw_client

    def ping_catalog_mgmt_ping_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Liveliness probe.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_liveliness_readiness.ping_catalog_mgmt_ping_get()
        """
        _response = self._raw_client.ping_catalog_mgmt_ping_get(request_options=request_options)
        return _response.data

    def health_catalog_mgmt_health_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthCheck:
        """
        PgSTAC HealthCheck.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheck
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_liveliness_readiness.health_catalog_mgmt_health_get()
        """
        _response = self._raw_client.health_catalog_mgmt_health_get(request_options=request_options)
        return _response.data


class AsyncCatalogLivelinessReadinessClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogLivelinessReadinessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCatalogLivelinessReadinessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogLivelinessReadinessClient
        """
        return self._raw_client

    async def ping_catalog_mgmt_ping_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Liveliness probe.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.catalog_liveliness_readiness.ping_catalog_mgmt_ping_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.ping_catalog_mgmt_ping_get(request_options=request_options)
        return _response.data

    async def health_catalog_mgmt_health_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthCheck:
        """
        PgSTAC HealthCheck.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheck
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
            await client.catalog_liveliness_readiness.health_catalog_mgmt_health_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.health_catalog_mgmt_health_get(request_options=request_options)
        return _response.data
