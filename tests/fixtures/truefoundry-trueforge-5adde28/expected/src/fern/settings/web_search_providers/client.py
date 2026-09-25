

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.get_web_search_provider_response import GetWebSearchProviderResponse
from ...types.web_search_provider_manifest import WebSearchProviderManifest
from .raw_client import AsyncRawWebSearchProvidersClient, RawWebSearchProvidersClient


OMIT = typing.cast(typing.Any, ...)


class WebSearchProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebSearchProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebSearchProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebSearchProvidersClient
        """
        return self._raw_client

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetWebSearchProviderResponse:
        """
        The configured provider for this tenant. `auth.api_key` is redacted when present.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebSearchProviderResponse
            The configured web search provider.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.settings.web_search_providers.get()
        """
        _response = self._raw_client.get(request_options=request_options)
        return _response.data

    def create_or_update(
        self, *, manifest: WebSearchProviderManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebSearchProviderResponse:
        """
        Upserts the single web search provider for this tenant. `auth.api_key`: real value sets/rotates; redacted keeps existing (400 if none).

        Parameters
        ----------
        manifest : WebSearchProviderManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebSearchProviderResponse
            The saved provider.

        Examples
        --------
        from fern import (
            FernApi,
            ParallelWebSearchProviderAuth,
            WebSearchProviderManifest,
            WebSearchProviderManifestType,
        )

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.settings.web_search_providers.create_or_update(
            manifest=WebSearchProviderManifest(
                auth=ParallelWebSearchProviderAuth(
                    api_key="api_key",
                ),
                type=WebSearchProviderManifestType.PARALLEL,
            ),
        )
        """
        _response = self._raw_client.create_or_update(manifest=manifest, request_options=request_options)
        return _response.data


class AsyncWebSearchProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebSearchProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebSearchProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebSearchProvidersClient
        """
        return self._raw_client

    async def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetWebSearchProviderResponse:
        """
        The configured provider for this tenant. `auth.api_key` is redacted when present.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebSearchProviderResponse
            The configured web search provider.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.settings.web_search_providers.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(request_options=request_options)
        return _response.data

    async def create_or_update(
        self, *, manifest: WebSearchProviderManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebSearchProviderResponse:
        """
        Upserts the single web search provider for this tenant. `auth.api_key`: real value sets/rotates; redacted keeps existing (400 if none).

        Parameters
        ----------
        manifest : WebSearchProviderManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebSearchProviderResponse
            The saved provider.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ParallelWebSearchProviderAuth,
            WebSearchProviderManifest,
            WebSearchProviderManifestType,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.settings.web_search_providers.create_or_update(
                manifest=WebSearchProviderManifest(
                    auth=ParallelWebSearchProviderAuth(
                        api_key="api_key",
                    ),
                    type=WebSearchProviderManifestType.PARALLEL,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update(manifest=manifest, request_options=request_options)
        return _response.data
