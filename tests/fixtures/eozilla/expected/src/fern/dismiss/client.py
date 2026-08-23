

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_info import JobInfo
from .raw_client import AsyncRawDismissClient, RawDismissClient


class DismissClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDismissClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDismissClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDismissClient
        """
        return self._raw_client

    def job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> JobInfo:
        """
        Cancel a job execution and removes it from the jobs list.

        For more information, see [OGC API — Processes — Part 1 Section 13](https://docs.ogc.org/is/18-062r2/18-062r2.html#Dismiss).

        Parameters
        ----------
        job_id : str
            Local identifier of a job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfo
            Information about the job.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dismiss.job(
            job_id="jobId",
        )
        """
        _response = self._raw_client.job(job_id, request_options=request_options)
        return _response.data


class AsyncDismissClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDismissClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDismissClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDismissClient
        """
        return self._raw_client

    async def job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> JobInfo:
        """
        Cancel a job execution and removes it from the jobs list.

        For more information, see [OGC API — Processes — Part 1 Section 13](https://docs.ogc.org/is/18-062r2/18-062r2.html#Dismiss).

        Parameters
        ----------
        job_id : str
            Local identifier of a job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfo
            Information about the job.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dismiss.job(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.job(job_id, request_options=request_options)
        return _response.data
