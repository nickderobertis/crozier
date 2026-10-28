

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawProcessingServiceClient, RawProcessingServiceClient


class ProcessingServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProcessingServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProcessingServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProcessingServiceClient
        """
        return self._raw_client

    def get_processes(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Returns list of all available processes from config.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.processing_service.get_processes()
        """
        _response = self._raw_client.get_processes(request_options=request_options)
        return _response.data

    def get_resource(self, resource: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Should return info about a specific resource.

        Parameters
        ----------
        resource : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.processing_service.get_resource(
            resource="resource",
        )
        """
        _response = self._raw_client.get_resource(resource, request_options=request_options)
        return _response.data

    def execute_process(self, resource: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Used to execute processing jobs.

        Parameters
        ----------
        resource : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.processing_service.execute_process(
            resource="resource",
        )
        """
        _response = self._raw_client.execute_process(resource, request_options=request_options)
        return _response.data

    def get_job_logs_endpoint(
        self, job_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Used to stream logs of a processing job.

        Parameters
        ----------
        job_id : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.processing_service.get_job_logs_endpoint(
            job_id="job_id",
        )
        """
        _response = self._raw_client.get_job_logs_endpoint(job_id, request_options=request_options)
        return _response.data

    def get_job_status_endpoint(
        self, job_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Used to get status of processing job.

        Parameters
        ----------
        job_id : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.processing_service.get_job_status_endpoint(
            job_id="job_id",
        )
        """
        _response = self._raw_client.get_job_status_endpoint(job_id, request_options=request_options)
        return _response.data

    def delete_job_endpoint(
        self, job_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Deletes a specific job from the database.

        Parameters
        ----------
        job_id : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.processing_service.delete_job_endpoint(
            job_id="job_id",
        )
        """
        _response = self._raw_client.delete_job_endpoint(job_id, request_options=request_options)
        return _response.data

    def get_jobs_endpoint(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Returns the status of all jobs from database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.processing_service.get_jobs_endpoint()
        """
        _response = self._raw_client.get_jobs_endpoint(request_options=request_options)
        return _response.data


class AsyncProcessingServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProcessingServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProcessingServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProcessingServiceClient
        """
        return self._raw_client

    async def get_processes(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Returns list of all available processes from config.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.processing_service.get_processes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_processes(request_options=request_options)
        return _response.data

    async def get_resource(
        self, resource: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Should return info about a specific resource.

        Parameters
        ----------
        resource : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.processing_service.get_resource(
                resource="resource",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_resource(resource, request_options=request_options)
        return _response.data

    async def execute_process(
        self, resource: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Used to execute processing jobs.

        Parameters
        ----------
        resource : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.processing_service.execute_process(
                resource="resource",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_process(resource, request_options=request_options)
        return _response.data

    async def get_job_logs_endpoint(
        self, job_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Used to stream logs of a processing job.

        Parameters
        ----------
        job_id : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.processing_service.get_job_logs_endpoint(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_logs_endpoint(job_id, request_options=request_options)
        return _response.data

    async def get_job_status_endpoint(
        self, job_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Used to get status of processing job.

        Parameters
        ----------
        job_id : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.processing_service.get_job_status_endpoint(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_status_endpoint(job_id, request_options=request_options)
        return _response.data

    async def delete_job_endpoint(
        self, job_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Deletes a specific job from the database.

        Parameters
        ----------
        job_id : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.processing_service.delete_job_endpoint(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_job_endpoint(job_id, request_options=request_options)
        return _response.data

    async def get_jobs_endpoint(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Returns the status of all jobs from database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.processing_service.get_jobs_endpoint()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_endpoint(request_options=request_options)
        return _response.data
