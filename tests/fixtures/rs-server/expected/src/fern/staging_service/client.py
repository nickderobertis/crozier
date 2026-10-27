

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.input_model import InputModel
from .raw_client import AsyncRawStagingServiceClient, RawStagingServiceClient


OMIT = typing.cast(typing.Any, ...)


class StagingServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStagingServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStagingServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStagingServiceClient
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
        client.staging_service.get_processes()
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
        client.staging_service.get_resource(
            resource="resource",
        )
        """
        _response = self._raw_client.get_resource(resource, request_options=request_options)
        return _response.data

    def execute_process(
        self, resource: str, *, inputs: InputModel, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Used to execute processing jobs.

        Parameters
        ----------
        resource : str

        inputs : InputModel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, InputModel, ItemsModel

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.staging_service.execute_process(
            resource="resource",
            inputs=InputModel(
                collection="collection",
                items=ItemsModel(),
            ),
        )
        """
        _response = self._raw_client.execute_process(resource, inputs=inputs, request_options=request_options)
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
        client.staging_service.get_job_status_endpoint(
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
        client.staging_service.delete_job_endpoint(
            job_id="job_id",
        )
        """
        _response = self._raw_client.delete_job_endpoint(job_id, request_options=request_options)
        return _response.data

    def get_jobs_endpoint(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Returns the status of all jobs.

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
        client.staging_service.get_jobs_endpoint()
        """
        _response = self._raw_client.get_jobs_endpoint(request_options=request_options)
        return _response.data

    def get_specific_job_result_endpoint(
        self, job_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get result from a specific job.

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
        client.staging_service.get_specific_job_result_endpoint(
            job_id="job_id",
        )
        """
        _response = self._raw_client.get_specific_job_result_endpoint(job_id, request_options=request_options)
        return _response.data


class AsyncStagingServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStagingServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStagingServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStagingServiceClient
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
            await client.staging_service.get_processes()


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
            await client.staging_service.get_resource(
                resource="resource",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_resource(resource, request_options=request_options)
        return _response.data

    async def execute_process(
        self, resource: str, *, inputs: InputModel, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Used to execute processing jobs.

        Parameters
        ----------
        resource : str

        inputs : InputModel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, InputModel, ItemsModel

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.staging_service.execute_process(
                resource="resource",
                inputs=InputModel(
                    collection="collection",
                    items=ItemsModel(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_process(resource, inputs=inputs, request_options=request_options)
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
            await client.staging_service.get_job_status_endpoint(
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
            await client.staging_service.delete_job_endpoint(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_job_endpoint(job_id, request_options=request_options)
        return _response.data

    async def get_jobs_endpoint(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Returns the status of all jobs.

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
            await client.staging_service.get_jobs_endpoint()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_endpoint(request_options=request_options)
        return _response.data

    async def get_specific_job_result_endpoint(
        self, job_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get result from a specific job.

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
            await client.staging_service.get_specific_job_result_endpoint(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_specific_job_result_endpoint(job_id, request_options=request_options)
        return _response.data
