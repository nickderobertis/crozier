

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.periodic_job import PeriodicJob
from ..types.periodic_job_catalog import PeriodicJobCatalog
from ..types.periodic_job_list import PeriodicJobList
from .raw_client import AsyncRawPeriodicJobsClient, RawPeriodicJobsClient


OMIT = typing.cast(typing.Any, ...)


class PeriodicJobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPeriodicJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPeriodicJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPeriodicJobsClient
        """
        return self._raw_client

    def list_periodic_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> PeriodicJobList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJobList
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.periodic_jobs.list_periodic_jobs()
        """
        _response = self._raw_client.list_periodic_jobs(request_options=request_options)
        return _response.data

    def create_periodic_job(
        self,
        *,
        id: str,
        kind: str,
        args: typing.Dict[str, typing.Any],
        queue: str,
        priority: int,
        max_attempts: int,
        tags: typing.Sequence[str],
        cron_expression: str,
        cron_timezone: str,
        paused: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PeriodicJob:
        """
        Parameters
        ----------
        id : str

        kind : str

        args : typing.Dict[str, typing.Any]

        queue : str

        priority : int

        max_attempts : int

        tags : typing.Sequence[str]

        cron_expression : str

        cron_timezone : str

        paused : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJob
            The request has succeeded and a new resource has been created as a result.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.periodic_jobs.create_periodic_job(
            id="id",
            kind="kind",
            args={"key": "value"},
            queue="queue",
            priority=1,
            max_attempts=1,
            tags=["tags"],
            cron_expression="cronExpression",
            cron_timezone="cronTimezone",
        )
        """
        _response = self._raw_client.create_periodic_job(
            id=id,
            kind=kind,
            args=args,
            queue=queue,
            priority=priority,
            max_attempts=max_attempts,
            tags=tags,
            cron_expression=cron_expression,
            cron_timezone=cron_timezone,
            paused=paused,
            request_options=request_options,
        )
        return _response.data

    def get_periodic_job_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PeriodicJobCatalog:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJobCatalog
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.periodic_jobs.get_periodic_job_catalog()
        """
        _response = self._raw_client.get_periodic_job_catalog(request_options=request_options)
        return _response.data

    def reset_periodic_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> PeriodicJobList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJobList
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.periodic_jobs.reset_periodic_jobs()
        """
        _response = self._raw_client.reset_periodic_jobs(request_options=request_options)
        return _response.data

    def update_periodic_job(
        self,
        periodic_job_id: str,
        *,
        kind: str,
        args: typing.Dict[str, typing.Any],
        queue: str,
        priority: int,
        max_attempts: int,
        tags: typing.Sequence[str],
        cron_expression: str,
        cron_timezone: str,
        paused: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PeriodicJob:
        """
        Parameters
        ----------
        periodic_job_id : str

        kind : str

        args : typing.Dict[str, typing.Any]

        queue : str

        priority : int

        max_attempts : int

        tags : typing.Sequence[str]

        cron_expression : str

        cron_timezone : str

        paused : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJob
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.periodic_jobs.update_periodic_job(
            periodic_job_id="periodicJobId",
            kind="kind",
            args={"key": "value"},
            queue="queue",
            priority=1,
            max_attempts=1,
            tags=["tags"],
            cron_expression="cronExpression",
            cron_timezone="cronTimezone",
        )
        """
        _response = self._raw_client.update_periodic_job(
            periodic_job_id,
            kind=kind,
            args=args,
            queue=queue,
            priority=priority,
            max_attempts=max_attempts,
            tags=tags,
            cron_expression=cron_expression,
            cron_timezone=cron_timezone,
            paused=paused,
            request_options=request_options,
        )
        return _response.data

    def delete_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        periodic_job_id : str

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
        client.periodic_jobs.delete_periodic_job(
            periodic_job_id="periodicJobId",
        )
        """
        _response = self._raw_client.delete_periodic_job(periodic_job_id, request_options=request_options)
        return _response.data

    def pause_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PeriodicJob:
        """
        Parameters
        ----------
        periodic_job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJob
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.periodic_jobs.pause_periodic_job(
            periodic_job_id="periodicJobId",
        )
        """
        _response = self._raw_client.pause_periodic_job(periodic_job_id, request_options=request_options)
        return _response.data

    def resume_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PeriodicJob:
        """
        Parameters
        ----------
        periodic_job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJob
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.periodic_jobs.resume_periodic_job(
            periodic_job_id="periodicJobId",
        )
        """
        _response = self._raw_client.resume_periodic_job(periodic_job_id, request_options=request_options)
        return _response.data


class AsyncPeriodicJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPeriodicJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPeriodicJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPeriodicJobsClient
        """
        return self._raw_client

    async def list_periodic_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> PeriodicJobList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJobList
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
            await client.periodic_jobs.list_periodic_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_periodic_jobs(request_options=request_options)
        return _response.data

    async def create_periodic_job(
        self,
        *,
        id: str,
        kind: str,
        args: typing.Dict[str, typing.Any],
        queue: str,
        priority: int,
        max_attempts: int,
        tags: typing.Sequence[str],
        cron_expression: str,
        cron_timezone: str,
        paused: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PeriodicJob:
        """
        Parameters
        ----------
        id : str

        kind : str

        args : typing.Dict[str, typing.Any]

        queue : str

        priority : int

        max_attempts : int

        tags : typing.Sequence[str]

        cron_expression : str

        cron_timezone : str

        paused : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJob
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
            await client.periodic_jobs.create_periodic_job(
                id="id",
                kind="kind",
                args={"key": "value"},
                queue="queue",
                priority=1,
                max_attempts=1,
                tags=["tags"],
                cron_expression="cronExpression",
                cron_timezone="cronTimezone",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_periodic_job(
            id=id,
            kind=kind,
            args=args,
            queue=queue,
            priority=priority,
            max_attempts=max_attempts,
            tags=tags,
            cron_expression=cron_expression,
            cron_timezone=cron_timezone,
            paused=paused,
            request_options=request_options,
        )
        return _response.data

    async def get_periodic_job_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PeriodicJobCatalog:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJobCatalog
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
            await client.periodic_jobs.get_periodic_job_catalog()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_periodic_job_catalog(request_options=request_options)
        return _response.data

    async def reset_periodic_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> PeriodicJobList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJobList
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
            await client.periodic_jobs.reset_periodic_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_periodic_jobs(request_options=request_options)
        return _response.data

    async def update_periodic_job(
        self,
        periodic_job_id: str,
        *,
        kind: str,
        args: typing.Dict[str, typing.Any],
        queue: str,
        priority: int,
        max_attempts: int,
        tags: typing.Sequence[str],
        cron_expression: str,
        cron_timezone: str,
        paused: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PeriodicJob:
        """
        Parameters
        ----------
        periodic_job_id : str

        kind : str

        args : typing.Dict[str, typing.Any]

        queue : str

        priority : int

        max_attempts : int

        tags : typing.Sequence[str]

        cron_expression : str

        cron_timezone : str

        paused : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJob
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
            await client.periodic_jobs.update_periodic_job(
                periodic_job_id="periodicJobId",
                kind="kind",
                args={"key": "value"},
                queue="queue",
                priority=1,
                max_attempts=1,
                tags=["tags"],
                cron_expression="cronExpression",
                cron_timezone="cronTimezone",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_periodic_job(
            periodic_job_id,
            kind=kind,
            args=args,
            queue=queue,
            priority=priority,
            max_attempts=max_attempts,
            tags=tags,
            cron_expression=cron_expression,
            cron_timezone=cron_timezone,
            paused=paused,
            request_options=request_options,
        )
        return _response.data

    async def delete_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        periodic_job_id : str

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
            await client.periodic_jobs.delete_periodic_job(
                periodic_job_id="periodicJobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_periodic_job(periodic_job_id, request_options=request_options)
        return _response.data

    async def pause_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PeriodicJob:
        """
        Parameters
        ----------
        periodic_job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJob
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
            await client.periodic_jobs.pause_periodic_job(
                periodic_job_id="periodicJobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pause_periodic_job(periodic_job_id, request_options=request_options)
        return _response.data

    async def resume_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PeriodicJob:
        """
        Parameters
        ----------
        periodic_job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PeriodicJob
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
            await client.periodic_jobs.resume_periodic_job(
                periodic_job_id="periodicJobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resume_periodic_job(periodic_job_id, request_options=request_options)
        return _response.data
