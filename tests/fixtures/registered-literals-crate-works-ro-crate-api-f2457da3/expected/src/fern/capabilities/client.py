

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.capabilities import Capabilities
from .raw_client import AsyncRawCapabilitiesClient, RawCapabilitiesClient


class CapabilitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCapabilitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCapabilitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCapabilitiesClient
        """
        return self._raw_client

    def get_capabilities(self, *, request_options: typing.Optional[RequestOptions] = None) -> Capabilities:
        """
        Declare what this implementation supports — the spec version it targets, the extensions it implements, and the search filters and facets it provides. Every conformant implementation MUST provide this endpoint so that clients can feature-detect rather than relying on per-archive configuration or probing.

        See the [Capabilities guide](https://ro-crate-api.crate-works.org/docs/getting-started/capabilities) for how clients should use this endpoint, and the [Extensions guide](https://ro-crate-api.crate-works.org/docs/extensions) for how extensions are registered.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Capabilities
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.capabilities.get_capabilities()
        """
        _response = self._raw_client.get_capabilities(request_options=request_options)
        return _response.data


class AsyncCapabilitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCapabilitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCapabilitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCapabilitiesClient
        """
        return self._raw_client

    async def get_capabilities(self, *, request_options: typing.Optional[RequestOptions] = None) -> Capabilities:
        """
        Declare what this implementation supports — the spec version it targets, the extensions it implements, and the search filters and facets it provides. Every conformant implementation MUST provide this endpoint so that clients can feature-detect rather than relying on per-archive configuration or probing.

        See the [Capabilities guide](https://ro-crate-api.crate-works.org/docs/getting-started/capabilities) for how clients should use this endpoint, and the [Extensions guide](https://ro-crate-api.crate-works.org/docs/extensions) for how extensions are registered.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Capabilities
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.capabilities.get_capabilities()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_capabilities(request_options=request_options)
        return _response.data
