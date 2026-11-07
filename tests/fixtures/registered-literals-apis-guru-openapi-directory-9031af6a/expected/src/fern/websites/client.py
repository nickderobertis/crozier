

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWebsitesClient, RawWebsitesClient
from .types.get_tracking_snippet_response import GetTrackingSnippetResponse


class WebsitesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebsitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebsitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebsitesClient
        """
        return self._raw_client

    def get_tracking_snippet(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTrackingSnippetResponse:
        """
        Endpoint used to get a snippet for a website.

        Parameters
        ----------
        domain : str
            The domain you want to receive a snippet for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTrackingSnippetResponse
            Snippet

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.websites.get_tracking_snippet(
            domain="domain",
        )
        """
        _response = self._raw_client.get_tracking_snippet(domain=domain, request_options=request_options)
        return _response.data


class AsyncWebsitesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebsitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebsitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebsitesClient
        """
        return self._raw_client

    async def get_tracking_snippet(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTrackingSnippetResponse:
        """
        Endpoint used to get a snippet for a website.

        Parameters
        ----------
        domain : str
            The domain you want to receive a snippet for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTrackingSnippetResponse
            Snippet

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.websites.get_tracking_snippet(
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tracking_snippet(domain=domain, request_options=request_options)
        return _response.data
