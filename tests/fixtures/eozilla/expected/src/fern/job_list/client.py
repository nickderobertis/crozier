

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_list import JobList
from .raw_client import AsyncRawJobListClient, RawJobListClient


class JobListClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobListClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobListClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobListClient
        """
        return self._raw_client

    def get_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> JobList:
        """
        List available jobs.

        For more information, see [OGC API — Processes — Part 1 Section 11](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_job_list).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobList
            A list of jobs for this process.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.job_list.get_jobs()
        """
        _response = self._raw_client.get_jobs(request_options=request_options)
        return _response.data


class AsyncJobListClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobListClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobListClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobListClient
        """
        return self._raw_client

    async def get_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> JobList:
        """
        List available jobs.

        For more information, see [OGC API — Processes — Part 1 Section 11](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_job_list).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobList
            A list of jobs for this process.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.job_list.get_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs(request_options=request_options)
        return _response.data
