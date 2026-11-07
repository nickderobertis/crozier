

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.provider_discovery import ProviderDiscovery
from .raw_client import AsyncRawProviderDiscoveryClient, RawProviderDiscoveryClient


OMIT = typing.cast(typing.Any, ...)


class ProviderDiscoveryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProviderDiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProviderDiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProviderDiscoveryClient
        """
        return self._raw_client

    def create_provider_discovery(
        self, *, docker_image: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderDiscovery:
        """
        Parameters
        ----------
        docker_image : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderDiscovery
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_discovery.create_provider_discovery(
            docker_image="docker_image",
        )
        """
        _response = self._raw_client.create_provider_discovery(
            docker_image=docker_image, request_options=request_options
        )
        return _response.data

    def get_provider_discovery(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderDiscovery:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderDiscovery
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_discovery.get_provider_discovery(
            id="id",
        )
        """
        _response = self._raw_client.get_provider_discovery(id, request_options=request_options)
        return _response.data


class AsyncProviderDiscoveryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProviderDiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProviderDiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProviderDiscoveryClient
        """
        return self._raw_client

    async def create_provider_discovery(
        self, *, docker_image: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderDiscovery:
        """
        Parameters
        ----------
        docker_image : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderDiscovery
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_discovery.create_provider_discovery(
                docker_image="docker_image",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_provider_discovery(
            docker_image=docker_image, request_options=request_options
        )
        return _response.data

    async def get_provider_discovery(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderDiscovery:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderDiscovery
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_discovery.get_provider_discovery(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_provider_discovery(id, request_options=request_options)
        return _response.data
