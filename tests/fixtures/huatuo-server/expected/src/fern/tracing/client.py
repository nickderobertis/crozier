

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.apis_v1components_observation_scope import ApisV1ComponentsObservationScope
from ..types.tracing_capabilities_response import TracingCapabilitiesResponse
from ..types.tracing_job_list_response import TracingJobListResponse
from ..types.tracing_job_response import TracingJobResponse
from ..types.tracing_type import TracingType
from .raw_client import AsyncRawTracingClient, RawTracingClient


OMIT = typing.cast(typing.Any, ...)


class TracingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTracingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTracingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTracingClient
        """
        return self._raw_client

    def list_tracing_jobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TracingJobListResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracingJobListResponse
            Tracing Jobs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tracing.list_tracing_jobs()
        """
        _response = self._raw_client.list_tracing_jobs(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def create_tracing_job(
        self,
        *,
        duration_seconds: int,
        hostname: str,
        scope: ApisV1ComponentsObservationScope,
        type: TracingType,
        container_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TracingJobResponse:
        """
        Parameters
        ----------
        duration_seconds : int

        hostname : str

        scope : ApisV1ComponentsObservationScope

        type : TracingType

        container_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracingJobResponse
            Tracing Job created.

        Examples
        --------
        from fern import ApisV1ComponentsObservationScope, FernApi, TracingType

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tracing.create_tracing_job(
            duration_seconds=1000000,
            hostname="hostname",
            scope=ApisV1ComponentsObservationScope.HOST,
            type=TracingType.NETWORKING_DROP,
        )
        """
        _response = self._raw_client.create_tracing_job(
            duration_seconds=duration_seconds,
            hostname=hostname,
            scope=scope,
            type=type,
            container_id=container_id,
            request_options=request_options,
        )
        return _response.data

    def get_tracing_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TracingCapabilitiesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracingCapabilitiesResponse
            Static tracing capabilities.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tracing.get_tracing_capabilities()
        """
        _response = self._raw_client.get_tracing_capabilities(request_options=request_options)
        return _response.data

    def get_tracing_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TracingJobResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracingJobResponse
            Tracing Job.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tracing.get_tracing_job(
            request_id="request_id",
        )
        """
        _response = self._raw_client.get_tracing_job(request_id, request_options=request_options)
        return _response.data

    def stop_tracing_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TracingJobResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracingJobResponse
            Current Tracing Job after applying the stop intent.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tracing.stop_tracing_job(
            request_id="request_id",
        )
        """
        _response = self._raw_client.stop_tracing_job(request_id, request_options=request_options)
        return _response.data


class AsyncTracingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTracingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTracingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTracingClient
        """
        return self._raw_client

    async def list_tracing_jobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TracingJobListResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracingJobListResponse
            Tracing Jobs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tracing.list_tracing_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tracing_jobs(
            limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def create_tracing_job(
        self,
        *,
        duration_seconds: int,
        hostname: str,
        scope: ApisV1ComponentsObservationScope,
        type: TracingType,
        container_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TracingJobResponse:
        """
        Parameters
        ----------
        duration_seconds : int

        hostname : str

        scope : ApisV1ComponentsObservationScope

        type : TracingType

        container_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracingJobResponse
            Tracing Job created.

        Examples
        --------
        import asyncio

        from fern import ApisV1ComponentsObservationScope, AsyncFernApi, TracingType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tracing.create_tracing_job(
                duration_seconds=1000000,
                hostname="hostname",
                scope=ApisV1ComponentsObservationScope.HOST,
                type=TracingType.NETWORKING_DROP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tracing_job(
            duration_seconds=duration_seconds,
            hostname=hostname,
            scope=scope,
            type=type,
            container_id=container_id,
            request_options=request_options,
        )
        return _response.data

    async def get_tracing_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TracingCapabilitiesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracingCapabilitiesResponse
            Static tracing capabilities.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tracing.get_tracing_capabilities()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tracing_capabilities(request_options=request_options)
        return _response.data

    async def get_tracing_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TracingJobResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracingJobResponse
            Tracing Job.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tracing.get_tracing_job(
                request_id="request_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tracing_job(request_id, request_options=request_options)
        return _response.data

    async def stop_tracing_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TracingJobResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracingJobResponse
            Current Tracing Job after applying the stop intent.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tracing.stop_tracing_job(
                request_id="request_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_tracing_job(request_id, request_options=request_options)
        return _response.data
