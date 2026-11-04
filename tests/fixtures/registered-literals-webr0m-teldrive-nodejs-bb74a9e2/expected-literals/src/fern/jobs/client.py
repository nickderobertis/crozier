

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cursor import Cursor
from ..types.job import Job
from ..types.job_page import JobPage
from ..types.job_purge_result import JobPurgeResult
from ..types.job_queue_list import JobQueueList
from ..types.job_state import JobState
from ..types.job_statistics import JobStatistics
from .raw_client import AsyncRawJobsClient, RawJobsClient


OMIT = typing.cast(typing.Any, ...)


class JobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobsClient
        """
        return self._raw_client

    def list_jobs(
        self,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        status: typing.Optional[JobState] = None,
        type: typing.Optional[str] = None,
        queue: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobPage:
        """
        Parameters
        ----------
        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        status : typing.Optional[JobState]

        type : typing.Optional[str]

        queue : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPage
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.jobs.list_jobs()
        """
        _response = self._raw_client.list_jobs(
            cursor=cursor, limit=limit, status=status, type=type, queue=queue, request_options=request_options
        )
        return _response.data

    def create_job(
        self,
        *,
        type: str,
        args: typing.Dict[str, typing.Any],
        queue: typing.Optional[str] = OMIT,
        priority: typing.Optional[int] = OMIT,
        max_attempts: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Job:
        """
        Parameters
        ----------
        type : str

        args : typing.Dict[str, typing.Any]

        queue : typing.Optional[str]

        priority : typing.Optional[int]

        max_attempts : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            The request has succeeded and a new resource has been created as a result.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.jobs.create_job(
            type="type",
            args={"key": "value"},
        )
        """
        _response = self._raw_client.create_job(
            type=type,
            args=args,
            queue=queue,
            priority=priority,
            max_attempts=max_attempts,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def get_job_statistics(self, *, request_options: typing.Optional[RequestOptions] = None) -> JobStatistics:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobStatistics
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.jobs.get_job_statistics()
        """
        _response = self._raw_client.get_job_statistics(request_options=request_options)
        return _response.data

    def list_job_queues(self, *, request_options: typing.Optional[RequestOptions] = None) -> JobQueueList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobQueueList
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.jobs.list_job_queues()
        """
        _response = self._raw_client.list_job_queues(request_options=request_options)
        return _response.data

    def pause_job_queue(self, queue: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        queue : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.jobs.pause_job_queue(
            queue="queue",
        )
        """
        _response = self._raw_client.pause_job_queue(queue, request_options=request_options)
        return _response.data

    def resume_job_queue(self, queue: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        queue : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.jobs.resume_job_queue(
            queue="queue",
        )
        """
        _response = self._raw_client.resume_job_queue(queue, request_options=request_options)
        return _response.data

    def purge_jobs(
        self, *, status: JobState, request_options: typing.Optional[RequestOptions] = None
    ) -> JobPurgeResult:
        """
        Parameters
        ----------
        status : JobState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPurgeResult
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.jobs.purge_jobs(
            status="available",
        )
        """
        _response = self._raw_client.purge_jobs(status=status, request_options=request_options)
        return _response.data

    def get_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Job:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.jobs.get_job(
            job_id="jobId",
        )
        """
        _response = self._raw_client.get_job(job_id, request_options=request_options)
        return _response.data

    def delete_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.jobs.delete_job(
            job_id="jobId",
        )
        """
        _response = self._raw_client.delete_job(job_id, request_options=request_options)
        return _response.data

    def cancel_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Job:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.jobs.cancel_job(
            job_id="jobId",
        )
        """
        _response = self._raw_client.cancel_job(job_id, request_options=request_options)
        return _response.data

    def retry_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Job:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.jobs.retry_job(
            job_id="jobId",
        )
        """
        _response = self._raw_client.retry_job(job_id, request_options=request_options)
        return _response.data


class AsyncJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobsClient
        """
        return self._raw_client

    async def list_jobs(
        self,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        status: typing.Optional[JobState] = None,
        type: typing.Optional[str] = None,
        queue: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobPage:
        """
        Parameters
        ----------
        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        status : typing.Optional[JobState]

        type : typing.Optional[str]

        queue : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPage
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.list_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_jobs(
            cursor=cursor, limit=limit, status=status, type=type, queue=queue, request_options=request_options
        )
        return _response.data

    async def create_job(
        self,
        *,
        type: str,
        args: typing.Dict[str, typing.Any],
        queue: typing.Optional[str] = OMIT,
        priority: typing.Optional[int] = OMIT,
        max_attempts: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Job:
        """
        Parameters
        ----------
        type : str

        args : typing.Dict[str, typing.Any]

        queue : typing.Optional[str]

        priority : typing.Optional[int]

        max_attempts : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            The request has succeeded and a new resource has been created as a result.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.create_job(
                type="type",
                args={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_job(
            type=type,
            args=args,
            queue=queue,
            priority=priority,
            max_attempts=max_attempts,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def get_job_statistics(self, *, request_options: typing.Optional[RequestOptions] = None) -> JobStatistics:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobStatistics
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_job_statistics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_statistics(request_options=request_options)
        return _response.data

    async def list_job_queues(self, *, request_options: typing.Optional[RequestOptions] = None) -> JobQueueList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobQueueList
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.list_job_queues()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_job_queues(request_options=request_options)
        return _response.data

    async def pause_job_queue(self, queue: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        queue : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.pause_job_queue(
                queue="queue",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pause_job_queue(queue, request_options=request_options)
        return _response.data

    async def resume_job_queue(self, queue: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        queue : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.resume_job_queue(
                queue="queue",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resume_job_queue(queue, request_options=request_options)
        return _response.data

    async def purge_jobs(
        self, *, status: JobState, request_options: typing.Optional[RequestOptions] = None
    ) -> JobPurgeResult:
        """
        Parameters
        ----------
        status : JobState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPurgeResult
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.purge_jobs(
                status="available",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.purge_jobs(status=status, request_options=request_options)
        return _response.data

    async def get_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Job:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_job(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job(job_id, request_options=request_options)
        return _response.data

    async def delete_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.delete_job(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_job(job_id, request_options=request_options)
        return _response.data

    async def cancel_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Job:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.cancel_job(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_job(job_id, request_options=request_options)
        return _response.data

    async def retry_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Job:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.retry_job(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retry_job(job_id, request_options=request_options)
        return _response.data
