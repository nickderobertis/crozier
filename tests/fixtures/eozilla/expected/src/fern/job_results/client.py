

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_results import JobResults
from .raw_client import AsyncRawJobResultsClient, RawJobResultsClient


class JobResultsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobResultsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobResultsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobResultsClient
        """
        return self._raw_client

    def get_job_results(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> JobResults:
        """
        List available results of a job. In case of a failure, list errors instead.

        For more information, see [OGC API — Processes — Part 1 Section 7.13](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_retrieve_job_results).

        Parameters
        ----------
        job_id : str
            Local identifier of a job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResults
            The results of a job.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.job_results.get_job_results(
            job_id="jobId",
        )
        """
        _response = self._raw_client.get_job_results(job_id, request_options=request_options)
        return _response.data


class AsyncJobResultsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobResultsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobResultsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobResultsClient
        """
        return self._raw_client

    async def get_job_results(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobResults:
        """
        List available results of a job. In case of a failure, list errors instead.

        For more information, see [OGC API — Processes — Part 1 Section 7.13](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_retrieve_job_results).

        Parameters
        ----------
        job_id : str
            Local identifier of a job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResults
            The results of a job.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.job_results.get_job_results(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_results(job_id, request_options=request_options)
        return _response.data
