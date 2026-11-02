

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawScansClient, RawScansClient
from .types.file_scan_request_drawer import FileScanRequestDrawer


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

    def file_scan(
        self, *, scan: core.File, drawer: FileScanRequestDrawer, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scan : core.File
            See core.File for more documentation

        drawer : FileScanRequestDrawer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scans.file_scan(
            drawer="drawer",
        )
        """
        _response = self._raw_client.file_scan(scan=scan, drawer=drawer, request_options=request_options)
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

    async def file_scan(
        self, *, scan: core.File, drawer: FileScanRequestDrawer, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scan : core.File
            See core.File for more documentation

        drawer : FileScanRequestDrawer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.scans.file_scan(
                drawer="drawer",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.file_scan(scan=scan, drawer=drawer, request_options=request_options)
        return _response.data
