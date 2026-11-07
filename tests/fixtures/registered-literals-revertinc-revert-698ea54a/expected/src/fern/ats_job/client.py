

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ats_create_or_update_job_request import AtsCreateOrUpdateJobRequest
from ..types.ats_create_or_update_job_response import AtsCreateOrUpdateJobResponse
from ..types.ats_delete_job_response import AtsDeleteJobResponse
from ..types.ats_get_job_response import AtsGetJobResponse
from ..types.ats_get_jobs_response import AtsGetJobsResponse
from .raw_client import AsyncRawAtsJobClient, RawAtsJobClient


OMIT = typing.cast(typing.Any, ...)


class AtsJobClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAtsJobClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAtsJobClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAtsJobClient
        """
        return self._raw_client

    def ats_job_get_job(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsGetJobResponse:
        """
        Get details of a job.

        Parameters
        ----------
        id : str
            The unique `id` of the job.

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetJobResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_job.ats_job_get_job(
            id="id",
        )
        """
        _response = self._raw_client.ats_job_get_job(id, fields=fields, request_options=request_options)
        return _response.data

    def ats_job_delete_job(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsDeleteJobResponse:
        """
        Delete details of an Job

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsDeleteJobResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_job.ats_job_delete_job(
            id="id",
        )
        """
        _response = self._raw_client.ats_job_delete_job(id, fields=fields, request_options=request_options)
        return _response.data

    def ats_job_update_job(
        self,
        id: str,
        *,
        request: AtsCreateOrUpdateJobRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateJobResponse:
        """
        Update a Job

        Parameters
        ----------
        id : str

        request : AtsCreateOrUpdateJobRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateJobResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_job.ats_job_update_job(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.ats_job_update_job(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    def ats_job_get_jobs(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsGetJobsResponse:
        """
        Get all the jobs.

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetJobsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_job.ats_job_get_jobs()
        """
        _response = self._raw_client.ats_job_get_jobs(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    def ats_job_create_job(
        self,
        *,
        request: AtsCreateOrUpdateJobRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateJobResponse:
        """
        Create a new Job

        Parameters
        ----------
        request : AtsCreateOrUpdateJobRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateJobResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_job.ats_job_create_job(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.ats_job_create_job(request=request, fields=fields, request_options=request_options)
        return _response.data


class AsyncAtsJobClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAtsJobClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAtsJobClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAtsJobClient
        """
        return self._raw_client

    async def ats_job_get_job(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsGetJobResponse:
        """
        Get details of a job.

        Parameters
        ----------
        id : str
            The unique `id` of the job.

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetJobResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_job.ats_job_get_job(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_job_get_job(id, fields=fields, request_options=request_options)
        return _response.data

    async def ats_job_delete_job(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsDeleteJobResponse:
        """
        Delete details of an Job

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsDeleteJobResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_job.ats_job_delete_job(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_job_delete_job(id, fields=fields, request_options=request_options)
        return _response.data

    async def ats_job_update_job(
        self,
        id: str,
        *,
        request: AtsCreateOrUpdateJobRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateJobResponse:
        """
        Update a Job

        Parameters
        ----------
        id : str

        request : AtsCreateOrUpdateJobRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateJobResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_job.ats_job_update_job(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_job_update_job(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    async def ats_job_get_jobs(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsGetJobsResponse:
        """
        Get all the jobs.

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetJobsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_job.ats_job_get_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_job_get_jobs(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def ats_job_create_job(
        self,
        *,
        request: AtsCreateOrUpdateJobRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateJobResponse:
        """
        Create a new Job

        Parameters
        ----------
        request : AtsCreateOrUpdateJobRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateJobResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_job.ats_job_create_job(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_job_create_job(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data
