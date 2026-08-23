

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
        The landing page provides links to the:
          * The OpenAPI-definition (no fixed path),
          * The Conformance statements (path /conformance),
          * The processes metadata (path /processes),
          * The endpoint for job monitoring (path /jobs).

        For more information, see [OGC API — Processes — Part 1 Section 7.2](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_landing_page).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Capabilities
            The landing page provides links to the API definition
            (link relations `service-desc` and `service-doc`),
            the Conformance declaration (path `/conformance`,
            link relation `http://www.opengis.net/def/rel/ogc/1.0/conformance`),
            and to other resources.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
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
        The landing page provides links to the:
          * The OpenAPI-definition (no fixed path),
          * The Conformance statements (path /conformance),
          * The processes metadata (path /processes),
          * The endpoint for job monitoring (path /jobs).

        For more information, see [OGC API — Processes — Part 1 Section 7.2](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_landing_page).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Capabilities
            The landing page provides links to the API definition
            (link relations `service-desc` and `service-doc`),
            the Conformance declaration (path `/conformance`,
            link relation `http://www.opengis.net/def/rel/ogc/1.0/conformance`),
            and to other resources.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.capabilities.get_capabilities()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_capabilities(request_options=request_options)
        return _response.data
