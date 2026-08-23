

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.process_list import ProcessList
from .raw_client import AsyncRawProcessListClient, RawProcessListClient


class ProcessListClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProcessListClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProcessListClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProcessListClient
        """
        return self._raw_client

    def get_processes(self, *, request_options: typing.Optional[RequestOptions] = None) -> ProcessList:
        """
        The list of processes contains a summary of each process the OGC API - Processes offers, including the link to a more detailed description of the process.

        For more information, see [OGC API — Processes — Part 1 Section 7.9](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_list).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessList
            Information about the available processes

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.process_list.get_processes()
        """
        _response = self._raw_client.get_processes(request_options=request_options)
        return _response.data


class AsyncProcessListClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProcessListClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProcessListClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProcessListClient
        """
        return self._raw_client

    async def get_processes(self, *, request_options: typing.Optional[RequestOptions] = None) -> ProcessList:
        """
        The list of processes contains a summary of each process the OGC API - Processes offers, including the link to a more detailed description of the process.

        For more information, see [OGC API — Processes — Part 1 Section 7.9](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_list).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessList
            Information about the available processes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.process_list.get_processes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_processes(request_options=request_options)
        return _response.data
