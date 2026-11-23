

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.portal import Portal
from ..types.scan_response import ScanResponse
from .raw_client import AsyncRawScansClient, RawScansClient


OMIT = typing.cast(typing.Any, ...)


class ScansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScansClient
        """
        return self._raw_client

    def start_scan(self, *, text: str, request_options: typing.Optional[RequestOptions] = None) -> ScanResponse:
        """
        Parameters
        ----------
        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScanResponse
            The finished scan.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.scans.start_scan(
            text="text",
        )
        """
        _response = self._raw_client.start_scan(text=text, request_options=request_options)
        return _response.data

    def get_portal(self, portal_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Portal:
        """
        Parameters
        ----------
        portal_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Portal
            The portal.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.scans.get_portal(
            portal_id="portalId",
        )
        """
        _response = self._raw_client.get_portal(portal_id, request_options=request_options)
        return _response.data


class AsyncScansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScansClient
        """
        return self._raw_client

    async def start_scan(self, *, text: str, request_options: typing.Optional[RequestOptions] = None) -> ScanResponse:
        """
        Parameters
        ----------
        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScanResponse
            The finished scan.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.scans.start_scan(
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_scan(text=text, request_options=request_options)
        return _response.data

    async def get_portal(self, portal_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Portal:
        """
        Parameters
        ----------
        portal_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Portal
            The portal.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.scans.get_portal(
                portal_id="portalId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_portal(portal_id, request_options=request_options)
        return _response.data
