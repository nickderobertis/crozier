

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_build_system_shared_dto_job import ApiPagedResponseBuildSystemSharedDtoJob
from ..types.build_system_shared_dto_job import BuildSystemSharedDtoJob
from ..types.build_system_shared_dto_job_activity import BuildSystemSharedDtoJobActivity
from ..types.build_system_shared_dto_parameter import BuildSystemSharedDtoParameter
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

    def getjobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoJob:
        """
        Gets a collection of Jobs. When successful, the response is a PagedResponse of Jobs.
                    If unsuccessful, an appropriate ApiError is returned.
                    ///

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted job, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoJob
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.jobs.getjobs()
        """
        _response = self._raw_client.getjobs(
            limit=limit, offset=offset, is_include_deleted=is_include_deleted, request_options=request_options
        )
        return _response.data

    def postjob(
        self,
        *,
        activities: typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a Job.  The body of the POST is the Job to create.  The JobID will be assigned on
                    creation of the Job.  When successful, the response is the JobID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activities : typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]]
            The activities which are performed for the job

        deleted : typing.Optional[bool]
            Indicates if the job has been deleted.

        job_id : typing.Optional[int]
            The ID of the job

        name : typing.Optional[str]
            The name of the job

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.jobs.postjob()
        """
        _response = self._raw_client.postjob(
            activities=activities,
            deleted=deleted,
            job_id=job_id,
            name=name,
            parameters=parameters,
            request_options=request_options,
        )
        return _response.data

    def getjob(
        self,
        job_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildSystemSharedDtoJob:
        """
        Gets a Job by ID. When successful, the response is the requested Job.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_id : int
            The ID of the Job to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted job, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoJob
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.jobs.getjob(
            job_id=1,
        )
        """
        _response = self._raw_client.getjob(
            job_id, is_include_deleted=is_include_deleted, request_options=request_options
        )
        return _response.data

    def putjob(
        self,
        job_id_: int,
        *,
        activities: typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a Job.  The body of the PUT is the updated Job.  When successful, the response is empty.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_id_ : int
            The id of the job to update

        activities : typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]]
            The activities which are performed for the job

        deleted : typing.Optional[bool]
            Indicates if the job has been deleted.

        job_id : typing.Optional[int]
            The ID of the job

        name : typing.Optional[str]
            The name of the job

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.jobs.putjob(
            job_id_=1,
        )
        """
        _response = self._raw_client.putjob(
            job_id_,
            activities=activities,
            deleted=deleted,
            job_id=job_id,
            name=name,
            parameters=parameters,
            request_options=request_options,
        )
        return _response.data

    def deletejob(self, job_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a Job. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        job_id : int
            The id of the job to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.jobs.deletejob(
            job_id=1,
        )
        """
        _response = self._raw_client.deletejob(job_id, request_options=request_options)
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

    async def getjobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoJob:
        """
        Gets a collection of Jobs. When successful, the response is a PagedResponse of Jobs.
                    If unsuccessful, an appropriate ApiError is returned.
                    ///

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted job, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoJob
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.jobs.getjobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.getjobs(
            limit=limit, offset=offset, is_include_deleted=is_include_deleted, request_options=request_options
        )
        return _response.data

    async def postjob(
        self,
        *,
        activities: typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a Job.  The body of the POST is the Job to create.  The JobID will be assigned on
                    creation of the Job.  When successful, the response is the JobID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activities : typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]]
            The activities which are performed for the job

        deleted : typing.Optional[bool]
            Indicates if the job has been deleted.

        job_id : typing.Optional[int]
            The ID of the job

        name : typing.Optional[str]
            The name of the job

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.jobs.postjob()


        asyncio.run(main())
        """
        _response = await self._raw_client.postjob(
            activities=activities,
            deleted=deleted,
            job_id=job_id,
            name=name,
            parameters=parameters,
            request_options=request_options,
        )
        return _response.data

    async def getjob(
        self,
        job_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildSystemSharedDtoJob:
        """
        Gets a Job by ID. When successful, the response is the requested Job.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_id : int
            The ID of the Job to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted job, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoJob
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.jobs.getjob(
                job_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getjob(
            job_id, is_include_deleted=is_include_deleted, request_options=request_options
        )
        return _response.data

    async def putjob(
        self,
        job_id_: int,
        *,
        activities: typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a Job.  The body of the PUT is the updated Job.  When successful, the response is empty.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_id_ : int
            The id of the job to update

        activities : typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]]
            The activities which are performed for the job

        deleted : typing.Optional[bool]
            Indicates if the job has been deleted.

        job_id : typing.Optional[int]
            The ID of the job

        name : typing.Optional[str]
            The name of the job

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.jobs.putjob(
                job_id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putjob(
            job_id_,
            activities=activities,
            deleted=deleted,
            job_id=job_id,
            name=name,
            parameters=parameters,
            request_options=request_options,
        )
        return _response.data

    async def deletejob(self, job_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a Job. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        job_id : int
            The id of the job to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.jobs.deletejob(
                job_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletejob(job_id, request_options=request_options)
        return _response.data
