

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_info import JobInfo
from .raw_client import AsyncRawJobStatusClient, RawJobStatusClient


class JobStatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobStatusClient
        """
        return self._raw_client

    def get_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> JobInfo:
        """
        Show the status of a job.

        For more information, see [OGC API — Processes — Part 1 Section 7.12](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_retrieve_status_info).

        Parameters
        ----------
        job_id : str
            Local identifier of a job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfo
            The status of a job.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.job_status.get_job(
            job_id="jobId",
        )
        """
        _response = self._raw_client.get_job(job_id, request_options=request_options)
        return _response.data


class AsyncJobStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobStatusClient
        """
        return self._raw_client

    async def get_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> JobInfo:
        """
        Show the status of a job.

        For more information, see [OGC API — Processes — Part 1 Section 7.12](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_retrieve_status_info).

        Parameters
        ----------
        job_id : str
            Local identifier of a job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfo
            The status of a job.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.job_status.get_job(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job(job_id, request_options=request_options)
        return _response.data
