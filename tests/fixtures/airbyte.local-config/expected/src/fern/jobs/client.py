

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attempt_normalization_status_read_list import AttemptNormalizationStatusReadList
from ..types.connection_id import ConnectionId
from ..types.job_config_type import JobConfigType
from ..types.job_debug_info_read import JobDebugInfoRead
from ..types.job_id import JobId
from ..types.job_info_light_read import JobInfoLightRead
from ..types.job_info_read import JobInfoRead
from ..types.job_optional_read import JobOptionalRead
from ..types.job_read_list import JobReadList
from ..types.pagination import Pagination
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

    def cancel_job(self, *, id: JobId, request_options: typing.Optional[RequestOptions] = None) -> JobInfoRead:
        """
        Parameters
        ----------
        id : JobId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfoRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.cancel_job(
            id=1000000,
        )
        """
        _response = self._raw_client.cancel_job(id=id, request_options=request_options)
        return _response.data

    def get_job_info(self, *, id: JobId, request_options: typing.Optional[RequestOptions] = None) -> JobInfoRead:
        """
        Parameters
        ----------
        id : JobId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfoRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_job_info(
            id=1000000,
        )
        """
        _response = self._raw_client.get_job_info(id=id, request_options=request_options)
        return _response.data

    def get_job_debug_info(
        self, *, id: JobId, request_options: typing.Optional[RequestOptions] = None
    ) -> JobDebugInfoRead:
        """
        Parameters
        ----------
        id : JobId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobDebugInfoRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_job_debug_info(
            id=1000000,
        )
        """
        _response = self._raw_client.get_job_debug_info(id=id, request_options=request_options)
        return _response.data

    def get_last_replication_job(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> JobOptionalRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobOptionalRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_last_replication_job(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.get_last_replication_job(
            connection_id=connection_id, request_options=request_options
        )
        return _response.data

    def get_job_info_light(
        self, *, id: JobId, request_options: typing.Optional[RequestOptions] = None
    ) -> JobInfoLightRead:
        """
        Parameters
        ----------
        id : JobId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfoLightRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_job_info_light(
            id=1000000,
        )
        """
        _response = self._raw_client.get_job_info_light(id=id, request_options=request_options)
        return _response.data

    def get_attempt_normalization_statuses_for_job(
        self, *, id: JobId, request_options: typing.Optional[RequestOptions] = None
    ) -> AttemptNormalizationStatusReadList:
        """
        Parameters
        ----------
        id : JobId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttemptNormalizationStatusReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_attempt_normalization_statuses_for_job(
            id=1000000,
        )
        """
        _response = self._raw_client.get_attempt_normalization_statuses_for_job(id=id, request_options=request_options)
        return _response.data

    def list_jobs_for(
        self,
        *,
        config_id: str,
        config_types: typing.Sequence[JobConfigType],
        including_job_id: typing.Optional[JobId] = OMIT,
        pagination: typing.Optional[Pagination] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobReadList:
        """
        Parameters
        ----------
        config_id : str

        config_types : typing.Sequence[JobConfigType]

        including_job_id : typing.Optional[JobId]
            If the job with this ID exists for the specified connection, returns the number of pages of jobs necessary to include this job. Returns an empty list if this job is specified and cannot be found in this connection.

        pagination : typing.Optional[Pagination]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobReadList
            Successful operation

        Examples
        --------
        from fern import FernApi, JobConfigType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.list_jobs_for(
            config_id="configId",
            config_types=[JobConfigType.CHECK_CONNECTION_SOURCE],
        )
        """
        _response = self._raw_client.list_jobs_for(
            config_id=config_id,
            config_types=config_types,
            including_job_id=including_job_id,
            pagination=pagination,
            request_options=request_options,
        )
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

    async def cancel_job(self, *, id: JobId, request_options: typing.Optional[RequestOptions] = None) -> JobInfoRead:
        """
        Parameters
        ----------
        id : JobId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfoRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.cancel_job(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_job(id=id, request_options=request_options)
        return _response.data

    async def get_job_info(self, *, id: JobId, request_options: typing.Optional[RequestOptions] = None) -> JobInfoRead:
        """
        Parameters
        ----------
        id : JobId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfoRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_job_info(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_info(id=id, request_options=request_options)
        return _response.data

    async def get_job_debug_info(
        self, *, id: JobId, request_options: typing.Optional[RequestOptions] = None
    ) -> JobDebugInfoRead:
        """
        Parameters
        ----------
        id : JobId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobDebugInfoRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_job_debug_info(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_debug_info(id=id, request_options=request_options)
        return _response.data

    async def get_last_replication_job(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> JobOptionalRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobOptionalRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_last_replication_job(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_last_replication_job(
            connection_id=connection_id, request_options=request_options
        )
        return _response.data

    async def get_job_info_light(
        self, *, id: JobId, request_options: typing.Optional[RequestOptions] = None
    ) -> JobInfoLightRead:
        """
        Parameters
        ----------
        id : JobId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfoLightRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_job_info_light(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_info_light(id=id, request_options=request_options)
        return _response.data

    async def get_attempt_normalization_statuses_for_job(
        self, *, id: JobId, request_options: typing.Optional[RequestOptions] = None
    ) -> AttemptNormalizationStatusReadList:
        """
        Parameters
        ----------
        id : JobId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttemptNormalizationStatusReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_attempt_normalization_statuses_for_job(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_attempt_normalization_statuses_for_job(
            id=id, request_options=request_options
        )
        return _response.data

    async def list_jobs_for(
        self,
        *,
        config_id: str,
        config_types: typing.Sequence[JobConfigType],
        including_job_id: typing.Optional[JobId] = OMIT,
        pagination: typing.Optional[Pagination] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobReadList:
        """
        Parameters
        ----------
        config_id : str

        config_types : typing.Sequence[JobConfigType]

        including_job_id : typing.Optional[JobId]
            If the job with this ID exists for the specified connection, returns the number of pages of jobs necessary to include this job. Returns an empty list if this job is specified and cannot be found in this connection.

        pagination : typing.Optional[Pagination]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, JobConfigType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.list_jobs_for(
                config_id="configId",
                config_types=[JobConfigType.CHECK_CONNECTION_SOURCE],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_jobs_for(
            config_id=config_id,
            config_types=config_types,
            including_job_id=including_job_id,
            pagination=pagination,
            request_options=request_options,
        )
        return _response.data
